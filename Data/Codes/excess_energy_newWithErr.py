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
coletilla="_newPure2"
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
#Articulo
ideal=[         
        "CholPC067_B0723/DataRaw/CholPC067_B0723.xlsx",         #_Newpure
        "TFG/Chol-DPPC-Curc-03_B1/Chol-DPPC-Curc-03_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-05_B1/Chol-DPPC-Curc-05_B1_IMG.xlsx",        
        #"TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1_IMG.xlsx",        
        "TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1_IMG_MOD.xlsx",        
        #"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG.xlsx",     
	"Mean/Chol-DPPC-Curc-10_mean_withFit.xlsx"
        ]
coletilla="_Fit"

filesave="borrar"


smooth=True

xSet=[]
ySet=[]

#
x_curc=np.array([0.0,0.3,0.5,0.7,1.0])
pure_data=Monolayer(filepath+ideal[0])
curc_data=Monolayer(filepath+ideal[4])

pure_data.RemoveBias("SP[mN/m]")
pure_data.RemoveCollapse("SP[mN/m]")
curc_data.RemoveBias("SP[mN/m]")
curc_data.RemoveCollapse("SP[mN/m]")
curc_data.data=curc_data.data.loc[curc_data.data["SP[mN/m]"]<=30]
pure_data.data=pure_data.data.loc[pure_data.data["SP[mN/m]"]<=30]

#for prop in proportions:
figure=plt.subplots()
xSet=[]
ySet=[]
G_each=np.zeros(5)
G_exc=np.zeros(5)
figComp,axComp=plt.subplots()
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
    myLegend=f.split(".")[0].split("/")[-1].replace("_areafix","")
    #data.data=data.data.loc[data.data["SP[mN/m]"]<=30]

    figure=Monolayer.PlotSimple(data,figure=figure,label=myLegend)
    data.RemoveCollapse("SP[mN/m]")
    data.data=data.data.loc[data.data["SP[mN/m]"]<=30]


    G_each[i]=np.trapz(data.data["Mma[A^2/molec]"],data.data["SP[mN/m]"])   #Así lo mismo q en Matlab
#With this I get i=0 -> A3, i=4 -> A12, i=[1,3] -> A123 for each concentration

#   G_exc[i]=N*(G_each[i]-(1-x_curc[i])*G_each[0]-x_curc[i]*G_each[4])
#Con todo    

    G_curc=np.trapz(x_curc[i]*curc_data.data["Mma[A^2/molec]"],curc_data.data["SP[mN/m]"])
    G_cell=np.trapz((1-x_curc[i])*pure_data.data["Mma[A^2/molec]"],pure_data.data["SP[mN/m]"])
    G_each2=np.trapz(data.data["Mma[A^2/molec]"],data.data["SP[mN/m]"])
    G_exc[i]=N*(G_each2-G_curc-G_cell)

    i+=1
G_exc=G_exc*1e-3*1e-20

axComp.plot(x_curc,G_exc,'--',color='b')
axComp.scatter(x_curc,G_exc,facecolor='blue', edgecolor='blue',label='$A_{id}$')

figure[1].legend(prop={"size":7})
#axComp.legend(prop={"size":7})
axComp.set_xlabel('$\chi_{cur}$')
axComp.set_ylabel('$\Delta$$G_{exc}$ [J/mol]')
axComp.grid()
axComp.set_ylim(ymin=-1500,ymax=1500)
figure[0].savefig(filepath+"IMG/FreeEnergy_"+filesave+"_isotherm"+coletilla+".png")

figComp.savefig(filepath+"IMG/FreeEnergy_"+filesave+coletilla+".png")

    #plt.close()

'''
[xMean,yMean,dy_rubish]=Monolayer.getMean(xSet,ySet,x_desphase="interpolate")
#axComp.plot(xMean,yMean, "--")
mean=pd.DataFrame(list(zip(xMean, yMean)),columns=["xMean","yMean"])
mean.to_excel("Borrar_mean.xls")
'''

plt.show()
print("Finish")





