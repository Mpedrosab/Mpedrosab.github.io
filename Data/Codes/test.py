


import matplotlib.pyplot as plt
import pandas as pd
from monolayerClass import Monolayer

#data='Data/DPPC_B0428N25/BAMRAW/ValuesPixel.csv'
data='Data/Chol_B0414Y25/BAMRAW/ValuesSubtracFirst.csv'
    
myMonolayer=Monolayer("Data/Chol_B0414Y25/Chol_B0414Y25_IMG.xlsx")
#myMonolayer=Monolayer("Data/DPPC_B0428N25/DPPC_B0428N25_IMG.xlsx")
myMonolayer.RemoveBias()
data2=myMonolayer.data
data2=data2.dropna(subset=["BamFile"]) 


img=myMonolayer.PlotSimple(label='DPPC')
plt.figure()

x=pd.read_csv(data)
x["SP[mN/m]"]=data2["SP[mN/m]"].values 
x["Bamfile"]=data2["BamFile"].values
x["Mma[A^2/molec]"]=data2["Mma[A^2/molec]"].values
myColumns=[col for col in list(x.columns) if "Y" in col ]
for column in myColumns:
    plt.plot(x["SP[mN/m]"],x[column])


plt.title(data.split("/")[-1])
plt.xlabel('SP[mN/m]')
plt.ylabel('PixelValue')
plt.grid()

plt.figure()
for column in myColumns:
    print(column)
    plt.plot(x["Mma[A^2/molec]"],x[column])
plt.title(data.split("/")[-1])
plt.xlabel('Mma[A^2/molec]')
plt.ylabel('PixelValue')
plt.grid()
plt.show()