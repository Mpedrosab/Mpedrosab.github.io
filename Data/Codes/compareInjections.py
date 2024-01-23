# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06  2022

@author: M. Pedrosa Bustos
"""
import matplotlib.pyplot as plt
from monolayerClass import Monolayer
import numpy as np
from scipy.signal import argrelextrema
myPaths=[

"MemF1_B0530I2/DataRaw/MemF1_B0530I2",
"MemF1_B0530I2/DataRaw/MemF1_B0530I2dox",
"MemF1_B0530I/DataRaw/MemF1_B0530I",
"MemF1_B0530I/DataRaw/MemF1_B0530Idox",
"MemF1_B0531I/DataRaw/MemF1_B0531I",
"MemF1_B0531I/DataRaw/MemF1_B0531Idox",
"MemF1_B0531I2/DataRaw/MemF1_B0531I2",
"MemF1_B0531I2/DataRaw/MemF1_B0531I2dox",
"MemF1_B0602I/DataRaw/MemF1_B0602I",
"MemF1_B0602I/DataRaw/MemF1_B0602Idox",
"MemF1_B0602I2/DataRaw/MemF1_B0602I2",
"MemF1_B0602I2/DataRaw/MemF1_B0602I2dox",
"MemF1_B0603I2/DataRaw/MemF1_B0603I2dox",
"MemF1_B0603I/DataRaw/MemF1_B0603Itest",
"MemF1_B0629ID/DataRaw/MemF1_B0629IDdox",
"MemF1_0630ID/DataRaw/MemF1_0630IDtest",


]
filepath="Data/"

plt.ioff()
plotTime=plt.subplots()
plotTimeScaled=plt.subplots()
plotIsotherms=plt.subplots()
plotTimePerArea=plt.subplots()
plotTimePerAreaScaled=plt.subplots()

for path in myPaths:
    path="Data/"+path+".xlsx"
    myMonolayer=Monolayer(path)
    myLabel=' %s' %(myMonolayer.param["Name"])

    if "dox" in path or "test" in path:

        myMonolayer.data["T[min]"]=myMonolayer.data["T[s]"]/60.0
        myMonolayer.data["SP[mN/m]/Area[m^2]"]=myMonolayer.data["SP[mN/m]"]/(myMonolayer.data["Area[cm^2]"])

        print("Area %.5f m2" %(myMonolayer.data["Area[cm^2]"].values[3]/10000))
        myMonolayer.param_label["T[min]"]='Time [min]'
        myMonolayer.param_label["SP[mN/m]/Area[m^2]"]=u'$\pi$ [mN/m]/Area[$m^2$]'

        #get first point of inyections
        differences= myMonolayer.data.loc[myMonolayer.data["T[min]"]<8].diff()
        #indexInject=np.where(differences>differences[2]*5)[0][0]
        indexInject=differences.idxmax()["SP[mN/m]"]
        intervalFindMin=differences.loc[indexInject-50:indexInject]
        indexInject=differences.loc[indexInject-50:indexInject].idxmin()["SP[mN/m]"]
        localizationMin=argrelextrema(intervalFindMin["SP[mN/m]"].values, np.less)[0][0]
        myIndices=intervalFindMin.index
        indexInject=myIndices[localizationMin]

        plotTime=myMonolayer.PlotSimple(figure=plotTime,xparam="T[min]", yparam="SP[mN/m]",label=myLabel,markersize=3, cycles=False) # %(myMonolayer.param["Name"]))
        
        plotTimePerArea=myMonolayer.PlotSimple(figure=plotTimePerArea,xparam="T[min]", yparam="SP[mN/m]/Area[m^2]",label=myLabel,markersize=3, cycles=False) # %(myMonolayer.param["Name"]))
        plotTimePerArea[1].scatter(myMonolayer.data["T[min]"].loc[indexInject],myMonolayer.data["SP[mN/m]/Area[m^2]"].loc[indexInject], marker="*", s=50, c="red", zorder=100000000)
        #scale by that injection
        myMonolayerScaled=myMonolayer
        myMonolayerScaled.data["T[min]"]=myMonolayerScaled.data["T[min]"]-myMonolayerScaled.data["T[min]"].loc[indexInject]
        myMonolayerScaled.data["SP[mN/m]"]=myMonolayerScaled.data["SP[mN/m]"]-myMonolayerScaled.data["SP[mN/m]"].loc[indexInject]
        myMonolayerScaled.data["SP[mN/m]/Area[m^2]"]=myMonolayerScaled.data["SP[mN/m]/Area[m^2]"]-myMonolayerScaled.data["SP[mN/m]/Area[m^2]"].loc[indexInject]
        plotTimeScaled=myMonolayerScaled.PlotSimple(figure=plotTimeScaled,xparam="T[min]", yparam="SP[mN/m]",label=myLabel,markersize=3, cycles=False) # %(myMonolayer.param["Name"]))
        plotTimePerAreaScaled=myMonolayerScaled.PlotSimple(figure=plotTimePerAreaScaled,xparam="T[min]", yparam="SP[mN/m]/Area[m^2]",label=myLabel,markersize=3, cycles=False) # %(myMonolayer.param["Name"]))
        plotTimePerAreaScaled[1].scatter(myMonolayerScaled.data["T[min]"].loc[indexInject],myMonolayerScaled.data["SP[mN/m]/Area[m^2]"].loc[indexInject], marker="*", s=50, c="red", zorder=100000000)
    
    else:
        myMass=(myMonolayer.param["Volume1"]*1E-3*myMonolayer.param["Concentration1"])
        myMonolayer.data["AreaPerMass"]=myMonolayer.data["Area[cm^2]"]*1E2/myMass
        myMonolayer.param_label["AreaPerMass"]="$mm^2/mg$"
        plotIsotherms=myMonolayer.PlotSimple(figure=plotIsotherms, xparam="AreaPerMass",label=myLabel,markersize=3, cycles=False) # %(myMonolayer.param["Name"]))

    print(path)
plotTime[1].legend()
plotTimeScaled[1].legend()
plotTimePerArea[1].legend()
plotTimePerAreaScaled[1].legend()
plotIsotherms[1].legend()

plotTimeScaled[0].suptitle("Scaled")
plotTimePerAreaScaled[0].suptitle("Scaled")
plt.show()
input("Press to exit")