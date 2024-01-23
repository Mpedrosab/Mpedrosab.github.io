# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:13:02 2017

@author: M. Pedrosa Bustos
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from matplotlib.axes import Axes
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

#%%
#==============================================================================
# PLOT MONOLAYER DATA
# 
# Arguments Graf_SP:
# Add limits to the graph =>    xlim_ax=[xmin,xmax] and ylim_ax=[ymin,ymax]
# Frequency of xticks => frecx=[num]
# Frequency of yticks => frecy=[num]
# With erros => err=True
# If do not want to add arguments do not pass them or pass []
#==============================================================================


def Graf_SP(data,param,title,legen,legen_title,material,save,**arg):
#
#    param_label={'T[s]':'Time [s]','Bpos[mm]':'Barrier position [mm]','Bspd[mm/min]':'Barrier speed [mm/min]','Area[cm^2]':'Area[$cm^2$]','Mma[A^2/molec]':u'Mean Molecular Area [$\AA^2$/molec]','SP[mN/m]':'Surface pressure [mN/m]'}
    param_label={'T[s]':'Time [s]','Bpos[mm]':'Barrier position [mm]','Bspd[mm/min]':'Barrier speed [mm/min]','Area[cm^2]':'Area[$cm^2$]','Mma[A^2/molec]':u'Mma [$\AA^2$/molec]','SP[mN/m]':u'$\pi$ [mN/m]'}
    param_dis={'T[s]':'T','Bpos[mm]':'Bpos','Bspd[mm/min]':'Bspd','Area[cm^2]':'A','Mma[A^2/molec]':'Mma','SP[mN/m]':'SP'}    
    for nom in param:
  
     
        plt.figure(material+'_'+param_dis[nom])
            
        if title!=None: 
            plt.title(title)
        
        plt.grid(ls='--')

        plt.xlabel(param_label[nom])
        plt.ylabel('$\pi$ [mN/m]')
        
        if (('xlim_ax' in arg) and (arg['xlim_ax']!=[])):
            plt.xlim(arg['xlim_ax'][0],arg['xlim_ax'][1])
        if (('ylim_ax' in arg) and (arg['ylim_ax']!=[])):

            plt.ylim(arg['ylim_ax'][0],arg['ylim_ax'][1])
            
#   Default colors for erros            
        prop_cycle = plt.rcParams['axes.prop_cycle']
        colors = prop_cycle.by_key()['color']   
        for i in range(0,len(data),1):       
            plt.plot(data[i][nom],data[i]['SP[mN/m]'],label=legen[i],zorder=11)
            plt.scatter(data[i][nom],data[i]['SP[mN/m]'],label=None,zorder=12)
#       Plot errors
            if(('err' in arg) and arg['err']==True):
                for i in range(0,len(data),1):       
                   # plt.errorbar(data[i][nom],data[i]['SP[mN/m]'],yerr=data[i]['DSP[mN/m]'],xerr=data[i]['D'+nom],fmt='none',elinewidth=3,color=colors[i],alpha=0.1,lw=3)
                    plt.fill_betweenx(data[i]['SP[mN/m]'],data[i][nom]-data[i]['D'+nom],data[i][nom]+data[i]['D'+nom],facecolor=colors[i],alpha=0.15,zorder=10)
                    try:
                        plt.fill_between(data[i][nom],data[i]['SP[mN/m]']-data[i]['DSPMean'],data[i]['SP[mN/m]']+data[i]['DSPMean'],facecolor=colors[i],alpha=0.15,zorder=10)
                    except:
                        plt.fill_between(data[i][nom],data[i]['SP[mN/m]']-data[i]['DSP[mN/m]'],data[i]['SP[mN/m]']+data[i]['DSP[mN/m]'],facecolor=colors[i],alpha=0.15,zorder=10)

#                   y ERROR IS NOT SHOWN
#   yerror very small, doesn't appreciate
        if legen_title!=None:
           leg= plt.legend(title=legen_title)
           if ('legendmarksize' in arg):
                
                llines = leg.get_lines()
                plt.setp(llines, linewidth=arg['legendmarksize'])
#                leg.set_linewidth=arg['legendmarksize']
#                _originalFn = Axes.legend
#                Axes.legend=leg
        if (('frecx' in arg) and (arg['frecx']!=[])):
            ax = plt.gca()
            ax.locator_params(axis='x',tight=True, nbins=arg['frecx'][0])
        if (('frecy' in arg) and (arg['frecy']!=[])):
            ax = plt.gca()
            ax.locator_params(axis='y',tight=True, nbins=arg['frecy'][0])
            
            
        plt.tight_layout()


        if('err' in arg):
            plt.savefig('../Pictures/Plots/'+save+'_'+'_'+param_dis[nom]+'.pdf')
        else:
            plt.savefig('../Pictures/Plots/'+save+'_'+'_'+param_dis[nom]+'.eps')
        plt.savefig('../Pictures/Plots/'+save+'_'+'_'+param_dis[nom])

'''
def Graf_deriv(data,param,title,legen,legen_title,material,save):
    param_label={'T[s]':'Time [s]','Bpos[mm]':'Barrier position [mm]','Bspd[mm/min]':'Barrier speed [mm/min]','Area[cm^2]':'Area[$cm^2$]','Mma[A^2/molec]':'Mean molecular Area [$\AA^2$/molec]','SP[mN/m]':'Surface pressure [mN/m]'}
    param_dis={'T[s]':'T','Bpos[mm]':'Bpos','Bspd[mm/min]':'Bspd','Area[cm^2]':'A','Mma[A^2/molec]':'Mma','SP[mN/m]':'SP'}    
    
    for nom in param:
        
        
        plt.figure(material+'_'+param_dis[nom]+'_deriv',figsize=(20,30))
        if title!=None: 
            plt.title(title)
        plt.grid(ls='--')

        plt.xlabel(param_label[nom])
        plt.ylabel('dSP/d'+param_dis[nom])
#        plt.ylim(-1,1)
#        plt.xlim(50,120)

    
        for i in range(0,len(data),1):
            dev=np.gradient(data[i]['SP[mN/m]'],data[i][nom])

            plt.plot(data[i][nom],dev,label=legen[i])
    
        plt.legend(title=legen_title)
        
        plt.savefig('../Pictures/Plots/'+save+'_'+'_'+param_dis[nom]+'_deriv.eps')
        plt.savefig('../Pictures/Plots/'+save+'_'+'_'+param_dis[nom]+'_deriv')
'''

#%%
def Graf_deriv(data,param,title,legen,legen_title,material,save):
    param_label={'T[s]':'Time [s]','Bpos[mm]':'Barrier position [mm]','Bspd[mm/min]':'Barrier speed [mm/min]','Area[cm^2]':'Area[$cm^2$]','Mma[A^2/molec]':'Mean molecular Area [$\AA^2$/molec]','SP[mN/m]':'Surface pressure [mN/m]'}
    param_dis={'T[s]':'T','Bpos[mm]':'Bpos','Bspd[mm/min]':'Bspd','Area[cm^2]':'A','Mma[A^2/molec]':'Mma','SP[mN/m]':'SP'}    
    
    for nom in param:
        
        
        fig,ax=plt.subplots(figsize=(20,30))
        if title!=None: 
            ax.set_title(title)
        ax.grid(ls='--')

        ax.set_xlabel(param_label[nom])
        ax.set_ylabel('dSP/d'+param_dis[nom])
        plt.ylim(-5,2)
#        plt.xlim(50,120)

# Zoom a part of the data
        '''
        axins = zoomed_inset_axes(ax, 2, loc=6)
        axins.set_xlim(60, 100)
        axins.set_ylim(-0.5, 0.5)
        axins.grid(ls='--')

        mark_inset(ax, axins, loc1=3, loc2=4, fc="none", ec="0.5")
        '''    
        for i in range(0,len(data),1):
            dev=np.gradient(data[i]['SP[mN/m]'],data[i][nom])

            ax.plot(data[i][nom],dev,label=legen[i])
#            axins.plot(data[i][nom],dev)
        ax.legend(title=legen_title)
        
        fig.savefig('../Pictures/Plots/'+save+'_'+'_'+param_dis[nom]+'_deriv.eps')
        fig.savefig('../Pictures/Plots/'+save+'_'+'_'+param_dis[nom]+'_deriv')


#%%
# =============================================================================
# ERRORS IN PLOTS
# Inputs: the data frame, deposited volume with error, concentration with error, molecular mass with  error
# Enter V in ul and conc in mg/ml
# Output: the erros are stored in the data dataframe and a dict with SP and Mma unumpy
# =============================================================================
#import numpy as np
#import pandas as pd
from uncertainties import unumpy as unp
from uncertainties import ufloat

'''
v=50
mw=734
conc=0.5
data[0]=read_excel('../Datos/Buffer/DPPC_B1/DPPC_B1.xls')
'''


def Err_monolayer(data,v,conc,mw):
    
    '''
    Function for computing the errors for each isotherm. 
    Inputs: 
        data: isotherm data. Theo output is also stored in this variable
        v: volume delivered at the interface. <=25 assumes it uses 25ul syringe. >25 for 50ul and 100ul syringe.
        conc: solution concentration
        mw: molecular weight of the substance
        
    Output:
        Data with the errors. It is stored in the input data variable
        
    '''
        
    Na=6.022045e23
    
#   ERRORS OF EACH VARIABLE
    #v_err depends on syringe. In ul
    if (v<=25): 
        v_err=0.5    
    elif (v>25): #for 50ul and 100ul syringe
        v_err=1
          
    v2=unp.uarray(v,v_err)    
    conc2=unp.uarray(conc,0.017)    #No higher than 0.015 mg/ml. Error conc later
    mw2=unp.uarray(mw,0.01)
    
    
    data['DArea[cm^2]']=data['Area[cm^2]']*1/100.   #1%   
    
#   compute the error for each Mma
    A2=unp.uarray(data['Area[cm^2]'],data['DArea[cm^2]'])
#    mma=mw2*A2*(1e16)/(1.0*v2*1e-6*conc2*Na)
    #to avoid dec error prop
    Na2=Na*1e-23
    mma=mw2*A2/(1.0*v2*conc2*Na2)       #All units compesate with the others except for e-1. mw=g/mol, A=cm2, v=ul, conc=mg/ml, Na=molec/mol
    mma=mma*1e-1    
    data['DMma[A^2/molec]']=unp.std_devs(mma)           #get the error component using std_devs
    
    data['DSP[mN/m]']=4*0.001       # 4uN/m
    
#J Store also V, conc and mw

    data['Vol[ul]']=np.nan
    data['Conc[mg/ml]']=np.nan
    data['Mw[g/mol]']=np.nan
    data['DVol[ul]']=np.nan
    data['DConc[mg/ml]']=np.nan
    data['DMw[g/mol]']=np.nan
    
    data['Vol[ul]'].loc[0]=unp.nominal_values(v2)
    data['DVol[ul]'].loc[0]=unp.std_devs(v2)
    data['Conc[mg/ml]'].loc[0]=unp.nominal_values(conc2)
    data['DConc[mg/ml]'].loc[0]=unp.std_devs(v2)
    data['Mw[g/mol]'].loc[0]=unp.nominal_values(mw2)
    data['DMw[g/mol]'].loc[0]=unp.std_devs(mw2)
    
#   To check if parameters where entered properly
    data['Mma_check']=unp.nominal_values(mma)


#   All already stored in data[] => do not need to return anything

 
'''    
#CHECK VALUES Mma (THEY ARE OK!!)    
    out={'Mma':mma}
    return out
'''
'''
# Concentration error check
    
masa=unp.uarray(10.99,0.01)  #mg
vconc=unp.uarray(5,0.025) #ml

conc=masa/vconc
vsyr=unp.uarray(0.5,0.01)   #ml
concmix=3*vsyr*conc/vconc
'''

#%%
#==============================================================================
# FIX AREA THROUGH
#==============================================================================
import pandas as pd

def Fix_Area(data0):
    #Data throughs
    width_mini=75   #mm
    area_mini=24300    #mm^2
    l_mini=area_mini/width_mini      #total lenght of the through
    
    width_maria=75   #mm
    area_maria=23775    #mm^2
    l_maria=area_maria/width_maria      #total lenght of the through
    
    data2=data0.copy(deep=True)
    space_betw_bar_bad=l_mini-2*data2['Bpos[mm]']
    
    #data['Area1[cm^2]']=(space_betw_bar_bad-(l_mini-l_maria))*0.01
    
    data2['Area[cm^2]']=0.01*(width_maria*((data0['Area[cm^2]']*100./(width_mini))-(l_mini-l_maria)))     #*100 to convert cm2 to mm2. 0.01 to convert back to cm2. /(width_mini) to get the wrong longitude for each area. -(l_mini-l_maria) to get the real longitude
    data2['Mma[A^2/molec]']=data2['Area[cm^2]']/(data0['Area[cm^2]']/data0['Mma[A^2/molec]'])           # gives the number of molecules
    return data2


#%%
# =============================================================================
#    CONVERT DATA TO UNUMPY
# =============================================================================
'''
def To_Unumpy2(data0):
    out=[]
    for i in range(0,len(data0),1):
        out[0]=unp.uarray(data0[i]['Mma[A^2/molec]'],data0[i]['DMma[A^2/molec]']),'SP':unp.uarray(data0[i]['SP[mN/m]'],data0[i]['DSPMean'])}
        out[1]==unp.uarray(data0['Mma[A^2/molec]'],data0['DMma[A^2/molec]'])
#       out[i]['SP[A^2/molec]']=unp.uarray(data0['SP[mN/m]'],data0['DSP[mN/m]'])
    return out
'''
def To_Unumpy(data0):
    out={}
    for i in range(0,len(data0),1):
        out[i]={'Mma[A^2/molec]':unp.uarray(data0[i]['Mma[A^2/molec]'],data0[i]['DMma[A^2/molec]']),'SP[mN/m]':unp.uarray(data0[i]['SP[mN/m]'],data0[i]['DSP[mN/m]']),'SPMean':unp.uarray(data0[i]['SPMean'],data0[i]['DSPMean'])}
#       out[i]['Mma[A^2/molec]']=unp.uarray(data0['Mma[A^2/molec]'],data0['DMma[A^2/molec]'])
#       out[i]['SP[A^2/molec]']=unp.uarray(data0['SP[mN/m]'],data0['DSP[mN/m]'])
    return out
#%%
# =============================================================================
#   FIND NEAREST VALUE IN ARRAY    
# =============================================================================

import numpy as np

def find_nearest(array, value):
    '''
    Find nearest values in array
    '''

    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return [int(idx), array[idx]]

def getMean(xList,yList, x_desphase=None):
    '''
    Compute mean value between data set
    Input: 
        x: list of x coordinates for all dataset
        y: list of y coord for all datasets
        x_desphase: 
            None: x coordinates are equal
            nearest: find nearest values of x and use their y values
            interpolate: interpolate values between points
    All take as reference the isotherm with smaller max value
    '''

    #Convert elements of list to legible format
    #if type(xList[1]).__module__ != np.__name__     #It's not numpy type
    if isinstance(xList[1], pd.Series):
        for i in range(len(yList)):
            xList[i]=xList[i].values
            yList[i]=yList[i].values

    if x_desphase!=None:
        elem_list=0
        lastMin=1e20
        indexMin=-1
        for y in yList:

            #Get dataset with minimum max pressure  to use as reference
            myMin=np.max(y)
            if lastMin>=myMin:
                lastMin=myMin
                indexMin=elem_list
            elem_list+=1
    print(indexMin)
    #Find nearest values in x space
    values_x=np.empty((len(xList[indexMin]),len(xList)))
    values_y=np.empty((len(yList[indexMin]),len(yList)))

    if x_desphase=="nearest":
        elem_list=0
        for x in xList:
            if elem_list==indexMin:
                values_x[:,elem_list]=x
                values_y[:,elem_list]=yList[elem_list]
            else:
                ind=0
                for value in xList[indexMin]:
                    [index,val]=find_nearest(x, value)
                    values_x[ind,elem_list]=val
                    values_y[ind,elem_list]=yList[elem_list][index]
                    ind+=1
            elem_list+=1  
            

    elif x_desphase=="interpolate":
        from scipy.interpolate import interp1d
        elem_list=0
        for x in xList:
            if elem_list==indexMin:
                values_x[:,elem_list]=x
                values_y[:,elem_list]=yList[elem_list]
            else:
                ind=0
                interpolation=interp1d(x, yList[elem_list], kind='cubic')

                values_x[:,elem_list]=xList[indexMin]
                values_y[:,elem_list]=interpolation(xList[indexMin])


    elif x_desphase==None:
        #Check if all x coordinates are the same or not
        comparison = an_array == another_array
        if ~comparison.all():
            raise Exception("x data not equal. Choose x_desphase type.")
            return
    else:
        raise Exception("x_desphase type not allowed. See documentation")
        return 

    #Do mean of all coordinates
    x_result=np.mean(values_x,1)
    y_result=np.mean(values_y,1)

    result2=pd.DataFrame(values_x)
    result2["y1"]=values_y[:,0]
    result2["y2"]=values_y[:,1]
    result2["y3"]=values_y[:,2]
    result2.to_excel("Borrar2.xls")
    return [x_result,y_result]

#%%
#############################################
##   TESTS
############################################
'''
import pandas as pd
from pandas import read_excel

#data1=read_excel('Datos/Report_final/Chol-Sph-Cur/Chol-Sph-Curc-00_B2_witherr_mean_2.xls')
#data2=read_excel('Datos/Report_final/Chol-Sph-Cur/Chol-Sph-Curc-05_B2_witherr_mean_2.xls')
#data3=read_excel('Datos/Report_final/Chol-Sph-Cur/Chol-Sph-Curc-07_B2_witherr_mean_2.xls')


data1=read_excel('Datos/Sph1/Sph1_molecfix.xls')
data2=read_excel('Datos/Sph2/Sph2.xls')
data3=read_excel('Datos/Sph3/Sph3.xls')
result=getMean([data1["Mma[A^2/molec]"],data2["Mma[A^2/molec]"],data3["Mma[A^2/molec]"]], \
    [data1["SP[mN/m]"],data2["SP[mN/m]"],data3["SP[mN/m]"]], x_desphase="interpolate")
result2=pd.DataFrame(np.array(result).T)
result2["data1_x"]=data1["Mma[A^2/molec]"]
result2["data2_x"]=data2["Mma[A^2/molec]"]
result2["data3_x"]=data3["Mma[A^2/molec]"]
result2["data1_y"]=data1["SP[mN/m]"]
result2["data2_y"]=data2["SP[mN/m]"]
result2["data3_y"]=data3["SP[mN/m]"]
result2.to_excel("Borrar.xls")
'''