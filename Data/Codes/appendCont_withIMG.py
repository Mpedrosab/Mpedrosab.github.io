# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:13:02 2017

@author: M. Pedrosa Bustos
"""
from BAMImgClass import BAMImg
from monolayerClass import Monolayer
import matplotlib.pyplot as plt

'''
    Append cont and main file to same file. 
    Append also IMG data and create HTML

'''



#x=BAMImg.CreateIndexHTML(pathAll)
#f=open("borrar.txt","w")
#f.write(x)
#f.close()

pathMain= "Data/Chol_B0414XH/DataRaw/DPPC_B0420Y20_main"
pathCont= "Data/Chol_B0414XH/DataRaw/DPPC_B0420Y20_cont"
pathOut=  "Data/Chol_B0414XH/DPPC_B0420Y20"

dataMain=Monolayer(pathMain+".xlsx")
dataMainIMG=BAMImg.AppendAbs(pathMain+".sql",dataMain,None)
dataCont=Monolayer(pathCont+".xlsx")
dataContIMG=BAMImg.AppendAbs(pathCont+".sql",dataCont,None)

#Append all
dataMainIMG.data=dataMainIMG.data.append(dataContIMG.data,ignore_index=True)

#Also create HTML
dataMainIMG.RemoveBias()

pathImg=pathOut+".png"
myLabel="[%s]=%.2f %s (%d $\mu$l)\n" %(dataMainIMG.param["Substance1"],dataMainIMG.param["Concentration1"],dataMainIMG.param["Unit1"],dataMainIMG.param["Volume1"])
myLabel+="T=%d $^oC$; $v_{comp}$=%.0f mm/min" %(dataMainIMG.param["Temperature"],dataMainIMG.data['Bspd[mm/min]'].max())
img=dataMainIMG.PlotSimple(label=myLabel)
img[0].savefig(pathImg)
pathHTML=BAMImg.SaveTableHTML(dataMainIMG,pathImg)
dataMainIMG.param["HTML"]=pathHTML
dataMainIMG.param["IMG"]=pathImg
dataMainIMG.to_excel(pathOut+"_IMG.xlsx")

plt.close()
