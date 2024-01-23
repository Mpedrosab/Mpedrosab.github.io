import matplotlib.pyplot as plt
from monolayerClass import Monolayer
import numpy as np
import pandas as pd
from scipy.stats import linregress

filepath='Data/'
file="Cur_B0509Ci/DataRaw/Cur_B0509Ci_NoCicles.xlsx"

askForLimits=False
thresh_fit=[19.9,60]  #SP[mN/m]

data=Monolayer(filepath+file)

myLength=len(data.data)
slope=np.empty(myLength)
intercept=np.empty(myLength)
r_value=np.empty(myLength)
p_value=np.empty(myLength)
std_err=np.empty(myLength)
y={}
x={}
area={}
x0=np.arange(1,5,0.3)  #with these points is enough for plotting the fit



#PLot to get data to fit
data.RemoveBias()
plt.ion()
figure=data.PlotSimple(markersize=3,zorder=10)

if askForLimits:
    thresh_fit=[float(input("Min SP for fit"))]
    thresh_fit.append(float(input("Max SP for fit")))

datafit=data.data.copy()
datafit=datafit[datafit['SP[mN/m]']>thresh_fit[0]]
datafit=datafit[datafit['SP[mN/m]']<thresh_fit[1]]

slope, intercept, r_value, p_value, std_err = linregress(datafit['Mma[A^2/molec]'],datafit['SP[mN/m]'])

#Get the line
x=x0*datafit.tail(n=1)['Mma[A^2/molec]'].iloc[0]
y=slope*x+intercept
#Get the area from fit. Get the interseccion with zero (y=0 => x=-intercept/slope)
area=-intercept/slope


figure[1].plot(x,y,label='Mma[$\AA^2$]=%.2f' %(area))
data.data=datafit.copy()
figure=data.PlotSimple(figure=figure, markersize=3,zorder=10)
filenameLabel=file.split("/")[-1].split(".")[0] 
figure[1].text(100,20,filenameLabel+'\nMma=%.2f $\AA^2$' %(area))

plt.show()
input("Finish")