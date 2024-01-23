from monolayerClass import Monolayer
import numpy as np
import pandas as pd

filepath='Data/'
name="C-Sph_B0915N20_mean"
nameSave=name
firstFile="C-Sph_B0915N20/C-Sph_B0915N20_IMG"
secondFile="TFG/Chol-Sph-Curc-10_B2/Chol-Sph-Curc-10_B2_IMG"

a=Monolayer(filepath+"%s.xlsx" %(firstFile))
b=Monolayer(filepath+"%s.xlsx" %(secondFile))
a.RemoveBias("SP[mN/m]")
b.RemoveBias("SP[mN/m]")

x,y,dx,dy=a.getMean([a.data["Mma[A^2/molec]"],b.data["Mma[A^2/molec]"]],[a.data["SP[mN/m]"],b.data["SP[mN/m]"]],x_desphase="nearest")
speed=np.max(a.data["Bspd[mm/min]"].values)
a.data=pd.DataFrame({"Mma[A^2/molec]":x,"SP[mN/m]":y,"DMma[A^2/molec]":dx,"DSP[mN/m]":dy})
a.data["Bspd[mm/min]"]=speed
a.outDictCols={"Mma[A^2/molec]":"Mma[A^2/molec]","SP[mN/m]":"SP[mN/m]","DMma[A^2/molec]":"DMma[A^2/molec]","DSP[mN/m]":"DSP[mN/m]"}
a.param["Name"]=name
a.param.pop('HTML', None)
a.param.pop('IMG', None)
a.param["Data1"]=firstFile
a.param["Data2"]=secondFile

a.to_excel(filepath+nameSave+".xlsx")
