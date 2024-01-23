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
from tikzplotlib import save as tikz_save

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
'''
ideal=[         
        "CholPC067_B0723/DataRaw/CholPC067_B0723.xlsx",         #_Newpure
        "TFG/Chol-DPPC-Curc-03_B1/Chol-DPPC-Curc-03_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-05_B1/Chol-DPPC-Curc-05_B1_IMG.xlsx",        
        #"TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1_IMG_MOD.xlsx",        
        #"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",     
	#"Mean/Chol-DPPC-Curc-10_mean_withFit.xlsx",
       # "Cur_B0512CiMore/DataRaw/Cur_B0512CiMore_NoCicles.xlsx"
        "Cur_B0509Ci/DataRaw/Cur_B0509Ci_NoCicles.xlsx"
        ]
'''
ideal=[         
        "CholPC067_B0723/DataRaw/CholPC067_B0723.xlsx",         #_Newpure
        "TFG/Chol-DPPC-Curc-03_B1/Chol-DPPC-Curc-03_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-05_B1/Chol-DPPC-Curc-05_B1_IMG.xlsx",        
        #"TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1_IMG_MOD.xlsx",        
        #"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",     
	#"Mean/Chol-DPPC-Curc-10_mean_withFit.xlsx"
        #"Cur_B0512CiMore/DataRaw/Cur_B0512CiMore_NoCicles.xlsx",
        "Cur_B0509Ci/DataRaw/Cur_B0509Ci_NoCicles.xlsx"
        ]



coletilla="_newCur2"

filesave="CholDPPC"


xSet=[]
ySet=[]

#
x_curc=np.array([0.0,0.3,0.5,0.7,1.0])
pressPoints=[5,15,30,40]


pure_data=Monolayer(filepath+ideal[0])
curc_data=Monolayer(filepath+ideal[4])
pure_points={}
curc_points={}

pure_data.RemoveBias("SP[mN/m]")
pure_data.RemoveCollapse("SP[mN/m]")
curc_data.RemoveBias("SP[mN/m]")
curc_data.RemoveCollapse("SP[mN/m]")



i=0
aexcess={}

for point in pressPoints:
    nearestPure=pure_data.find_nearest(pure_data.data["SP[mN/m]"],point)
    pure_points[point]=[nearestPure[0],nearestPure[1],pure_data.data.loc[nearestPure[0],"Mma[A^2/molec]"]]
    nearestCur=curc_data.find_nearest(curc_data.data["SP[mN/m]"],point)
    curc_points[point]=[nearestCur[0],nearestCur[1],curc_data.data.loc[nearestCur[0],"Mma[A^2/molec]"]]
    aexcess[point]=[]
#for prop in proportions:
figure=plt.subplots()
figureLabel=plt.subplots()
xSet=[]
ySet=[]

figComp,axComp=plt.subplots()
i=0


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
        aexcess[point].append(data.data.loc[nearest[0],"Mma[A^2/molec]"]-(1-x_curc[i])*pure_points[point][2]-x_curc[i]*curc_points[point][2])
            
    i+=1

for point in pressPoints:
    axComp.plot(x_curc,aexcess[point],'--')
    axComp.scatter(x_curc,aexcess[point], label=None)

    figureLabel[1].scatter(0,0,label='%.d' %(point))
figureLabel[1].legend(title='$\pi$[mN/m]',loc=0,ncol=4)
#figureLabel[1].tight_layout()
figureLabel[0].savefig(filepath+"IMG/excessArea_"+filesave+"_legend"+coletilla+".png")
tikz_save(filepath+"IMG/excessArea_"+filesave+"_legend"+coletilla+".tikz",figureLabel[0],axis_width = '\\figwidth',encoding ='utf-8') 

figure[1].legend(prop={"size":7})
#axComp.legend(prop={"size":7})
axComp.grid()
axComp.set_ylim(ymin=-15,ymax=10)
axComp.set_xticks(x_curc)
axComp.set_xticklabels(x_curc)
axComp.set_xlabel('$\chi_{cur}$')
axComp.set_ylabel('$A_{exc}$ [$\AA^2$/molec]')
figure[0].savefig(filepath+"IMG/excessArea_"+filesave+"_isotherm"+coletilla+".png")

figComp.savefig(filepath+"IMG/excessArea_"+filesave+coletilla+".png")
tikz_save(filepath+"IMG/excessArea_"+filesave+coletilla+".tikz",figComp,axis_width = '\\figwidth',encoding ='utf-8') 

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





