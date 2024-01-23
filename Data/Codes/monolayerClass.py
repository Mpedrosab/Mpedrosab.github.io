# -*- coding: utf-8 -*-
"""
Created on 05/04/21 at 15:13:02

@author: M. Pedrosa Bustos
"""

from calendar import firstweekday
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
#from matplotlib.axes import Axes
#from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
#from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from uncertainties import unumpy as unp
from uncertainties import ufloat
import datetime
#%%
#==============================================================================
# CLASS TO HANDLE MONOLAYER DATA
#==============================================================================


class Monolayer:
    def __init__(self, source,myPreamble=None):
        self.dictCols={'t[s]':'T[s]',	'Bpos':'Bpos[mm]',	'Bspd':'Bspd[mm/min]',	'A[cm²]':'Area[cm^2]',	'Mma[Å²]':'Mma[A^2/molec]',	'P1[mN/m]':'SP[mN/m]',	'P2[mN/m]':'SP2[mN/m]'}
        self.outDictCols=dict((y,x) for x,y in self.dictCols.items())

        if type(source) == str: #When the path to data is given
            
            self.path=source

            if ".xls" in source:   #read excel file      
                self.data=pd.read_excel(source)
                if 'Area[cm^2]' not in self.data.columns:
                    self.data=pd.read_excel(source,skiprows=43)
                    self.data=self.data.rename(columns=self.dictCols)
                    self.preamble=pd.read_excel(source,header=None).iloc[:43,0:2]
                    self.param={}
                    add=''
                    firstWidth="Through"
                    for index,myParam in self.preamble.iterrows():
                        if type(myParam[0])==float:    #Avoid nan
                            add=''
                            continue
                        if (myParam[0] not in self.param.keys()):
                            if "Width" in myParam[0]:
                                myParam[0]=myParam[0].replace("Width","Width"+firstWidth)
                                firstWidth="Substrate"
                            if " " in myParam[0]:
                                paramStr=myParam[0].split(" ")[:-1]
                                paramEnd=paramStr[0]
                                paramStr=paramStr[1:]
                                if len(paramStr)!=1:
                                    for p in paramStr:
                                        if p=="":
                                            break
                                        paramEnd=paramEnd+" "+p
                                if type(myParam[1])==str:
                                    self.param[paramEnd+add]=myParam[1].strip()
                                else:
                                    self.param[paramEnd+add]=myParam[1]
                            else:
                                paramEnd=myParam[0]
                                self.param[paramEnd]=myParam[1]  
                            if "1" in paramEnd:
                                add="1"
                            elif "2" in paramEnd:
                                add="2"
                    if ("Speed" not in self.param.keys()):
                        self.param["Speed"]=self.data['Bspd[mm/min]'].max()
                        self.param["Unit_Speed"]="mm/min"
                    self.param["Unit_Vol"]="ul"

                    #Remove back mivng from main data
                    #self.dataBack=self.data.loc[self.data["Bspd[mm/min]"]<0]
                    #self.data=self.data.loc[self.data["Bspd[mm/min]"]>=0]
                    #self.data=self.data.loc[self.data["Bspd[mm/min]"]>=0]

                    #change wrong date
                    if (isinstance(self.param["Date"], datetime.date) )==False:
                        self.param["Date"]=datetime.datetime.strptime(self.param["Date"], '%d/%m/%Y')


            self.dictLabels={          #Labels with the equial
                 "NameSmall":"$_{[\mathtt{%s}]}$"  %(self.param["Name"].replace("_","/")),
                 "Temperature":"T=%d $^oC$"  %(self.param["Temperature"]),
                   "Speed": "$%.0f %s" %(self.param["Speed"],self.param["Unit_Speed"]),
                   "SpeedEqual": "$v_{comp}=$" ,
                   "Substance1": self.param["Substance1"],
                   "Volume1": "%d $\mu$l" %(self.param["Volume1"]), 
                   "Concentration1": "%.2f %s" %(self.param["Concentration1"],self.param["Unit1"])
            }        
        else:                           #When data is given in a Pandas
            self.data=source
            self.preamble=myPreamble
            self.path=None
            self.param=None

        self.lenght=len(self.data)
        self.param_label={'T[s]':'Time [s]','Bpos[mm]':'Barrier position [mm]','Bspd[mm/min]':'Barrier speed [mm/min]','Area[cm^2]':'Area[$cm^2$]','Mma[A^2/molec]':u'Mma [$\AA^2$/molec]','SP[mN/m]':u'$\pi$ [mN/m]','SPMean':u'$\pi$ [mN/m]'}

        #Get unumpy for errors if proceede
        self.errors={}
        for col in self.data.columns:
            if col[0]=="D":              #Errors start by D
                self.To_Unumpy(col[1:])

    def RemoveCollapse(self,param='SP[mN/m]',range=None):
        '''
            Remove the collapse by finding the max or 
            by remove input from given pressure
        
        '''
        # slope = np.diff(self.data[param])/np.diff(self.data["Mma[A^2/molec]"])
        # index=np.argmin(slope)
        # plt.plot(self.data["Mma[A^2/molec]"][:-1],slope)
        # self.data=self.data.iloc[:index-5]
        if range==None:
            index=np.argmax(self.data[param])
            self.data=self.data.iloc[:index]
        else:
            #In case during collapse there is data that get lower than limit
            if param=="Mma[A^2/molec]":
                badRange=self.data.loc[self.data[param]<range]
            else:
                badRange=self.data.loc[self.data[param]>range]
            if len(badRange)!=0:
                maxTime=badRange.iloc[0]["Bpos[mm]"]
                self.data=self.data.loc[self.data["Bpos[mm]"]<maxTime]
        return self

    def RemoveBias(self,param='SP[mN/m]'):
        '''
            Removes the original bias of the isotherms
        '''
        self.data[param] = self.data[param]-self.data[param].iloc[0]
        return

    def PlotSimple(self,xparam='Mma[A^2/molec]',yparam='SP[mN/m]',error=False,cycles=False,**args):
        '''
            Plots simple isotherms
            If figure in args, get [fig,ax] to add to plot. Else create figure
            error: pl
        '''
        if("figure" not in args):
            figure=plt.subplots()
        else: 
            figure=args["figure"]
        if("style" not in args):
            style="-o"
        else: 
            style=args["style"]
        if("zorder" not in args):
            zorder=1
        else: 
            zorder=args["zorder"]
        myLabel=None 
        if "label" in args:
            myLabel=args["label"]
        
        if "markersize" in args:
            markersize=args["markersize"]
        else:
            markersize=5        

        if "FitAt[A^2/molec]" in list(self.param.keys()):
            limit=self.param["FitAt[A^2/molec]"]
            figure[1].plot(self.data.loc[self.data["Mma[A^2/molec]"]>limit,xparam],self.data.loc[self.data["Mma[A^2/molec]"]>limit,yparam],style,markersize=markersize, label=myLabel, zorder=zorder)

            myColor=figure[1].lines[-1]._color     

            figure[1].plot(self.data.loc[self.data["Mma[A^2/molec]"]<=limit,xparam],self.data.loc[self.data["Mma[A^2/molec]"]<=limit,yparam],"--",color=myColor, label=None, zorder=zorder)
        else:
            if cycles:
                myAlpha=1
                myDataNoFirst=self.data.iloc[1:].copy()
                mydataPlot=myDataNoFirst.loc[(myDataNoFirst['Bspd[mm/min]'].diff()!=0) & (myDataNoFirst['Bspd[mm/min]']!=0) & (~myDataNoFirst['Bspd[mm/min]'].diff().isna())]
                cycleNum=0
                indexPrev=0
                numCycles=len(mydataPlot)
                if numCycles==0:
                    print("NO CYCLES AT ALL!")
                    figure[1].plot(self.data[xparam],self.data[yparam],style, markersize=markersize, label=myLabel,zorder=zorder)
                else:    
                    print ("Number of speed changes: %d" % (numCycles))
                    for index,row in mydataPlot.iterrows():
                        if index<=1:
                            continue
                        dataNow=self.data.iloc[indexPrev+1:index]
                        if cycleNum==0:
                            figure[1].plot(dataNow[xparam],dataNow[yparam],style, markersize=markersize, label=myLabel, alpha=(1-cycleNum/numCycles),zorder=zorder)

                            myColor=figure[1].lines[-1]._color  

                        else:
                            figure[1].plot(dataNow[xparam],dataNow[yparam],"--", markersize=markersize, label=None,color=myColor, alpha=(1-(cycleNum-1)/numCycles),zorder=zorder)
                        cycleNum+=1
                        indexPrev=index
                    myColor=figure[1].lines[-1]._color
                    dataNow=self.data.iloc[indexPrev+1:]
                    if cycleNum==0:
                        cycleNum=1
                    figure[1].plot(dataNow[xparam],dataNow[yparam],"--", markersize=markersize, label=None,color=myColor, alpha=(1-(cycleNum-1)/numCycles),zorder=zorder)
            else:    
                figure[1].plot(self.data[xparam],self.data[yparam],style, markersize=markersize, label=myLabel,zorder=zorder)

            myColor=figure[1].lines[-1]._color     
        if error:
            #figure[1].errorbar(self.data[xparam],self.data[yparam],yerr=self.data['D'+yparam],xerr=self.data['D'+xparam],lw=3,zorder=1)
            # plt.errorbar(data[i][nom],data[i]['SP[mN/m]'],yerr=data[i]['DSP[mN/m]'],xerr=data[i]['D'+nom],fmt='none',elinewidth=3,color=colors[i],alpha=0.1,lw=3)
            figure[1].axes.fill_betweenx(self.data[yparam],self.data[xparam]-self.data['D'+xparam],self.data[xparam]+self.data['D'+xparam],facecolor=myColor,alpha=0.3,zorder=1)
            figure[1].axes.fill_between(self.data[xparam],self.data[yparam]-self.data['D'+yparam],self.data[yparam]+self.data['D'+yparam],facecolor=myColor,alpha=0.3,zorder=1)

           
        figure[1].set_xlabel(self.param_label[xparam])
        figure[1].set_ylabel(self.param_label[yparam])

        if "title" in args:
            figure[1].set_title(args["title"])
        #Check if grid is on
        if figure[1].xaxis._major_tick_kw['gridOn']==False:
            figure[1].grid()
        
        if "xLim" in args:
            figure[1].set_xlim(xmin=args["xLim"][0],xmax=args["xLim"][0])
        if "yLim" in args:
            figure[1].set_ylim(ymin=args["yLim"][0],ymax=args["yLim"][0])

        figure[1].legend()
        return figure

    def get_LimitArea(self,upperLimit,lowerLimit,xparam='Mma[A^2/molec]',param='SP[mN/m]',plot=False,figure=None):
        '''
        Fit a line to solid phase and return the fit and the limit area
        '''
        dataFit=self.data.loc[(self.data[param]<=upperLimit) & (self.data[param]>=lowerLimit) ]
        m, b = np.polyfit(dataFit[xparam], dataFit[param], 1)
        limitArea=(0-b)/m      #y=m*x+b => (y-b)/m=x

        #get xdata to return beautiful line
        #figure=None
        if plot:
            xMax,yMin=[(-5-b)/m,-5]
            xMin,yMax=[(self.data[param].max()-b)/m,self.data[param].max()]  
            xData=[xMin,limitArea,xMax]
            yData=[yMax,0,yMin]
            if figure==None:
                figure=plt.subplots()
            figure=self.PlotSimple(figure=figure) 
            figure[1].plot(xData,yData,"--",c="black",label="limit Area %.3f" %(limitArea))
            figure[1].plot(dataFit[xparam], dataFit[param],"-.",c="red",label=None)

        return limitArea,[m,b],figure
    #%%
    # =============================================================================
    #    CONVERT DATA TO UNUMPY
    # =============================================================================

    def To_Unumpy(self,param):
        '''
        Convert to unumpy array
        Input: dataframe with all the values
                Param: list of parameters to compute the unumpy array. Error keys must start with D
        Output: dict with the unumpy arrays
        '''
        self.errors[param]={param:unp.uarray(self.data[param],self.data["D"+param])}
        
        return
    #%%
    # =============================================================================
    #   FIND NEAREST VALUE IN ARRAY    
    # =============================================================================

    def pad(array, reference_shape, offsets):
        """
        array: Array or list to be padded
        reference_shape: tuple of size of ndarray to create
        offsets: list of offsets (number of elements must be equal to the dimension of the array)
        will throw a ValueError if offsets is too big and the reference_shape cannot handle the offsets
        """

        # Create an array of zeros with the reference shape
        result = np.zeros(reference_shape)
        # Create a list of slices from offset to offset + shape in each dimension
        insertHere = [slice(offsets[dim], offsets[dim] + array.shape[dim]) for dim in range(array.ndim)]
        # Insert the array in the result at the specified offsets
        result[insertHere] = array
        return result

    def find_nearest(self,array, value):
        '''
        Find nearest values in array
        '''

        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return [int(idx), array[idx]]
        
    def RemoveDuplicates(self,param):
        """
        Remove duplicates keeping last repeated vale
        NOTE: this can make the monolayer pressure not to be zero at fist value
        """
        self.data=self.data.drop_duplicates(subset=param,keep='last')    #Keep last recorded value

    def to_excel(self,pathSave):

        '''
            Save the monolayer to an excel file

        '''
  
        self.data.rename(columns=self.outDictCols).to_excel(pathSave, index=None,startrow=44)
        x=pd.read_excel(pathSave)

        parameters=pd.DataFrame.from_dict(self.param,orient="index").reset_index()
        PreambleLength=len(parameters)
        x.iloc[0:PreambleLength,0:2]=parameters
        x.to_excel(pathSave, index=None, header=None)


    def Interpolate(self,original_xList,original_yList, x_desphase):
        '''
        Interpolate y values to match x in both dataset
        Input: 
            x: list of x coordinates for all dataset
            y: list of y coord for all datasets
            x_desphase: 
                nearest: find nearest values of x ,and use their y values. Uses as reference the  x vector less dense
                interpolate: interpolate values between points
            error: compute the error of x
        All take as reference the isotherm with smaller max value

        NOTE: step in Mma is almost equal in all monolayers (0.13)
        '''

        #Convert elements of list to legible format
        #if type(xList[1]).__module__ != np.__name__     #It's not numpy type
        if len(original_xList)==1:
            print("Only one array to compute mean. Return same array")
            return original_xList,original_yList
        if isinstance(original_xList[1], pd.Series):
            for i in range(len(original_xList)):
                original_xList[i]=original_xList[i].values
                original_yList[i]=original_yList[i].values

        xList = copy.deepcopy(original_xList)
        yList = copy.deepcopy(original_yList)

        if x_desphase!=None:
            #elem_list=0
            #lastMin=1e20
            #indexMin=-1


            #REMOVE!!! Save for debug
            result2=pd.DataFrame()
            #Remove!!
            maxLength=0
            lengths=[len(x) for x in xList]
            maxLength=np.max(lengths)   #Save also max length of arrays to reshape them laterr
                

            denserList=0           #Stores denser x vector
            lightList=0           #Stores lighter x vector
            minDist=1e6
            maxDist=-1e6
            for elem in range(0,len(xList)):
                #Stores denser vector
                dist=np.mean(np.diff(xList[elem]))
                if dist>maxDist:
                    maxDist=dist
                    lightList=elem
                if dist<minDist:
                    minDist=dist
                    denserList=elem
                #REMOVE!!
                result2["x"+str(elem+1)]=Monolayer.pad(xList[elem],(maxLength,),[0])
                result2["y"+str(elem+1)]=Monolayer.pad(yList[elem],(maxLength,),[0])
        #Find nearest values in x space

        #Find lower max and higher min to avoid out of bonds
        maxAll=[]
        minAll=[]
        [maxAll.append(np.max(x)) for x in xList]  
        [minAll.append(np.min(x)) for x in xList]  
        xMinAll=np.max(minAll)
        xMaxAll=np.min(maxAll)

        if x_desphase=="nearest":
            #Not to go beyond smaller max or highest min
            yList[lightList]=yList[lightList][(xList[lightList]<xMaxAll) & (xList[lightList]>xMinAll)]
            xList[lightList]=xList[lightList][(xList[lightList]<xMaxAll) & (xList[lightList]>xMinAll)]

            #For nearest, take as reference the x vector less dense
            values_x=np.empty((len(xList[lightList]),len(xList)))
            values_y=np.empty((len(yList[lightList]),len(yList)))
            err_xAll=np.empty((len(yList[lightList]),len(yList)))
            elem_list=0
            for x in xList:
                if elem_list==lightList:
                    values_x[:,elem_list]=x
                    values_y[:,elem_list]=yList[elem_list]
                    err_xAll[:,elem_list]=0
                else:
                    ind=0
                    for value in xList[lightList]:
                        [index,val]=self.find_nearest(x, value)
                        values_x[ind,elem_list]=val
                        values_y[ind,elem_list]=yList[elem_list][index]
                        err_xAll[ind,elem_list]=np.abs(val-value)
                        ind+=1
                result2["x"+str(elem_list+1)+"_Nearest"]=Monolayer.pad(values_x[:,elem_list],(maxLength,),[0])
                result2["y"+str(elem_list+1)+"_Nearest"]=Monolayer.pad(values_y[:,elem_list],(maxLength,),[0])

                elem_list+=1  
            err_x=np.std(values_x,1)

        elif x_desphase=="interpolate":
            #For interpolation, take as reference the denser x vector


            yList[denserList]=yList[denserList][(xList[denserList]<xMaxAll) & (xList[denserList]>xMinAll)]
            xList[denserList]=xList[denserList][(xList[denserList]<xMaxAll) & (xList[denserList]>xMinAll)]
            
            #REMOVE!!
            elem_list=0
            for x in xList:

                result2["x"+str(elem_list+1)+"_Tresh"]=Monolayer.pad(xList[elem_list],(maxLength,),[0])
                result2["y"+str(elem_list+1)+"_Tresh"]=Monolayer.pad(yList[elem_list],(maxLength,),[0])
                elem_list+=1

            values_x=np.empty((len(xList[denserList]),len(xList)))
            values_y=np.empty((len(yList[denserList]),len(yList)))
            err_xAll=np.empty((len(yList[denserList]),len(yList)))
            from scipy.interpolate import interp1d
            elem_list=0
            for x in xList:
                if elem_list==denserList:
                    values_x[:,elem_list]=x
                    values_y[:,elem_list]=yList[elem_list]
                    err_xAll[:,elem_list]=0
                else:
                    ind=0
                    interpolation=interp1d(x, yList[elem_list], kind='cubic')

                    values_x[:,elem_list]=xList[denserList]
                    values_y[:,elem_list]=interpolation(xList[denserList])
                    err_xAll[:,elem_list]=np.abs(xList[denserList]-x)

                result2["x"+str(elem_list+1)+"_Interp"]=Monolayer.pad(values_x[:,elem_list],(maxLength,),[0])
                result2["y"+str(elem_list+1)+"_Interp"]=Monolayer.pad(values_y[:,elem_list],(maxLength,),[0])

                elem_list+=1
            err_x=np.std(values_x,1)

        else:
            raise Exception("x_desphase type not allowed. See documentation")
            return 

        ##REMOVE!!
        #result2.to_excel("Borrar_after.xls")
        return values_x,values_y,[err_x,err_xAll]

    def getMean(self, original_xList,original_yList, x_desphase=None):
        '''
        Compute mean value between data set
        Input: 
            x: list of x coordinates for all dataset
            y: list of y coord for all datasets
            x_desphase: 
                None: x coordinates are equal
                nearest: find nearest values of x and use their y values
                interpolate: interpolate values between points
            error: compute the error from computing mean

        NOTE: step in Mma is almost equal in all monolayers (0.13)
        '''
        if len(original_xList)==1:
            print("Only one array to compute mean. Return same array")
            return original_xList,original_yList,[0],[0]

        #Check if all x coordinates are the same or not
        if x_desphase==None:
            for i in range(len(original_xList)):
                for j in range(i,len(original_xList)):
                    comparison = original_xList[i]== original_xList[j]
                if comparison==False:
                    raise Exception("x data not equal. Choose x_desphase type.")

            values_x=[original_xList]
            values_y=[original_yList]
            err_x=np.zeros(len(original_yList))
        else:
            values_x,values_y,err_x = self.Interpolate(original_xList,original_yList,x_desphase)
            err_x=err_x[0]
        #Do mean of all coordinates
        if len(values_x)==1:                #In case they are single points
            x_result=values_x[0]      #All x values are suppose to be equal after interpolation
        else:
            x_result=values_x[:,0]      #All x values are suppose to be equal after interpolation
        y_result=np.mean(values_y,1)

        #Get error if err is true
        dy_result=np.std(values_y,1)            #Divided by N, not N-1      
        return x_result,y_result,err_x,dy_result



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


    def Graf_SP(self ,data,param,title,legen,legen_title,material,save,**arg):
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


    def Err_monolayer(self,v,conc,mw):
        
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
        
        
        self.data['DArea[cm^2]']=self.data['Area[cm^2]']*1/100.   #1%   
        
    #   compute the error for each Mma
        A2=unp.uarray(self.data['Area[cm^2]'],self.data['DArea[cm^2]'])
    #    mma=mw2*A2*(1e16)/(1.0*v2*1e-6*conc2*Na)
        #to avoid dec error prop
        Na2=Na*1e-23
        mma=mw2*A2/(1.0*v2*conc2*Na2)       #All units compesate with the others except for e-1. mw=g/mol, A=cm2, v=ul, conc=mg/ml, Na=molec/mol
        mma=mma*1e-1    
        self.data['DMma[A^2/molec]']=unp.std_devs(mma)           #get the error component using std_devs
        
        self.data['DSP[mN/m]']=4*0.001       # 4uN/m
        
    #J Store also V, conc and mw

        self.data['Vol[ul]']=np.nan
        self.data['Conc[mg/ml]']=np.nan
        self.data['Mw[g/mol]']=np.nan
        self.data['DVol[ul]']=np.nan
        self.data['DConc[mg/ml]']=np.nan
        self.data['DMw[g/mol]']=np.nan
        
        self.data['Vol[ul]'].loc[0]=unp.nominal_values(v2)
        self.data['DVol[ul]'].loc[0]=unp.std_devs(v2)
        self.data['Conc[mg/ml]'].loc[0]=unp.nominal_values(conc2)
        self.data['DConc[mg/ml]'].loc[0]=unp.std_devs(v2)
        self.data['Mw[g/mol]'].loc[0]=unp.nominal_values(mw2)
        self.data['DMw[g/mol]'].loc[0]=unp.std_devs(mw2)

        self.errors['Vol[ul]']=v2
        self.errors['Conc[mg/ml]']=conc2
        self.errors['Mw[g/mol]']=mw2
        
    #   To check if parameters where entered properly
    #   data['Mma_check']=unp.nominal_values(mma)


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

