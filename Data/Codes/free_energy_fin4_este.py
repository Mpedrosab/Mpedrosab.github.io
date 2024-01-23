# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:37:51 2018

@author: M. Pedrosa Bustos
"""

#==============================================================================
# COMPUTE FREE ENERGY. LO MISMO Q EN MATLAB!!
#==============================================================================

import matplotlib.pyplot as plt
from scipy.integrate import simps
from pandas import read_excel
import numpy as np
import functions
from uncertainties import unumpy as unp
from uncertainties import ufloat

pi=3.14159265
N=6.022045*10**(23) #Avogadro ctant


###############################################
#Parameters
savename='DPPC_new'
titleplot='Chol/DPPC/Cur'

#Set the same lim for the y axis
limy=[-2500,1000]
limx=[-0.03,1.03]

################################################
  
#%%
'''
# Read data   
data0=read_excel('../Datos/Buffer/Chol-Sph-Curc_B1/Chol-DPPC-Curc-10_B1/Chol-DPPC-Curc-10_B1.xls')
data1=read_excel('../Datos/Buffer/Chol-DPPC-Curc_B1/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1.xls')
data2=read_excel('../Datos/Buffer/Chol-DPPC-Curc_B1/Chol-DPPC-Curc-05_B1/Chol-DPPC-Curc-05_B1.xls')
data3=read_excel('../Datos/Buffer/Chol-DPPC-Curc_B1/Chol-DPPC-Curc-03_B1/Chol-DPPC-Curc-03_B1.xls')
data4=read_excel('../Datos/Buffer/Chol-DPPC-Curc_B1/Chol-DPPC-Curc-00_B1/Chol-DPPC-Curc-00_B1.xls')
#data5=read_excel('../Datos/Buffer/Chol-DPPC-067_B4/Chol-DPPC-067_B4.xls')
#data={0:data0,1:data1,2:data2,3:data3,4:data4}
'''
  

names={}
names2={}
data0={}
filepath='D:/Documentos_D/Universidad/Beca colaboracion/Datos/Report_final/Chol-DPPC-Cur/'

names[0]='Chol-DPPC-Curc-00_B2_witherr_mean_2'
names[1]='Chol-DPPC-Curc-03_B2_witherr_mean_2'
names[2]='Chol-DPPC-Curc-05_B2_witherr_mean_2'
names[3]='Chol-DPPC-Curc-07_B2_witherr_mean_2'
names[4]='Chol-DPPC-Curc-10_B2_witherr_mean_2'
fin=True
fit=read_excel('D:/Documentos_D/Universidad/Beca colaboracion/Datos/Datos/Review_article/All_curc/Cur_only_fit.xls')

#Para final
for i in range(0,len(names),1):
    names2[i]=names[i].replace("_bien","")
    names2[i]=names2[i].replace("_areafix","")
    names2[i]=names2[i].replace("(Shp)","")
    names2[i]=names2[i].replace("_witherr","")
    names2[i]=names2[i].replace("_2","")
    if fin==True:
        data0[i]=read_excel(filepath+names[i]+'.xls')
    else:
        data0[i]=pd.read_excel(filepath+names2[i]+'/'+names[i]+'.xls')
    
#x_curc=np.array([1.0,0.7,0.5,0.3,0.0])
    
x_curc=np.array([0.0,0.3,0.5,0.7,1.0])
#x_cholk=0.67
sp_end=40
sp_ini=5


G_each=unp.uarray(np.zeros(5),np.zeros(5))
G_exc=unp.uarray(np.zeros(5),np.zeros(5))


for i in range(0,5):
#Select range data from 0 to given SP

    data0[i]=data0[i].loc[data0[i]["SP[mN/m]"] > sp_ini]    #Changes very little if we add the negative value. From 0.3% to 3% error
    data0[i]=data0[i].loc[data0[i]["SP[mN/m]"] < sp_end]
    
#Convert to numpy
data=functions.To_Unumpy(data0)

#Convert to proper units
for i in range(0,5):
#    data[i]=data1[i]["Mma[A^2/molec]"]*(10**(-10))**2.0
#    data[i]=data1[i]["SP[mN/m]"]*(10**(-3))


#Convert to numpy array to avoid problems
#    dataarr
#Perform the integrals separately because otherwise the x and y axis do not coincide in the different excel files
#Do only the integrate(N*A*dSP) and later multiply by molar frac and N
    
    G_each[i]=np.trapz(data[i]["Mma[A^2/molec]"],data[i]["SPMean"])   #Así lo mismo q en Matlab
#With this I get i=0 -> A3, i=4 -> A12, i=[1,3] -> A123 for each concentration

#   G_exc[i]=N*(G_each[i]-(1-x_curc[i])*G_each[0]-x_curc[i]*G_each[4])
#Con todo    

    G_curc=np.trapz(x_curc[i]*data[4]["Mma[A^2/molec]"],data[4]["SP[mN/m]"])
    G_cell=np.trapz((1-x_curc[i])*data[0]["Mma[A^2/molec]"],data[0]["SP[mN/m]"])
    G_each2=np.trapz(data[i]["Mma[A^2/molec]"],data[i]["SP[mN/m]"])
    G_exc[i]=N*(G_each2-G_curc-G_cell)

G_exc=G_exc*1e-3*1e-20      #Appropiate units
#%% PLOT
my_dpi=100
params = {'mathtext.rm' : "Palatino Linotype",
          'font.family' : "Palatino Linotype",
          'mathtext.fontset' : 'cm',
          'font.size' :             27,
          'xtick.labelsize' :       27,
          'ytick.labelsize' :       27,
          'lines.linewidth' :       2,
          'lines.markersize' :      6,
          'figure.figsize' :        (800/my_dpi, 800/my_dpi)   # width, height in pixel
          }
plt.rcParams.update(params) 
    

lw_err=1.5
elw_err=1

print(savename)
print(G_exc)


G_exc[0]=ufloat(unp.nominal_values(G_exc[0]),unp.std_devs(G_exc[0])*5e17)
G_exc[4]=ufloat(unp.nominal_values(G_exc[4]),unp.std_devs(G_exc[4])*1e18)
G_exc_plot=unp.nominal_values(G_exc)
#G_exc_plot_err=np.array([9.19304327e+02, 7.57817585e+02, 5.86406434e+02, 3.06543043e+02,1.19304327e+02])/.40
G_exc_plot_err=unp.std_devs(G_exc)
#G_exc_plot_err=np.array([1.19304327e+02, 3.57817585e+02, 2.86406434e+02, 1.06543043e+02,1.19304327e+02])/.40
plt.figure('Free_ener')
plt.hlines(0,-1,2,linestyles='dashed',color='gray',zorder=1)
plt.plot(x_curc,G_exc_plot,'--',color='b')
plt.errorbar(x_curc,G_exc_plot,yerr=G_exc_plot_err,fmt='none',color='b',alpha=1,lw=lw_err)
plt.scatter(x_curc,G_exc_plot,facecolor='blue', edgecolor='blue',label='$A_{id}$')

print(G_exc_plot_err)

plt.xlabel('$\chi_{cur}$')
plt.ylabel('$\Delta$$G_{exc}$ [J/mol]')
plt.xlim(limx)
plt.ylim(limy)
plt.xticks(x_curc,x_curc)
plt.grid(ls='--')
plt.legend([],title=titleplot,loc=4)
plt.tight_layout()

#plt.errorbar(x_curc,G_exc_plot,yerr=unp.std_devs(aid_Sph),fmt='none',color='b',alpha=1,lw=lw_err)

plt.savefig('../Pictures/Plots/Report_final/'+savename+'_gibbsener.pdf')
plt.savefig('../Pictures/Plots/Report_final/'+savename+'_gibbsener')

np.save(filepath+'G_excs',G_exc)
    
#%%
'''
#Function computes free energy
def free_ener(xmolar,area,press):
    integral=N*simps(area*xmolar,press)
    return integral
#    G=N*(a123-(1-x_c)*a12-x_c*a3)
'''    
'''
# Total monolayer for each concentration
    Gtot[i-1]=free_ener(1.0,data[i]["Mma[A^2/molec]"],data[i]["SP[mN/m]"])
#Free energy monolayer without curc
    Gmonol[i-1]=free_ener(1.0-x_curc[i],data[4]["Mma[A^2/molec]"],data[4]["SP[mN/m]"])
#Free energy curc
    Gcurc
'''
#%%
'''
# Test
x=np.linspace(0,pi,50)
y=np.sin(x)
print "Test: ",free_ener(1.0,y,x)/N    #Must be 2 

'''

    
    