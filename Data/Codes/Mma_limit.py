
import matplotlib.pyplot as plt
from monolayerClass import Monolayer
import numpy as np
import pandas as pd
from scipy.stats import linregress

filepath='Data/'
#file="Cur_B0509Ci/DataRaw/Cur_B0509Ci_NoCicles.xlsx"
#file="Cur_B0512Ci/DataRaw/Cur_B0512Ci.xlsx"
files=[
	"Cur_B0509Ci/DataRaw/Cur_B0509Ci_NoCicles.xlsx",
	"Cur_B0512Ci/DataRaw/Cur_B0512Ci_NoCicles.xlsx",
	"Cur_B0512CiMore/DataRaw/Cur_B0512CiMore_NoCicles.xlsx"
	]

askForLimits=False
thresh_fits=[
	[10,30],  #SP[mN/m]0
	[10,30],  #SP[mN/m]0
	[10,30],  #SP[mN/m]0
]

i=0
figure=plt.subplots()
myLegend=[]
for file in files:
	thresh_fit=thresh_fits[i]

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


#PLot to get data to 
	if askForLimits:
		data.RemoveBias()
		plt.ion()
		figure2=data.PlotSimple(markersize=3,zorder=10)

		thresh_fit=[float(input("Min SP for fit"))]
		thresh_fit.append(float(input("Max SP for fit")))


	limitArea,[m,b],figure=data.get_LimitArea(thresh_fit[1],thresh_fit[0],xparam='Mma[A^2/molec]',param='SP[mN/m]',plot=True,figure=None)
	myLegend.append(file.split("/")[-1].split(".")[0])
	myLegend.append(u"$A_0$: %.3f $\AA^2$/molec" %(limitArea))
	figure[0].legend([file.split("/")[-1].split(".")[0]+"\n"+u"$A_0$: %.3f $\AA^2$/molec" %(limitArea)])
	i+=1
#figure[0].legend(myLegend)
plt.show()
input("Finish")