# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 06:15:43 2020

@author: M. Pedrosa Bustos
"""

#==============================================================================
# Compute excess area

#NOTE: At low SP, there are duplicate values of SP that interfere when computing mean.
#       Remove them by computing mean
#==============================================================================

import matplotlib.pyplot as plt
from monolayerClass import Monolayer
import numpy as np
import pandas as pd
from scipy import signal
from tikzplotlib import save as tikz_save



filepath='Data/'

#Puras y modelos
ideal=[ 
        "C-Sph_B0915N20/DataRaw/C-Sph_B0915N20.xlsx",
        "C-SphCur03B0922/DataRaw/C-SphCur03B0922.xlsx",
        "C-SphCur05B0922/DataRaw/C-SphCur05B0922.xlsx",
        "C-SphCur07B0923/C-SphCur07B0923_IMG_MOD.xlsx",
        #"Cur_B0917N20f/DataRaw/Cur_B0917N20f.xlsx",
        #"Mean/Chol-DPPC-Curc-10_mean_withFit.xlsx"
        #"Cur_B0512CiMore/DataRaw/Cur_B0512CiMore_NoCicles.xlsx",
        "Cur_B0509Ci/DataRaw/Cur_B0509Ci_NoCicles.xlsx"
]
myCollapse=[32.7,26.9,17.03,10,-3]
#myCollapse=[-3]*5
allLegends=["0.0","0.3","0.5", "0.7", "1.0" ]
#allLegends=[x.split("/")[-1].split(".")[0] for x in ideal]

coletilla="_newCur2_smooth2"
legendLabel="Chol:%s \n    $\chi_{Cur}$" %("Sph")
filesave="borrar"


smooth=True

xSet=[]
ySet=[]

#

figure=plt.subplots()
xSet=[]
ySet=[]
figComp,axComp=plt.subplots()
comprAt30=[]

smooth_file=""
i=0


for f in ideal:

    #if "Chol-Sph-Curc-10" not in f and "Chol-Sph-025" not in f:
    #if "Chol-Sph-Curc-10" not in f and "Chol-DPPC-Curc-10" not in f:
    #if "Chol-DPPC-Curc-" not in f:
    #    continue
    data=Monolayer(filepath+f)
    #figure=Monolayer.PlotSimple(data)
    data.RemoveBias("SP[mN/m]")
    #figure=Monolayer.PlotSimple(data,figure=figure)
    #myLegend=f.split(".")[0].split("/")[-1].replace("_areafix","")
    myLegend=allLegends[i]
 
    data.RemoveCollapse("Mma[A^2/molec]",myCollapse[i])

    
    if "Cur_B0509Ci" in f:
        myX=data.data["Mma[A^2/molec]"].iloc[:-1]
        data.data["SP[mN/m]"]=signal.savgol_filter(data.data["SP[mN/m]"], 53, 2)
        data.data["Mma[A^2/molec]"]=myX
        

    if "Chol_" in f:
      
        figure=data.PlotSimple(figure=figure,label=myLegend,markersize=3,zorder=10)
        data.RemoveCollapse("SP[mN/m]")

    else:
        figure=data.PlotSimple(figure=figure,label=myLegend,markersize=3,zorder=1)

    #upperLimit=float(input("Upper limit: "))
    #lowerLimit=float(input("Lower limit: "))

    #area,fit=data.get_LimitArea(upperLimit[i],lowerLimit[i],plot=True,figure=figureArea)
    #areaAll.append(area)
   
    #Get Compress modulus
    #mma1= (data["Mma[A^2/molec]"].iloc[1:]+data["Mma[A^2/molec]"].iloc[:-1])*0.5
    

    result= data.data["Mma[A^2/molec]"].iloc[:-1]
    result=result.to_frame()

    mma2 = (data.data["Mma[A^2/molec]"].iloc[1:]+data.data["Mma[A^2/molec]"].iloc[:-1])*0.5
    result["C1"]= np.diff(data.data["Mma[A^2/molec]"])/np.diff(data.data["SP[mN/m]"])*1./result["Mma[A^2/molec]"]   #Same as inverting first
    result["C1"]=-1./result["C1"]
    x_check=result["C1"].copy()
        #Remove inf and nan data
    badSmooth=result.index[np.isinf(result["C1"])]
    for index in badSmooth[1:-1]:
        result["C1"].iloc[index]=(result["C1"].iloc[index-1]+result["C1"].iloc[index+1])/2.
    x=result["C1"].copy()

        #Check if bad data in smooth and replace it
    if smooth:
        if "Cur_B0509Ci" in f:
            #result["C1"]=signal.savgol_filter(result["C1"], 63, 2)
            result["C1"]=signal.savgol_filter(result["C1"], 53, 2)
        else:
            result["C1"]=signal.savgol_filter(result["C1"], 53, 2)
        smooth_file="_smooth"
        badSmooth=result.index[np.isinf(result["C1"])]
        result["C1"].iloc[badSmooth]=x.iloc[badSmooth]
    result["SP[mN/m]"]=data.data["SP[mN/m]"].iloc[:-1]

    if "FitAt[A^2/molec]" in list(data.param.keys()):
        limit=data.param["FitAt[A^2/molec]"]
        limitSP=data.data.loc[round(data.data["Mma[A^2/molec]"],4)==limit,"SP[mN/m]"].values[0]
        result1=result.loc[result["SP[mN/m]"]<limitSP]
        result2=result.loc[result["SP[mN/m]"]>=limitSP]
        axComp.plot(result1["SP[mN/m]"],result1["C1"],"-o",markersize=3,label=myLegend)
        myColor=axComp.lines[-1]._color     

        #axComp.plot(result2["SP[mN/m]"],result2["C1"],"--",label=None,color=myColor)

    else:
        axComp.plot(result["SP[mN/m]"],result["C1"],"-o",markersize=3,label=myLegend)
    
    #Remove duplicates for the mean (at low SP). Sotres the one with minimum Mma (latwer measured in isotherm). Be careful with collapse!!
    #result=result.groupby(["SP[mN/m]"]).mean()
    result=result.drop_duplicates(subset=["SP[mN/m]"],keep='last')
    xSet.append(result["SP[mN/m]"])
    ySet.append(result["C1"])

    #Get module at 30 mN/m
    [index30,data30]=data.find_nearest(result["SP[mN/m]"],30)
    comprAt30.append(result["C1"].iloc[index30])

    i+=1


figure[1].legend(title=legendLabel)
#figure[1].legend()     #for pures
figure[1].set_xlim(xmin=-2,xmax=82)
figure[1].set_ylim(ymin=-2,ymax=62)

axComp.legend(loc=2,title=legendLabel)
#axComp.legend()        #for pures
axComp.grid()
axComp.set_ylabel("$C^{-1} [mN/m]$")
axComp.set_xlabel(data.param_label["SP[mN/m]"])
axComp.set_ylim(ymin=-20, ymax=192)
axComp.set_xlim(xmax=62)
#figureArea[1].legend(prop={"size":7})
figure[0].savefig(filepath+"IMG/CompressMod_"+filesave+"_isotherm%s.png" %(coletilla))
tikz_save(filepath+"IMG/CompressMod_"+filesave+"_isotherm%s.tikz" %(coletilla),figure[0],axis_width = '\\figwidth',encoding ='utf-8') 

figComp.savefig(filepath+"IMG/CompressMod_"+filesave+"%s%s.png" %(smooth_file,coletilla))
tikz_save(filepath+"IMG/CompressMod_"+filesave+"%s%s.tikz" %(smooth_file,coletilla),figComp,axis_width = '\\figwidth',encoding ='utf-8') 

    #plt.close()

'''
[xMean,yMean,dy_rubish]=Monolayer.getMean(xSet,ySet,x_desphase="interpolate")
#axComp.plot(xMean,yMean, "--")
mean=pd.DataFrame(list(zip(xMean, yMean)),columns=["xMean","yMean"])
mean.to_excel("Borrar_mean.xls")
'''
print("Values at 30mN/m")
print(comprAt30)

plt.show()
input("done")




