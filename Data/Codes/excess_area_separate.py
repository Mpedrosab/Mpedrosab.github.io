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
import pandas as pd
from pandas import read_excel
import numpy as np
from monolayerClass import Monolayer
from os import listdir
from scipy import signal
pi=3.14159265
N=6.022045*10**(23) #Avogadro ctant


filepath='Data/'
ideal=[ 
        "CholPC067_B0723/DataRaw/CholPC067_B0723.xlsx",
        #"C-PC067_B0729D20/DataRaw/C-PC067_B0729D20.xlsx",    #_pure2

        #"CholPCCur03B0727/DataRaw/CholPCCur03B0727.xlsx",
        "C-PCCur03B1004D/DataRaw/C-PCCur03B1004D.xlsx",
        "CholPCCur05B0727/DataRaw/CholPCCur05B0727.xlsx",
        "CholPCCur07B0727/DataRaw/CholPCCur07B0727.xlsx",
        #"Cur_B0917N20f/DataRaw/Cur_B0917N20f.xlsx",
        "TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",

        ]

'''
ideal=[                                                         #_2
        "CholPC067_B0723/DataRaw/CholPC067_B0723.xlsx",
        #"C-PC067_B0729D20/DataRaw/C-PC067_B0729D20.xlsx", #_pure2

        #"CholPCCur03B0727/DataRaw/CholPCCur03B0727.xlsx",
        "C-PCCur03B1004D/DataRaw/C-PCCur03B1004D.xlsx",
        "C-PCCur05B1005D/DataRaw/C-PCCur05B1005D.xlsx",
        
        "C-PCCur07B1005Df/DataRaw/C-PCCur07B1005Df.xlsx",
        "Cur_B0917N20f/DataRaw/Cur_B0917N20f.xlsx",
        #"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",
        ]
'''
'''
ideal=[         
        "TFG/Chol-Sph-Curc-00_B3/Chol-Sph-Curc-00_B3_IMG.xlsx",    #_pureTFG
         #"TFG/Chol-Sph-Curc-00_B2/Chol-Sph-Curc-00_B2_IMG.xlsx",      #_pureTFG          

        #"C-Sph_B0915N20/DataRaw/C-Sph_B0915N20.xlsx",
        "C-SphCur03B0922/DataRaw/C-SphCur03B0922.xlsx",
        "C-SphCur05B0922/DataRaw/C-SphCur05B0922.xlsx",
        "C-SphCur07B0923/DataRaw/C-SphCur07B0923.xlsx",
        "Cur_B0917N20f/DataRaw/Cur_B0917N20f.xlsx",
        #"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",

        ]
'''

#TFG

ideal=[ 
        #"CholPC067_B0723/DataRaw/CholPC067_B0723.xlsx",         #_Newpure
        "C-PC067_B0729D20/DataRaw/C-PC067_B0729D20.xlsx",    #_Newpure2

        #"TFG/Chol-DPPC-Curc-00_B1/Chol-DPPC-Curc-00_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-03_B1/Chol-DPPC-Curc-03_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-05_B1/Chol-DPPC-Curc-05_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",     
               
        # "TFG/Chol-DPPC-Curc-00_B2/Chol-DPPC-Curc-00_B2_IMG.xlsx",        
        # "TFG/Chol-DPPC-Curc-03_B2/Chol-DPPC-Curc-03_B2_IMG.xlsx",
        # "TFG/Chol-DPPC-Curc-05_B2/Chol-DPPC-Curc-05_B2_IMG.xlsx",
        # "TFG/Chol-DPPC-Curc-07_B2/Chol-DPPC-Curc-07_B2_IMG.xlsx",        
        # "TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",        

        
        ]   

'''
ideal=[ 
      
        "TFG/Chol-Sph-Curc-00_B2/Chol-Sph-Curc-00_B2_IMG.xlsx",               
        "TFG/Chol-Sph-Curc-03_B2/Chol-Sph-Curc-03_B2_IMG.xlsx",        
        "TFG/Chol-Sph-Curc-05_B2/Chol-Sph-Curc-05_B2_IMG.xlsx",        
        "TFG/Chol-Sph-Curc-07_B2/Chol-Sph-Curc-07_B2_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",

        # "TFG/Chol-Sph-Curc-00_B3/Chol-Sph-Curc-00_B3_IMG.xlsx",        
        # "TFG/Chol-Sph-Curc-03_B3/Chol-Sph-Curc-03_B3_IMG.xlsx",       
        # "TFG/Chol-Sph-Curc-05_B3/Chol-Sph-Curc-05_B3_IMG.xlsx",        
        # "TFG/Chol-Sph-Curc-07_B3/Chol-Sph-Curc-07_B3_IMG.xlsx",        
        # "TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",          

        
        ] 
'''
#articulo
ideal=[         
          
        "C-Sph_B0915N20/DataRaw/C-Sph_B0915N20.xlsx",
        "C-SphCur03B0922/DataRaw/C-SphCur03B0922.xlsx",
        "C-SphCur05B0922/DataRaw/C-SphCur05B0922.xlsx",
        "C-SphCur07B0923/DataRaw/C-SphCur07B0923.xlsx",
       "Mean/Chol-DPPC-Curc-10_mean_withFit.xlsx"
        ]
myLipid="TFG/Sph_fix_B3/Sph_fix_B3_IMG.xlsx"
myChol="Chol_B0913N20/Chol_B0913N20_IMG.xlsx"
x_chol=0.25

coletilla="_separate_Chol_B0913N20_Sph_fix_B3"
filesave=ideal[1].split("/")[-1].split(".")[0]


smooth=True

xSet=[]
ySet=[]

#
x_curc=np.array([0.0,0.3,0.5,0.7,1.0])
pressPoints=[5,15,30,40]


lipid_data=Monolayer(filepath+myLipid)
chol_data=Monolayer(filepath+myChol)
curc_data=Monolayer(filepath+ideal[4])
lipid_points={}
chol_points={}
curc_points={}

lipid_data.RemoveBias("SP[mN/m]")
lipid_data.RemoveCollapse("SP[mN/m]")
chol_data.RemoveBias("SP[mN/m]")
chol_data.RemoveCollapse("SP[mN/m]")
curc_data.RemoveBias("SP[mN/m]")
curc_data.RemoveCollapse("SP[mN/m]")



i=0
aexcess={}

for point in pressPoints:
    nearestLipid=lipid_data.find_nearest(lipid_data.data["SP[mN/m]"],point)
    lipid_points[point]=[nearestLipid[0],nearestLipid[1],lipid_data.data.iloc[nearestLipid[0]]["Mma[A^2/molec]"]]
    nearestChol=chol_data.find_nearest(chol_data.data["SP[mN/m]"],point)
    chol_points[point]=[nearestChol[0],nearestChol[1],chol_data.data.iloc[nearestChol[0]]["Mma[A^2/molec]"]]
    nearestCur=curc_data.find_nearest(curc_data.data["SP[mN/m]"],point)
    curc_points[point]=[nearestCur[0],nearestCur[1],curc_data.data.iloc[nearestCur[0]]["Mma[A^2/molec]"]]
    aexcess[point]=[]
#for prop in proportions:
figure=plt.subplots()
xSet=[]
ySet=[]

figComp,axComp=plt.subplots()
smooth_file=""
i=0
axComp.axhline(y=0,lw=2,ls="--",c="black")

for f in ideal:

    data=Monolayer(filepath+f)
    #figure=Monolayer.PlotSimple(data)
    data.RemoveBias("SP[mN/m]")
    #figure=Monolayer.PlotSimple(data,figure=figure)
    myLegend=f.split(".")[0].split("/")[-1].replace("_areafix","")
    #data.data=data.data.loc[data.data["SP[mN/m]"]<=30]

    figure=Monolayer.PlotSimple(data,figure=figure,label=myLegend)
    data.RemoveCollapse("SP[mN/m]")

    #Get data at certain points in pressure
    
    for point in pressPoints:
        nearest=data.find_nearest(data.data["SP[mN/m]"],point)
        aexcess[point].append(data.data.loc[nearest[0],"Mma[A^2/molec]"]-(1-x_curc[i])*(1-x_chol)*lipid_points[point][2]-(1-x_curc[i])*(x_chol)*chol_points[point][2]-x_curc[i]*curc_points[point][2])
            
    i+=1
for point in pressPoints:
    axComp.plot(x_curc,aexcess[point],'--')
    axComp.scatter(x_curc,aexcess[point], label=point)

figure[1].legend(prop={"size":7})
axComp.legend(prop={"size":7})
axComp.grid()
axComp.set_ylim(ymin=-15,ymax=10)
axComp.set_xticks(x_curc)
axComp.set_xticklabels(x_curc)

figure[0].savefig(filepath+"IMG/excessArea_"+filesave+"_isotherm"+coletilla+".png")

figComp.savefig(filepath+"IMG/excessArea_"+filesave+coletilla+".png")
#_pureTFG
    #plt.close()

'''
[xMean,yMean,dy_rubish]=Monolayer.getMean(xSet,ySet,x_desphase="interpolate")
#axComp.plot(xMean,yMean, "--")
mean=pd.DataFrame(list(zip(xMean, yMean)),columns=["xMean","yMean"])
mean.to_excel("Borrar_mean.xls")
'''

plt.show()
print("Finish")





