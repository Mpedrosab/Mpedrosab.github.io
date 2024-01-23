import pandas as pd
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import pickle
import copy


def FitCurve(x, a, b, c):
	return a * x + b

def interpolateXval(x1,x2,y1,y2,yGet):
    p=np.polyfit([x1,x2], [y1,y2], 1)
    m = p[0]  # Gradient
    c = p[1]  # y-intercept
    return (yGet-c)/m
    
def find_nearest(array, value):
    '''
    Find nearest values in array
    '''

    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return [int(idx), array[idx]]
        

def Interpolate(original_xList,original_yList, x_desphase):
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
                    [index,val]=find_nearest(x, value)
                    values_x[ind,elem_list]=val
                    values_y[ind,elem_list]=yList[elem_list][index]
                    err_xAll[ind,elem_list]=np.abs(val-value)
                    ind+=1
            elem_list+=1  
        err_x=np.std(values_x,1)

    elif x_desphase=="interpolate":
        #For interpolation, take as reference the denser x vector


        yList[denserList]=yList[denserList][(xList[denserList]<xMaxAll) & (xList[denserList]>xMinAll)]
        xList[denserList]=xList[denserList][(xList[denserList]<xMaxAll) & (xList[denserList]>xMinAll)]
        
        #REMOVE!!
        elem_list=0
        for x in xList:

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


            elem_list+=1
        err_x=np.std(values_x,1)

    else:
        raise Exception("x_desphase type not allowed. See documentation")
        return 

    ##REMOVE!!
    #result2.to_excel("Borrar_after.xls")
    return values_x,values_y,[err_x,err_xAll]

def getMean(original_xList,original_yList, x_desphase=None):
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
        values_x,values_y,err_x = Interpolate(original_xList,original_yList,x_desphase)
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


def getSI(xUnit):
    myUnits={
        "nN":10**(-9),
        "nm":10**(-9),
        "um":10**(-6)
    }
    return myUnits[xUnit]

def getNanoEntreMicro(xUnit,yUnit,invert=False):
    myUnits={
        "nN":10**(-9),
        "nm":10**(-9),
        "um":10**(-6)
    }
    if (invert==True):

        return myUnits[xUnit]/myUnits[yUnit]
    else:
        return myUnits[yUnit]/myUnits[xUnit]


def readFile(filepath):
    myFile=open(filepath,'r')

    #Data start after 	"um	nN" line. Check which line is it
    i=0
    alreadyData=False
    for data in myFile.readlines():
        if alreadyData==True:
            if "micrometer" in data:
                units=data.replace("micrometer","um").replace("nanonewton","nN").replace("\n","").split("\t")[1:3]
            else:
                units=data.replace("\n","").split("\t")[1:3]
            break
        if "Height" in data and "Force" in data:
            alreadyData=True
            #need to read units in next loop
            
        
        i+=1

    if alreadyData==False:
        print("PROBLEM IN FINDING DATA!!")
        return None,None
    headerForce="Force_[%s]" %(units[1])
    headerHeihg="ZHeight_[%s]" %(units[0])
    data = pd.read_csv(filepath, sep="\s+",skiprows=i, names=["row",headerHeihg, headerForce], header=0)
       

    return data,units,[headerHeihg,headerForce]


#START HEREEE

pathAll=[
"M1/Zona1/",
"M1/Zona2/",
"M2/Zona3/PinPoint/",
"M3/Zona1/",
"M4/Zona1/",
"M5/Zona1/",
]
now=5
#path="/home/mariapb/GoogleDrive_UGR2/Data_analysis/AFM/Nanos/Fuerza/PropNanomecanicas/20_10_2022/M3/Zona1/"
#path="D:/Documentos_D/Google_Drive_UGR/Data_analysis/AFM/Nanos/Fuerza/Aprender/"
#path="../../../Documentos_D/Google_Drive_UGR/Data_analysis/AFM/Nanos/Fuerza/Aprender/Ej_Articulo/"
path="../../../Documentos_D/Google_Drive_UGR/Data_analysis/AFM/Nanos/Fuerza/PropNanomecanicas/20_10_2022/"+pathAll[now]
getMeanAll=False   #get the mean plot of all curves

fitTreshAll=[
[17.49,87.44],          #M1/Zona1/            
[17.49,87.45],          #M1/Zona2/
[19.01,95.06],          #M2/Zona3/PinPoint/
[16.95,84.77],          #M3/Zona1/
[15.22,76.09],          #M4/Zona1/
[21.43,107.13]           #M5/Zona1/,

]
 #to set data to fit for modulus
fitTresh=fitTreshAll[now]

stiffThreshold=fitTresh[0]
#fitTresh=[[14.48,74.48],
#[17.41,84.53],
#[17.12,85.5]
#
#]

#allFiles=[f for f in listdir(path) if "txt" in f and "fig1" in f]    #para aprender
allFiles=[f for f in listdir(path) if "txt" in f and "inicial" not in f] 
#myCols=["file","Stiffness_Resta[nN]","Stiffness_Calc_[N/m]","Stiffness_Slope_[N/m]","EModulus_Up_[Pa] (Approach)","EModulus_Down_[Pa] (Detach)","EModulus_Mean_[Pa]","Adhesion_[nN]","xUpSlope"]
myColsAll=["file",
"Stiffness_Resta_MaxForce[nN]","Stiffness_Resta_UpSetpoint[nN]","STIFFNESS_CALC_MAXForce_[N/m]",
"STIFFNESS_CALC_UpSetpoint_[N/m]","STIFFNESS_SLOPE_[N/m]","EModulus_Approach_[Pa*m]",
"EMODULUS_RETRACT_[Pa*m]","EModulus_Approach_Hertz_[Pa]","EMODULUS_RETRACT_HERTZ_[Pa]",
"EMODULUS_approach_Ok_[Pa]","EModulus_Mean_[Pa*m]","ADHESION_[nN]",
"hertz_cte","xUpSlope","xMax","xThreshold"
]
myCols=[myColsAll[0]]
myCols.append(myColsAll[1])
myCols.append(myColsAll[2])
myCols.append(myColsAll[5])
myCols.append(myColsAll[7])
myCols.append(myColsAll[9])
myCols.append(myColsAll[10])
myCols.append(myColsAll[12])
dataModulus=pd.DataFrame(columns=myCols)
dataModulusAll=pd.DataFrame(columns=myColsAll)
totalXvalUp=[]
totalXvalDown=[]
totalYvalUp=[]
totalYvalDown=[]
figGen, axGen = plt.subplots(nrows=1, ncols=1)
plt.rcParams['image.cmap']="tab20"
plt.ioff()
#plt.ion()
stiffThresholdOrig=stiffThreshold
fitTreshoOrig=fitTresh
i=0
for file in allFiles:
    fig, ax = plt.subplots(nrows=1, ncols=1)

    myData,units,[headerHeihg,headerForce]=readFile(path+file)
    #stiffThreshold=fitTreshoOrig[i][0]
    #fitTresh=fitTreshoOrig[i]
    i+=1
    #CHANGE UNITS
    #units[0]="um"
    #myData[headerHeihg]=myData[headerHeihg]*getSI(units[0])
   # myData[headerForce]=myData[headerHeihg]*getSI(units[1])
   # stiffThreshold=stiffThresholdOrig*getSI(units[1])
    #fitTresh[0]=fitTreshoOrig[0]*getSI(units[1])
    #fitTresh[1]=fitTreshoOrig[1]*getSI(units[1])

    print(file)
    #Separate going up and down
    #max
    myMax=myData[headerForce].idxmax()
    myMaxVal=myData[headerForce].max()
    myMaxValX=myData[headerHeihg].iloc[myMax]

    dataApproach=myData.iloc[:myMax]
    dataRetract=myData.iloc[myMax:]

    minUp=dataApproach[headerForce].idxmin()
    dataForStar=dataApproach.iloc[minUp:]
    xStart= dataForStar[headerHeihg].iloc[(dataForStar[headerForce]-0).abs().argsort()[:1]].item()
    #myData[headerHeihg]=myData[headerHeihg]-xStart
    #dataApproach=myData.iloc[:myMax]
    #dataRetract=myData.iloc[myMax:]
    
        #individual plot
    ax.plot(dataApproach[headerHeihg],dataApproach[headerForce], "o-", c="green",label=file.replace(".txt",""))
    ax.plot(dataRetract[headerHeihg],dataRetract[headerForce], "+-",c="red",label="_no label_")


    ax.legend()
    ax.set_xlabel(myData.columns[1])
    ax.set_ylabel(myData.columns[2])
    ax.grid()
    nameFile=path+file.replace(".txt","").replace(" ","_")+"FD_Plot"
    fig.savefig(nameFile+".png")
    #pickle.dump(fig, open(nameFile+".pickel", 'wb'))


    #Get data parameterss
    #elastic modulus = slope in the approach region
    fitUp=dataApproach.loc[(dataApproach[headerForce]>=fitTresh[0]) & (dataApproach[headerForce]<=fitTresh[1])]
    fitDown=dataRetract.loc[(dataRetract[headerForce]>=fitTresh[0]) & (dataRetract[headerForce]<=fitTresh[1])]
    pUp=np.polyfit(fitUp[headerHeihg], fitUp[headerForce], 1)
    eModApproach = pUp[0]  # Gradient
    cUp = pUp[1]  # y-intercept
    pDown=np.polyfit(fitDown[headerHeihg], fitDown[headerForce], 1)
    eModRetract = pDown[0]  # Gradient
    cDown = pDown[1]  # y-intercept

    #Apply Hertz model
    alfa=40*np.pi/180.0
    v=0.5
    k= 5 #N/m
    r=8*10**(-9)/(getSI(units[0]))
    k=k/(getSI(units[1])/getSI(units[0]))
    x=dataApproach[headerForce]/k
    #delta=dataApproach[headerHeihg]-xStart+x
    #delta=dataApproach[headerHeihg]-x
    delta=dataApproach[headerHeihg]+x
    #delta=-(-1*(dataApproach[headerHeihg]-xStart)-x)
    #delta=np.abs(delta)
    #delta=1
    fitUp=dataApproach.loc[(dataApproach[headerForce]>=fitTresh[0]) & (dataApproach[headerForce]<=fitTresh[1])]
    xFit=delta.loc[(dataApproach[headerForce]>=fitTresh[0]) & (dataApproach[headerForce]<=fitTresh[1])]
    
    #FROM SQRT
    xFit=np.sqrt(xFit**3)
    deltaPlot=np.sqrt(delta**3)
    deltaForcePlot=dataApproach[headerForce]
    fitUp=fitUp

    #TO SQUARE
    #fitUp=fitUp**2
    #deltaForcePlot=dataApproach[headerForce]**2
    #deltaPlot=delta**3
    #xFit=xFit**3

    fitHerzt=np.polyfit(xFit, fitUp[headerForce], 1)
    eHertzNoConv = fitHerzt[0]  # Gradient

    #TO SQUARE
    #eHertzNoConv=np.sqrt(np.abs(eHertzNoConv))

    eHertz=eHertzNoConv*(3.0/4.0)*(1.0-v*v)/np.sqrt(r)
    delta2=1
    a=(2*np.tan(alfa)*delta2/np.pi)*1/(1.0-v*v)
    eModApproach2=eModApproach/a
    eModRetract2=eModRetract/a

    figMod,axMod=plt.subplots(nrows=1, ncols=1)
    axMod.plot(deltaPlot,deltaForcePlot, "o-",label=file.replace(".txt",""))
    axMod.plot(xFit, xFit*fitHerzt[0] +fitHerzt[1] ,"--",label="_no label_")
    figMod.savefig(nameFile+"_fitIndent.png")

    #for adhesion, the minimum value in return
    adhesion=dataRetract[headerForce].min()


    figFit, axFit = plt.subplots(nrows=1, ncols=1)
    axFit.plot(myData[headerHeihg],myData[headerForce], "o-",label=file.replace(".txt",""))
   # axFit.plot(fitUp[headerHeihg], fitUp[headerForce], "--",c="black",label="_no label_")
    #axFit.plot(fitDown[headerHeihg], fitDown[headerForce], "--",c="black",label="_no label_")

     #Plot line of the curve
    dataLineX=np.array([fitUp[headerHeihg].iloc[0],fitUp[headerHeihg].iloc[-1]])
    dataLineY=np.array([dataLineX[0]*eModApproach+cUp,dataLineX[1]*eModApproach+cUp])
    axFit.plot(dataLineX, dataLineY,label="_no label_")

    dataLineX=np.array([fitDown[headerHeihg].iloc[0],fitDown[headerHeihg].iloc[-1]])
    dataLineY=np.array([dataLineX[0]*eModRetract+cDown,dataLineX[1]*eModRetract+cDown])
    axFit.plot(dataLineX, dataLineY,label="_no label_")

    #also plot indentation
    axFit.plot(delta, dataApproach[headerForce],label="_no label_")

    #find x of starting s

    #stiffness id the max value in the 
    stiffness=myMaxVal-stiffThreshold
    stiffnessWithUpSetPoint=fitTresh[1]-stiffThreshold
    
    #find two nearest point with stiffness threshold value
    nearestvals= dataApproach.iloc[(dataApproach[headerForce]-stiffThreshold).abs().argsort()[:2]]
    getX=interpolateXval(nearestvals[headerHeihg].iloc[0],nearestvals[headerHeihg].iloc[1],nearestvals[headerForce].iloc[0],nearestvals[headerForce].iloc[1],stiffThreshold)
    #stiffFitCalc=stiffness/abs(myMaxValX-getX)
    stiffFitCalc=stiffness/abs(myMaxValX-xStart)
    stiffFitCalcWithUpSetPoint=stiffnessWithUpSetPoint/abs(myMaxValX-xStart)
    #con fit
    fitThres=dataApproach.loc[(dataApproach[headerForce]>=stiffThreshold) & (dataApproach[headerForce]<=fitTresh[1])]
    pUp=np.polyfit(fitThres[headerHeihg], fitThres[headerForce], 1)
    stiffFit = abs(pUp[0])  # Gradient
    cUp = pUp[1]  # y-intercept

    xFit=np.array([fitThres[headerHeihg].min(),fitThres[headerHeihg].max()])
    yFit=xFit*pUp[0]+cUp
    axFit.plot(fitThres[headerHeihg], fitThres[headerForce],"--",label="for threshold")
    axFit.plot(xFit, yFit,label="for threshold")
    axFit.plot([getX,myMaxValX], [stiffThreshold,myMaxVal],"o",c="red",ms=6,label="_no label_")
    axFit.vlines(xStart,-2,100,linestyles="dashed",colors="red")


    axFit.legend()
    axFit.set_xlabel(myData.columns[1])
    axFit.set_ylabel(myData.columns[2])
    axFit.grid()
    figFit.savefig(nameFile+"_fit.png")

    #get modulus
    eModApproach=np.abs(eModApproach)
    eModRetract=np.abs(eModRetract)

    #save down
    #myList=[file.replace(".txt",""),stiffness,stiffFitCalc*getNanoEntreMicro(units[0],units[1]),stiffFit*getNanoEntreMicro(units[0],units[1]),eModApproach*getNanoEntreMicro(units[0],units[1]),eModRetract*getNanoEntreMicro(units[0],units[1]),(eModApproach+eModRetract)*getNanoEntreMicro(units[0],units[1])/2,np.abs(adhesion),xStart, myMaxValX,getX]
    #myList=[file.replace(".txt",""),stiffness/getSI(units[1]),stiffFitCalc,stiffFit,eModApproach,eModRetract,(eModApproach+eModRetract)/2,np.abs(adhesion)/getSI(units[0]),xStart/getSI(units[0]), myMaxValX/getSI(units[0]),getX/getSI(units[0])]
    myList=[file.replace(".txt",""),stiffness,stiffnessWithUpSetPoint,
        stiffFitCalc*getSI(units[1])/getSI(units[0]),stiffFitCalcWithUpSetPoint*getSI(units[1])/getSI(units[0]),
        stiffFit*getSI(units[1])/getSI(units[0]),eModApproach*getSI(units[1])/getSI(units[0]),eModRetract*getSI(units[1])/getSI(units[0]),
        eModApproach2*getSI(units[1])/(getSI(units[0])*getSI(units[0])),eModRetract2*getSI(units[1])/(getSI(units[0])*getSI(units[0])),eHertz*getSI(units[1])/(getSI(units[0])*getSI(units[0])),
        ((eModApproach+eModRetract)*getSI(units[1])/getSI(units[0]))/2,np.abs(adhesion),a
        ]
    myListAll=myList+[xStart, myMaxValX,getX]
    dataModulusAll=dataModulusAll.append(pd.DataFrame([myListAll], 
     columns=myColsAll), 
     ignore_index=True)    #fig2, ax2 = plt.subplots(nrows=1, ncols=1)
    #upDif=dataApproach[headerForce].diff()/dataApproach[headerHeihg].diff()
    #downDif=dataRetract[headerForce].diff()/dataRetract[headerHeihg].diff()
    upDif=dataApproach[headerForce].diff()
    downDif=dataRetract[headerForce].diff()

    #ax.plot(dataApproach[headerHeihg],upDif/upDif.max()*100,c="green")
    #ax.plot(dataRetract[headerHeihg],downDif/downDif.max()*100,c="red")
    #ax2.grid()
    #ax2.set_yscale("log")
    #axFit.plot(dataRetract[headerHeihg],dataRetract[headerForce].diff())
    #plt.show()
    #input("Done")



    #Move all so they are at same z value
    minInd=dataRetract[headerForce].idxmin()
    valXMin=dataRetract[headerHeihg].loc[minInd]
    dataApproachheaderHeihg=(dataApproach[headerHeihg]-valXMin)+1
    myDataheaderHeihg=(myData[headerHeihg]-valXMin)+1
    dataRetractheaderHeihg=(dataRetract[headerHeihg]-valXMin)+1
    myDataheaderHeihg=(myData[headerHeihg]-valXMin)+1
    axGen.plot(myDataheaderHeihg,myData[headerForce], "o-",label=file.replace(".txt","")+"_%.3f X" %(valXMin) )
    #axGen.plot(dataApproachheaderHeihg,dataApproach[headerForce], "o-",label=file.replace(".txt","")+"_%.3f X" %(valXMin) )
    #axGen.plot(dataRetractheaderHeihg,dataRetract[headerForce], "--",label="_no label_",cmap="tab20")
    totalXvalUp.append(dataApproachheaderHeihg.values)
    totalXvalDown.append(dataRetractheaderHeihg.values)
    totalYvalUp.append(dataApproach[headerForce].values)
    totalYvalDown.append(dataRetract[headerForce].values)
plt.close("all")
axGen.legend()
axGen.set_xlabel(myData.columns[1])
axGen.set_ylabel(myData.columns[2])
axGen.grid()


nameFile=path+"FD_Plot_All"
figGen.savefig(nameFile+".png")
pickle.dump(figGen, open(nameFile+".pickel", 'wb'))

#get mean
x=dataModulusAll.mean()
print("getting mean")
x["file"]="MEAN"
dataModulusAll=dataModulusAll.append(x,ignore_index=True)
xSTD=dataModulusAll.std()
xSTD["file"]="STD"
dataModulusAll=dataModulusAll.append(xSTD,ignore_index=True)
dataModulusAll["Outlier"]=""
for col in myCols[1:]:
    if "file" in col:
        dataModulusAll[col].loc[dataModulusAll["file"]=="STD"]=""
        dataModulusAll[col].loc[dataModulusAll["file"]=="MEAN"]=""
        continue
    dataModulusAll["Outlier"].loc[abs(dataModulusAll[col]-x[col])>xSTD[col]]="X"

dataModulusAll["Outlier"].loc[dataModulusAll["file"]=="STD"]=""
dataModulusAll["Outlier"].loc[dataModulusAll["file"]=="MEAN"]=""
dataModulusAll[myCols].to_excel(nameFile.replace("_Plot","_DATA")+".xlsx")
dataModulusAll.to_excel(nameFile.replace("_Plot","_DATA_AllParam")+".xlsx")

#mean of all plots
if getMeanAll:
    [x_resultUp,y_resultUp,err_xUp,dy_resultUp]=getMean(totalXvalUp,totalYvalUp,"interpolate")
    [x_resultDown,y_resultDown,err_xDown,dy_resultDown]=getMean(totalXvalDown,totalYvalDown,"interpolate")

    figMean, axMean = plt.subplots(nrows=1, ncols=1)
    axMean.plot(x_resultUp,y_resultUp, "o-")
    axMean.plot(x_resultDown,y_resultDown, "o-")
    axMean.set_xlabel(myData.columns[1])
    axMean.set_ylabel(myData.columns[2])
    axMean.grid()
    figMean.savefig(nameFile+"_Mean.png")


plt.show()



#showData=input("Show data? y/n: ")
#if showData=="y":
#    print("Showing graphs")
#    plt.show()
#    input("Finish")
#else:
#    plt.close("all")