# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:13:02 2017

@author: M. Pedrosa Bustos
"""
import matplotlib.pyplot as plt
from monolayerClass import Monolayer
from tikzplotlib import save as tikz_save
plot=plt.subplots()
plot2=plt.subplots()
plotTime=plt.subplots()


myPaths=[
        "MemF2_W0131Ci2/MemF2_W0131Ci2",
        "MemF2_W0202Ci/MemF2_W0202Ci",
        "MemF1D_W0204_2/MemF1D_W0204_2",
#"MemF1D_W0207_2/MemF1D_W0207_2",
"MemF1D_W0207Ci/MemF1D_W0207Ci",
]

myPaths=[
#"MemF1_W0118/MemF1_W0118",
"MemF1_W01182/MemF1_W01182",
"MemF1_W01183/MemF1_W01183",
"MemF1_W01184/MemF1_W01184",
"MemF1_W0120/MemF1_W0120",
"MemF1_W01202/MemF1_W01202",
"MemF1_W01203/MemF1_W01203",
"MemF1_W01204/MemF1_W01204",
"MemF1_W0121/MemF1_W0121",
#"MemF1_W01215/MemF1_W01215",
#"MemF1_W01216/MemF1_W01216",


]


#para comparar
myPaths=[

"MemF2_W0131Ci2/MemF2_W0131Ci2",
"MemF2_W0202Ci/MemF2_W0202Ci",
"MemF1D_W0204_2/MemF1D_W0204_2",
"MemF1D_W0207Ci/MemF1D_W0207Ci",
"MemF1D_W0207Ci_3/MemF1D_W0207Ci_3",
"MemF1D_W0208Ci_2/MemF1D_W0208Ci_2",
"MemF1D_W0208_3/MemF1D_W0208_3",
"MemF1D_W0215Ci/MemF1D_W0215Ci",
"MemF1D_W0216Ci_2/MemF1D_W0216Ci_2",
"MemF1_W0217Ci/MemF1_W0217Ci",
"MemF1_W0217Ci_2/MemF1_W0217Ci_2",
"MemF1_W0218Ci/MemF1_W0218Ci",
"MemF1D_W0218Ci/MemF1D_W0218Ci",

"MemF1D_W0221/MemF1D_W0221",
"MemF1D_W0221Ci/MemF1D_W0221Ci",


"MemF1_W0222Ci/MemF1_W0222Ci",
"MemF1_W0222_2/MemF1_W0222_2",
"MemF1_W0222Ci_3/MemF1_W0222Ci_3",
]



myPaths=[
#"MemF1D_W0215Ci/MemF1D_W0215Ci",
#"MemF1D_W0216Ci_2/MemF1D_W0216Ci_2",
#"MemF1D_W0221Ci/MemF1D_W0221Ci",

"MemF1D_B0404Ci/MemF1D_B0404Ci",
"MemF1D_B0504Ci/MemF1D_B0504Ci",
"MemF1D_B0504Ci2/MemF1D_B0504Ci2",

#"MemF2D_W0704Ci/MemF2D_W0704Ci",
#"MemF2D_W0704Ci2/MemF2D_W0704Ci2",
"MemF1D_W0704Ci/MemF1D_W0704Ci",
#"MemF2D_W0704Ci3/MemF2D_W0704Ci3",


#"MemF1D_B0804Ci/MemF1D_B0804Ci",

"MC7_B0425Ci/MC7_B0425Ci",
"MC7_B0425CiDOx/MC7_B0425CiDOx",
"MC7_B0425CiDOx/MC7_B0425CiDOx_wait",
#"MC7_B0427DOx/MC7_B0427DOx_inyect_raw",
#"MC7_B0427DOx/MC7_B0427DOx_inyect",
"DOX_B0427Ci/DOX_B0427Ci",
#"TFG/Chol-Sph-Curc-10_B2/Chol-Sph-Curc-10_B2_IMG",
#"TFG/Chol-Sph-Curc-10_B3/Chol-Sph-Curc-10_B3_IMG",
#"TFG/Chol-DPPC-Curc-10_B1/Chol-DPPC-Curc-10_B1_IMG",
#"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG",
#"Mean/Chol-DPPC-Curc-10_mean_withFit",
#"Cur_B0920N20/DataRaw/Cur_B0920N20",
##"Cur_B0917N20b/DataRaw/Cur_B0917N20b",
#"Cur_B0917N20f/DataRaw/Cur_B0917N20f",
#"Cur_B0915N20/DataRaw/Cur_B0915N20",
#"Cur_B0727N20/DataRaw/Cur_B0727N20",
"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2_IMG",
"Mean/Chol-DPPC-Curc-10_mean_withFit",
"Cur_B0509/DataRaw/Cur_B0509",
"Cur_B0509More/DataRaw/Cur_B0509More",
"Cur_B0509Ci/DataRaw/Cur_B0509Ci",

"Cur_B0511CiSlow/DataRaw/Cur_B0511CiSlow",
"Cur_B0511CiSlo2/DataRaw/Cur_B0511CiSlo2",
"Cur_B0511CiSlof/DataRaw/Cur_B0511CiSlof",

]


myPaths=[

"MemF1_B0530I2/DataRaw/MemF1_B0530I2",
"MemF1_B0530I2/DataRaw/MemF1_B0530I2dox",
"MemF1_B0530I/DataRaw/MemF1_B0530I",
"MemF1_B0530I/DataRaw/MemF1_B0530Idox",
"MemF1_B0531I/DataRaw/MemF1_B0531I",
"MemF1_B0531I/DataRaw/MemF1_B0531Idox",
"MemF1_B0531I2/DataRaw/MemF1_B0531I2",
"MemF1_B0531I2/DataRaw/MemF1_B0531I2dox",
"MemF1_B0602I/DataRaw/MemF1_B0602I",
"MemF1_B0602I/DataRaw/MemF1_B0602Idox",
"MemF1_B0602I2/DataRaw/MemF1_B0602I2",
"MemF1_B0602I2/DataRaw/MemF1_B0602I2dox",
"MemF1_B0603I2/DataRaw/MemF1_B0603I2dox",
"MemF1_B0603I/DataRaw/MemF1_B0603Itest",


]

myPaths=[

"MemF1_B1215I/DataRaw/MemF1_B1215I",
"MemF1_B0404Ci/DataRaw/MemF1_B0404Ci",
"MemF1_B0504Ci/DataRaw/MemF1_B0504Ci",
#"MemF1_B0504Ci2/DataRaw/MemF1_B0504Ci2",

#"MemF2D_W0704Ci/MemF2D_W0704Ci",
#"MemF2D_W0704Ci2/MemF2D_W0704Ci2",
#"MemF1_W0704Ci/DataRaw/MemF1_W0704Ci",
#"MemF2D_W0704Ci3/MemF2D_W0704Ci3",

"MemF1_B0214/DataRaw/MemF1_B0214",
"MemF1_B0216/DataRaw/MemF1_B0216",
#"MemF1_B0217D/DataRaw/MemF1_B0217D",
]



filepath="Data/"
#filesave="AllCurs"
whatToPlot="AreaPerMass"
#whatToPlot="PercentCompr"
#whatToPlot="T[min]"
#whatToPlot="Mma[A^2/molec]"
#whatToPlot="Area[cm^2]"

#from os import listdir
#folder="Data"
#myPaths=[f+"/"+f for f in listdir(folder) if "Mem" in f and "D_" not in f]

for path in myPaths:

    path="Data/"+path+".xlsx"

    if "Ci" in path:
        
        isCycle=True
    else:
        isCycle=False
    myMonolayer=Monolayer(path)
    myMonolayer.data["T[min]"]=myMonolayer.data["T[s]"]/60.0
    myMonolayer.data["SP[mN/m]/Area[m^2]"]=myMonolayer.data["SP[mN/m]"]/(myMonolayer.data["Area[cm^2]"]/10000)
    myMonolayer.param_label["T[min]"]='Time [min]'
    myMonolayer.param_label["SP[mN/m]/Area[m^2]"]=u'$\pi$ [mN/m]/Area[$m^2$]'
    myMass=(myMonolayer.param["Volume1"]*1E-3*myMonolayer.param["Concentration1"])
    myMonolayer.data["AreaPerMass"]=myMonolayer.data["Area[cm^2]"]*1E2/myMass
    myMonolayer.param_label["AreaPerMass"]="$mm^2/mg$"
    myMonolayer.data["VperArea"]=myMonolayer.data["Area[cm^2]"]/myMonolayer.param["Volume1"]
    myMonolayer.param_label["VperArea"]="$cm^2/ul$"
    myMonolayer.data["PercentCompr"]=100-myMonolayer.data["Area[cm^2]"]*100/(myMonolayer.param["Area"]*0.01)
    myMonolayer.param_label["PercentCompr"]="% compression"
    if "TFG" in path or "Mean" in path:
        myMonolayer.RemoveBias()
    percentSpeed=2*myMonolayer.param["WidthThrough"]*myMonolayer.param["Speed"]*100/myMonolayer.param["Area"]
    #myLabel=' %s' %(myMonolayer.param["Date"].strftime("%d-%b-%Y"))
    #myLabel=' %s, V= %.3f ul (%.3f mg/ml)' %(myMonolayer.param["Name"],myMonolayer.param["Volume1"],myMonolayer.param["Concentration1"])
    myLabel=' %s' %(myMonolayer.param["Name"]) #'%s, m= %.3f mg (%.3f mg/ml)' %(myMonolayer.param["Name"],myMass,myMonolayer.param["Concentration1"])
    #myLabel=myMonolayer.param["Name"]    

    if "dox" in path or "test" in path:
        whatToPlot="T[min]"
        plotTime=myMonolayer.PlotSimple(figure=plotTime,xparam=whatToPlot, yparam="SP[mN/m]/Area[m^2]",label=myLabel,markersize=3, cycles=isCycle) # %(myMonolayer.param["Name"]))

    else:
        whatToPlot="AreaPerMass"
        plot2=myMonolayer.PlotSimple(figure=plot2,xparam=whatToPlot,label=myLabel,markersize=3, cycles=isCycle) # %(myMonolayer.param["Name"]))

    #plot2[1].set_ylim(-5,40)
    plot2[1].legend()

   # plot3=myMonolayer.PlotSimple(xparam=whatToPlot,label=myLabel,markersize=3, cycles=isCycle) # %(myMonolayer.param["Name"]))
   # if whatToPlot=="T[min]":
       
       # plot3[1].set_ylim(25,36)
    #else:
       # plot3[1].set_ylim(-5,40)

    #plot3[1].legend()
   # plot3[0].savefig(path.replace("DataRaw/","")+myMonolayer.param["Name"]+".png")
    #tikz_save(path+"IMG/"+myMonolayer.param["Name"]+".tikz",plot3[0],axis_width = '\\figwidth',encoding ='utf-8') 

    #plot2=myMonolayer.PlotSimple(figure=plot2,xparam=whatToPlot,label=myLabel,markersize=3, cycles=isCycle) # %(myMonolayer.param["Name"]))
    #whatToPlotPerc="PercentCompr"
    #plot=myMonolayer.PlotSimple(figure=plot,xparam=whatToPlotPerc,label=myLabel,markersize=3, cycles=isCycle) # %(myMonolayer.param["Name"]))

    print ("Vol:  %.2f ul Mass:  %.3f ul; Initial:  %.3f Final:  %.3f" %( myMonolayer.param["Volume1"],myMass,myMonolayer.data["AreaPerMass"].iloc[0], myMonolayer.data["AreaPerMass"].iloc[-1] ))

if whatToPlot=="PercentCompr":
    plot[1].invert_xaxis()
#plot[1].set_ylim(-5,60)
#plot2[1].set_ylim(-5,50)
#plotTime[1].set_ylim(25,40)

#plot2[1].set_xlim(xmax=200000)
#plot[1].legend()
#plot2[1].legend()
plotTime[1].legend()

#plot[1].legend()
plot[1].set_title("Temperature= $%d^oC$" %(myMonolayer.param["Temperature"]))
plot2[1].set_title("Temperature= $%d^oC$" %(myMonolayer.param["Temperature"]))

#plot2[0].savefig(filepath+"IMG/"+filesave+".png")

#tikz_save(path+"IMG/"+filesave+".tikz",plot2[0],axis_width = '\\figwidth',encoding ='utf-8') 

plt.show()
input("Press to exit")