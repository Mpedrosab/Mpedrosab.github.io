# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:13:02 2017

@author: M. Pedrosa Bustos
"""
from BAMImgClass import BAMImg
from monolayerClass import Monolayer
import matplotlib.pyplot as plt

'''
    Create pandas with img and save as html

'''
'''
####to check which one is not in here

fileNamesAlready=""
ls -t1 Chol* > all.txt
echo "" > notincluded.txt
while read p
     do num=$(grep -c $p $fileNamesAlready)
     if [ $num == 0 ]
     then echo $p >> notincluded.txt
     fi
done < all.txt


'''

pathAll=[
    "DPPC_W0427N20sf/DPPC_W0427N20sf",
 "DPPC_W0427N20s/DPPC_W0427N20s",
   "Chol_B0423Xss/Chol_B0423Xss_tuned",           
   "Chol_B0423X20s/Chol_B0423X20s",           
   "Chol_B0415X36/Chol_B0415X36",           
   "DPPC_B0423X20s/DPPC_B0423X20s",           
   "DPPC_B2103X/DPPC_B2103X",
   "Chol_B0414Y/Chol_B0414Y",              
   "Chol_B0422Y20/Chol_B0422Y20",      
   "DPPC_W1/DPPC_W1",
   "Chol_B0414Y25/Chol_B0414Y25",         
   #"DPPC_W1/DPPC_W1_cont2",
   "Chol_B0414Y25S/Chol_B0414Y25S_tuned",       
   "Chol_W1/Chol_W1",                  
   #"DPPC_W1/DPPC_W1_cont",
   #"Chol_B0414Y25S/Chol_B0414Y25S_main",
   "DPPC_B0413Y/DPPC_B0413Y",           
   #"DPPC_W1/DPPC_W1_main",
   "DPPC_B0413Y2/DPPC_B0413Y2",        
   #"Chol_B0414Y25S/Chol_B0414Y25Sc2", 
   "DPPC_B0415X36/DPPC_B0415X36",    
   "DPPC_W2/DPPC_W2",
   # "Chol_B0414Y25S/Chol_B0414Y25Sc", 
   "DPPC_B0420Y20/DPPC_B0420Y20", 
   #"DPPC_W2/DPPC_W2_principal",
   #"DPPC_W2/DPPC_W2cont",
   "DPPC_B0422Y20s/DPPC_B0422Y20s",   
   "DPPC_W3/DPPC_W3",
"Chol_W0428N20s/Chol_W0428N20s",
"DPPC_B0428N20/DPPC_B0428N20",
"DPPC_B0428N20f/DPPC_B0428N20f",
"DPPC_B0428N25/DPPC_B0428N25",
"DPPC_B0430N25/DPPC_B0430N25",
"DPPC_B0430N36/DPPC_B0430N36",
"Chol_B0527N20/Chol_B0527N20",
"DPPC_B0723N20/DPPC_B0723N20",
"Chol_B0721N20/Chol_B0721N20",
"Chol_B0720N20/Chol_B0720N20",
"CholPC067_B0723/CholPC067_B0723",
"CholPCCur03B0727/CholPCCur03B0727",
"CholPCCur05B0727/CholPCCur05B0727",
"CholPCCur07B0727/CholPCCur07B0727",
"C-PC067_B0729D20/C-PC067_B0729D20",
"C-PC067_B0729D25/C-PC067_B0729D25",
"Cur_B0727N20/Cur_B0727N20",
#"Sph_B0909N20/Sph_B0909N20",
"Chol_B0909N20/Chol_B0909N20",
"Sph_B0909N20b/Sph_B0909N20b",
"Chol_B0909N25b/Chol_B0909N25b",
"Sph_B0909N20/Sph_B0909N20",
"Sph_B0910N20/Sph_B0910N20",
#"Sph_B1009N20/Sph_B1009N20_cont",
"Chol_B0910N25_BAD/Chol_B0910N25_BAD",
"Chol_B0913N20/Chol_B0913N20",
"C-Sph_B0913N20/C-Sph_B0913N20",
"C-Sph_B0913D20/C-Sph_B0913D20",
"Sph_B0914N20/Sph_B0914N20",
"Cur_B0915N20/Cur_B0915N20",
"C-Sph_B0915N20/C-Sph_B0915N20",
"C-Sph_B0915D20f/C-Sph_B0915D20f",
"Cur_B0917N20f/Cur_B0917N20f",
#"Cur_B0917N20_BAD/Cur_B0917N20_BAD",

"Cur_B0917N20b/Cur_B0917N20b",
"Cur_B0920N20/Cur_B0920N20",
#"C-SphB0921N20/C-SphB0921N20_tuned",
"C-SphB0921D20/C-SphB0921D20",
#"C-SphCur03B0922/C-SphCur03B0922",
"C-SphCur03B0922D/C-SphCur03B0922D",
"C-SphCur05B0922/C-SphCur05B0922",
"C-SphCur05B0923D/C-SphCur05B0923D",
"C-SphCur07B0923/C-SphCur07B0923",
"C-SphCur07B0924D/C-SphCur07B0924D",
"DPPC_B0930N20/DPPC_B0930N20",
"C-PCB1004D20/C-PCB1004D20",
"C-PCCur03B1004D20/C-PCCur03B1004D20",

"C-PCB1004D20/C-PCB1004D20",

"C-PCCur03B1004D/C-PCCur03B1004D",
"C-PCCur05B1005D/C-PCCur05B1005D",
"C-PCCur07B1005D/C-PCCur07B1005D",
"C-PCCur07B1005Df/C-PCCur07B1005Df",
"C-SphCur03B0922/C-SphCur03B0922",
"C-SphCur03B0922D/C-SphCur03B0922D",
"C-SphCur05B0922/C-SphCur05B0922",
"C-SphCur05B0923D/C-SphCur05B0923D",
"C-SphCur07B0923/C-SphCur07B0923",
"C-SphCur07B0924D/C-SphCur07B0924D",
"MemF1Clo_W0210/MemF1Clo_W0210",
"MemF1_W0204Ci/MemF1_W0204Ci",
"MemF1_W0204_2/MemF1_W0204_2",
"MemF1_W0207Ci/MemF1_W0207Ci",
"MemF1_W0207Ci_3/MemF1_W0207Ci_3",
"MemF1_W0207_2/MemF1_W0207_2",
"MemF1_W0208/MemF1_W0208",
"MemF1_W0208Ci_2/MemF1_W0208Ci_2",
"MemF1_W0208Dip/MemF1_W0208Dip",
"MemF1_W0208_3/MemF1_W0208_3",
"MemF1_W0209/MemF1_W0209",
"MemF1_W0209Ci/MemF1_W0209Ci",
"MemF1_W0209Ci_2/MemF1_W0209Ci_2",
"MemF1_W0210/MemF1_W0210",
"MemF1_W0210_2/MemF1_W0210_2",
"MemF1_W0211_2/MemF1_W0211_2",
"MemF1_W0215Ci/MemF1_W0215Ci",
"MemF1_W0215Ci_3/MemF1_W0215Ci_3",
"MemF1_W0215f/MemF1_W0215f",
"MemF1_W0216Ci/MemF1_W0216Ci",
"MemF1_W0216Ci_2/MemF1_W0216Ci_2",
"MemF1_W0218Ci/MemF1_W0218Ci",
"MemF1_W0221/MemF1_W0221",
"MemF1_W0221Ci/MemF1_W0221Ci",
"MemF1_W0118/MemF1_W0118",
"MemF1_W01182/MemF1_W01182",
"MemF1_W01183/MemF1_W01183",
"MemF1_W01184/MemF1_W01184",
"MemF1_W0120/MemF1_W0120",
"MemF1_W01202/MemF1_W01202",
"MemF1_W01203/MemF1_W01203",
"MemF1_W01204/MemF1_W01204",
"MemF1_W0121/MemF1_W0121",
"MemF1_W01212/MemF1_W01212",
"MemF1_W01215/MemF1_W01215",
"MemF1_W01216/MemF1_W01216",
"MemF1_W0126Clop/MemF1_W0126Clop",
"MemF1_W0126Clop2/MemF1_W0126Clop2",
"MemF1_W0127Ci/MemF1_W0127Ci",
"MemF1_W0128/MemF1_W0128",
"MemF1_W01283/MemF1_W01283",
"MemF1_W0128Ci2/MemF1_W0128Ci2",
"MemF1_W0204/MemF1_W0204",
"MemF1_W0217Ci/MemF1_W0217Ci",
"MemF1_W0217Ci_2/MemF1_W0217Ci_2",
"MemF1_W0218Ci/MemF1_W0218Ci",
"MemF1_W0222Ci/MemF1_W0222Ci",
"MemF1_W0222Ci_3/MemF1_W0222Ci_3",
"MemF1_W0222_2/MemF1_W0222_2",
"MemF2_W0131Ci/MemF2_W0131Ci",
"MemF2_W0131Ci2/MemF2_W0131Ci2",
"MemF2_W0201/MemF2_W0201",
"MemF2_W0201Ci/MemF2_W0201Ci",
"MemF2_W0201_2/MemF2_W0201_2",
"MemF2_W0202/MemF2_W0202",
"MemF2_W0202Ci/MemF2_W0202Ci",
"MemF2_W0202Ul/MemF2_W0202Ul",
"MemF2_W0203/MemF2_W0203",
"MemF2_W0203_2/MemF2_W0203_2",

"MemF1_B0404Ci/MemF1_B0404Ci",

"MemF1_B0404Ci/MemF1_B0404Ci",
"MemF1_B0504Ci/MemF1_B0504Ci",
"MemF1_B0504Ci2/MemF1_B0504Ci2",

"MemF2_W0704Ci/MemF2_W0704Ci",
"MemF2_W0704Ci2/MemF2_W0704Ci2",
"MemF1_W0704Ci/MemF1_W0704Ci",
"MemF2_W0704Ci3/MemF2_W0704Ci3",

"MemF1_W0804Ci/MemF1_W0804Ci",
"MemF1_B0804Ci/MemF1_B0804Ci",

"Cur_B0509/Cur_B0509",
"Cur_B0509More/Cur_B0509More",
"Cur_B0509Ci/Cur_B0509Ci",

"Cur_B0511CiSlow/Cur_B0511CiSlow",
"Cur_B0511CiSlo2/Cur_B0511CiSlo2",
"Cur_B0511CiSlof/Cur_B0511CiSlof",


"Cur_B0509Ci/Cur_B0509Ci",  #Good
"Cur_B0509/Cur_B0509",  #Good
"Cur_B0512Ci/Cur_B0512Ci",
"Cur_B0512CiMore/Cur_B0512CiMore",


"CholPC90_0126/CholPC90_0126",
"CholPC80_0126/CholPC80_0126",
"CholPC80_B0126_2/CholPC80_B0126_2",
"CholPC25_B0125/CholPC25_B0125",
"CholPC40_B0125/CholPC40_B0125",
"CholPC10_B0125/CholPC10_B0125",
"CholPC90_B0123/CholPC90_B0123",
"CholPC25_0120/CholPC25_0120",
"CholPC10_0120/CholPC10_0120",
"CholPC80_0123/CholPC80_0123",
"C-PC040B1125D2/C-PC040B1125D2"

"DPPC_1812/DPPC_1812",
"HealthM_1812IDdi/HealthM_1812IDdi",
"HealthyM_1112ID/HealthyM_1112ID",
"HealthyM_1204/HealthyM_1204",
"HealthyM_1211IT/HealthyM_1211IT",
"HealthyM_1412ID/HealthyM_1412ID",
"HealthyM_1412SP/HealthyM_1412SP",
"HealthyM_1512ID/HealthyM_1512ID",
"HealthyM_1812ID2/HealthyM_1812ID2",
"HelthM_1812_ITdi/HelthM_1812_ITdi",
"Sph_S1204/Sph_S1204",
"Sph_S1211/Sph_S1211",
"Tumor_2212/Tumor_2212",
"Tumor_2212ID/Tumor_2212ID",
"Tumor_2212ID2/Tumor_2212ID2",
"TumorM_1205/TumorM_1205",
"TumorM_1205ID/TumorM_1205ID",
"TumorM_1211ID/TumorM_1211ID",
"TumorM_1212BAD/TumorM_1212BAD",
"TumorM_1213SP/TumorM_1213SP",
"TumorM_1412dip/TumorM_1412dip",
"TumorM_1412SD/TumorM_1412SD",
"TumorM_2012BAD2/TumorM_2012BAD2",
"TumorM_2012ID/TumorM_2012ID",
"TumorM_2012IT/TumorM_2012IT",
"TumorM_2012ITBAD/TumorM_2012ITBAD",
"TumorM_2112/TumorM_2112",
"TumorM_2112IT/TumorM_2112IT",
"TumorM_2112_SD/TumorM_2112_SD",
"TumorM_2112SD2/TumorM_2112SD2",
]
pathAll=[

#"MemF1_B0504Ci2/MemF1_B0504Ci2",
#"MemF1_B0404Ci/MemF1_B0404Ci",
#"MemF1_W0804Ci/MemF1_W0804Ci",
#"MemF1_B0804Ci/MemF1_B0804Ci",
#"MemF1_W0704Ci/MemF1_W0704Ci",
#"MemF1_B0504Ci/MemF1_B0504Ci",
#"MemF1_W0221Ci/MemF1_W0221Ci",
#"MemF1_W0221/MemF1_W0221",
#"MemF1_W0218Ci/MemF1_W0218Ci",
#"MemF1_W0216Ci/MemF1_W0216Ci",
#"MemF1_W0216Ci_2/MemF1_W0216Ci_2",
#"MemF1_W0211_2/MemF1_W0211_2",
#"MemF1_W0215Ci_3/MemF1_W0215Ci_3",
#"MemF1_W0215Ci/MemF1_W0215Ci",
#"MemF1_W0215f/MemF1_W0215f",
#"MemF1_W0204Ci/MemF1_W0204Ci",
#"MemF1_W0210/MemF1_W0210",
#"MemF1_W0210_2/MemF1_W0210_2",
#"MemF1_W0209Ci_2/MemF1_W0209Ci_2",
#"MemF1_W0209/MemF1_W0209",
#"MemF1_W0208/MemF1_W0208",
#"MemF1_W0208_3/MemF1_W0208_3",
#"MemF1_W0208Dip/MemF1_W0208Dip",
#"MemF1_W0208Ci_2/MemF1_W0208Ci_2",
#"MemF1_W0207Ci_3/MemF1_W0207Ci_3",
#"MemF1_W0207_2/MemF1_W0207_2",
#"MemF1_W0207Ci/MemF1_W0207Ci",
#"MemF1_W0204_2/MemF1_W0204_2",
#"MemF2_W0704Ci3/MemF2_W0704Ci3",
#"MemF2_W0704Ci/MemF2_W0704Ci",
#"MemF2_W0704Ci2/MemF2_W0704Ci2"
#"C-PC067B1124D/C-PC067B1124D",
#"C-PC067B1124D2/C-PC067B1124D2",
#"C-PC040B1125D/C-PC040B1125D",
#"C-PC040B1125D2/C-PC040B1125D2",
#"C-PC0401125/C-PC0401125",
#"DPPC_B0119/DPPC_B0119",
#"DPPC_B0120/DPPC_B0120",

#"DPPC_1812/DPPC_1812",
#"HealthM_1812IDdi/HealthM_1812IDdi",
#"HealthyM_1112ID/HealthyM_1112ID",
#"HealthyM_1204/HealthyM_1204",
#"HealthyM_1211IT/HealthyM_1211IT",
#"HealthyM_1412ID/HealthyM_1412ID",
#"HealthyM_1412SP/HealthyM_1412SP",
#"HealthyM_1512ID/HealthyM_1512ID",  #*
#"HealthyM_1812ID2/HealthyM_1812ID2",
#"HelthM_1812_ITdi/HelthM_1812_ITdi",
"Sph_S1204/Sph_S1204",  #*
#"Sph_S1211/Sph_S1211",
#"TumorM_2212/TumorM_2212",
#"TumorM_2212ID/TumorM_2212ID",
#"TumorM_2212ID2/TumorM_2212ID2",
#"TumorM_1205/TumorM_1205",
#"TumorM_1205ID/TumorM_1205ID",
#"TumorM_1211ID/TumorM_1211ID",
#"TumorM_1212BAD/TumorM_1212BAD",
#"TumorM_1213SP/TumorM_1213SP",
#"TumorM_1412dip/TumorM_1412dip",
#"TumorM_1412SD/TumorM_1412SD",
#"TumorM_2012BAD2/TumorM_2012BAD2",
#"TumorM_2012ID/TumorM_2012ID",
"TumorM_2012IT/TumorM_2012IT",   #*
#"TumorM_2012ITBAD/TumorM_2012ITBAD",
#"TumorM_2112/TumorM_2112",
"TumorM_2112IT/TumorM_2112IT",    #*
#"TumorM_2112SD/TumorM_2112SD",
#"TumorM_2112SD2/TumorM_2112SD2",
]
#from os import listdir
#folder="Data"
#pathAll=[f+"/"+f for f in listdir(folder) if "Mem" in f]

reached=False

onlyCreateHTML=True       #Set to true if you do not want to create de IMG.xlsx file
for path in pathAll:
    #if path in ["MemF1Clo_W0210/MemF1Clo_W0210","MemF1_W0118/MemF1_W0118","MemF1_W0209Ci/MemF1_W0209Ci","MemF1_W0210/MemF1_W0210"]:
    #    continue
    #if "MemF1_W0222Ci_3" in path:
    #    reached=True
    #if reached==False:
    #    continue
    if "Ci" in path:
        isCycle=True
    else:
        isCycle=False
    #pathRaw="Data/"+path.replace("/","/DataRaw/")
    pathRaw=""+path.replace("/","/DataRaw/")
    #path="Data/"+path
    path=""+path
    print(path)
    if onlyCreateHTML==False:
        data=Monolayer(pathRaw+".xlsx")
        data.param["Name"]=data.param["Name"].replace("F1D", "F1")
        data.param["Name"]=data.param["Name"].replace("F2D", "F2")
        BAMImg.AppendAbs(pathRaw+".sql",data,path+"_IMG.xlsx")

    data=Monolayer(path+"_IMG.xlsx")
    data.RemoveBias()

    pathImg=path+".png"
    myLabel="[%s]=%.2f %s (%d $\mu$l)\n" %(data.param["Substance1"],data.param["Concentration1"],data.param["Unit1"],data.param["Volume1"])
    myLabel+="T=%d $^oC$; $v_{comp}$=%.0f mm/min" %(data.param["Temperature"],data.data['Bspd[mm/min]'].max())
    if "Membrane" in data.param["Substance1"]:
        data.data["AreaPerMass"]=data.data["Area[cm^2]"]*1E2/(data.param["Volume1"]*1E-3*data.param["Concentration1"])
        data.param_label["AreaPerMass"]="$mm^2/mg$"
        img=data.PlotSimple(label=myLabel,xparam="AreaPerMass", cycles= isCycle)

    else:
        img=data.PlotSimple(label=myLabel)
    img[0].savefig(pathImg)
    pathHTML=BAMImg.SaveTableHTML(data,pathImg)
    dataSave=Monolayer(path+"_IMG.xlsx")
    dataSave.param["HTML"]=pathHTML
    dataSave.param["IMG"]=pathImg
    plt.close()
#    except Exception as e:
#        print("Error for %s: %s" %(pathRaw,e))



