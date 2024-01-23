# -*- coding: utf-8 -*-
"""""
Created on Fri Apr 23 15:13:02 2021

@author: M. Pedrosa Bustos
"""

from monolayerClass import Monolayer
from monolayerDBClass import MonolayerDB

'''
"TFG/Chol-DPPC-067_B1/Chol-DPPC-067_B1",
"TFG/Chol-DPPC-067_B3/Chol-DPPC-067_B3",
"TFG/Chol-DPPC-067_B4/Chol-DPPC-067_B4",
"TFG/Chol-DPPC-Cur-00_B1/Chol-DPPC-Cur-00_B1",
"TFG/Chol-DPPC-Cur-00_B2/Chol-DPPC-Cur-00_B2",
"TFG/Chol-DPPC-Curc-03_B1/Chol-DPPC-Curc-03_B1",
"TFG/Chol-DPPC-Curc-03_B2/Chol-DPPC-Curc-03_B2",
"TFG/Chol-DPPC-Curc-05_B1/Chol-DPPC-Curc-05_B1",
"TFG/Chol-DPPC-Curc-05_B2/Chol-DPPC-Curc-05_B2",
"TFG/Chol-DPPC-Curc-07_B1/Chol-DPPC-Curc-07_B1",
"TFG/Chol-DPPC-Curc-07_B2/Chol-DPPC-Curc-07_B2",
"TFG/Chol-Sph-025_B1/Chol-Sph-025_B1",
"TFG/Chol-Sph-025_B2/Chol-Sph-025_B2",
"TFG/Chol-Sph-Curc-00_B2/Chol-Sph-Curc-00_B2",
"TFG/Chol-Sph-Curc-00_B3/Chol-Sph-Curc-00_B3",
"TFG/Chol-Sph-Curc-03_B2/Chol-Sph-Curc-03_B2",
"TFG/Chol-Sph-Curc-03_B3/Chol-Sph-Curc-03_B3",
"TFG/Chol-Sph-Curc-05_B2/Chol-Sph-Curc-05_B2",
"TFG/Chol-Sph-Curc-05_B3/Chol-Sph-Curc-05_B3",
"TFG/Chol-Sph-Curc-07_B2/Chol-Sph-Curc-07_B2",
"TFG/Chol-Sph-Curc-07_B3/Chol-Sph-Curc-07_B3",
"TFG/Sph_fix_B1/Sph_fix_B1",
"TFG/Sph_fix_B2/Sph_fix_B2",
"TFG/Sph_fix_B3/Sph_fix_B3",
"TFG/Chol-DPPC-Curc-00_B1/Chol-DPPC-Curc-00_B1",
"TFG/Chol-DPPC-Curc-00_B2/Chol-DPPC-Curc-00_B2",
"TFG/Chol-Sph-Curc-00_B2/Chol-Sph-Curc-00_B2",
"TFG/Chol-Sph-Curc-00_B3/Chol-Sph-Curc-00_B3",

"TFG/Chol-DPPC-Curc-10_B1/Chol-DPPC-Curc-10_B1",
"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2",
"TFG/Chol-Sph-Curc-10_B2/Chol-Sph-Curc-10_B2",
"TFG/Chol-Sph-Curc-10_B3/Chol-Sph-Curc-10_B3",
"TFG/Chol-DPPC-Curc-10_B1/Chol-DPPC-Curc-10_B1",
"TFG/Chol-DPPC-Curc-10_B2/Chol-DPPC-Curc-10_B2",
"TFG/Chol-Sph-Curc-10_B2/Chol-Sph-Curc-10_B2",
"TFG/Chol-Sph-Curc-10_B3/Chol-Sph-Curc-10_B3",

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
#"SphB1009N20/SphB1009N20_cont",
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
"MemF1D_W0204Ci/MemF1D_W0204Ci",
"MemF1D_W0204_2/MemF1D_W0204_2",
"MemF1D_W0207Ci/MemF1D_W0207Ci",
"MemF1D_W0207Ci_3/MemF1D_W0207Ci_3",
"MemF1D_W0207_2/MemF1D_W0207_2",
"MemF1D_W0208/MemF1D_W0208",
"MemF1D_W0208Ci_2/MemF1D_W0208Ci_2",
"MemF1D_W0208Dip/MemF1D_W0208Dip",
"MemF1D_W0208_3/MemF1D_W0208_3",
"MemF1D_W0209/MemF1D_W0209",
"MemF1D_W0209Ci/MemF1D_W0209Ci",
"MemF1D_W0209Ci_2/MemF1D_W0209Ci_2",
"MemF1D_W0210/MemF1D_W0210",
"MemF1D_W0210_2/MemF1D_W0210_2",
"MemF1D_W0211_2/MemF1D_W0211_2",
"MemF1D_W0215Ci/MemF1D_W0215Ci",
"MemF1D_W0215Ci_3/MemF1D_W0215Ci_3",
"MemF1D_W0215f/MemF1D_W0215f",
"MemF1D_W0216Ci/MemF1D_W0216Ci",
"MemF1D_W0216Ci_2/MemF1D_W0216Ci_2",
"MemF1D_W0218Ci/MemF1D_W0218Ci",
"MemF1D_W0221/MemF1D_W0221",
"MemF1D_W0221Ci/MemF1D_W0221Ci",
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

]
pathAll=[
"MemF1Clo_W0210/MemF1Clo_W0210",
"MemF1D_W0204Ci/MemF1D_W0204Ci",
"MemF1D_W0204_2/MemF1D_W0204_2",
"MemF1D_W0207Ci/MemF1D_W0207Ci",
"MemF1D_W0207Ci_3/MemF1D_W0207Ci_3",
"MemF1D_W0207_2/MemF1D_W0207_2",
"MemF1D_W0208/MemF1D_W0208",
"MemF1D_W0208Ci_2/MemF1D_W0208Ci_2",
"MemF1D_W0208Dip/MemF1D_W0208Dip",
"MemF1D_W0208_3/MemF1D_W0208_3",
"MemF1D_W0209/MemF1D_W0209",
"MemF1D_W0209Ci/MemF1D_W0209Ci",
"MemF1D_W0209Ci_2/MemF1D_W0209Ci_2",
"MemF1D_W0210/MemF1D_W0210",
"MemF1D_W0210_2/MemF1D_W0210_2",
"MemF1D_W0211_2/MemF1D_W0211_2",
"MemF1D_W0215Ci/MemF1D_W0215Ci",
"MemF1D_W0215Ci_3/MemF1D_W0215Ci_3",
"MemF1D_W0215f/MemF1D_W0215f",
"MemF1D_W0216Ci/MemF1D_W0216Ci",
"MemF1D_W0216Ci_2/MemF1D_W0216Ci_2",
"MemF1D_W0218Ci/MemF1D_W0218Ci",
"MemF1D_W0221/MemF1D_W0221",
"MemF1D_W0221Ci/MemF1D_W0221Ci",
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


"MemF1D_B0404Ci/MemF1D_B0404Ci",
"MemF1D_B0504Ci/MemF1D_B0504Ci",
"MemF1D_B0504Ci2/MemF1D_B0504Ci2",

"MemF2D_W0704Ci/MemF2D_W0704Ci",
"MemF2D_W0704Ci2/MemF2D_W0704Ci2",
"MemF1D_W0704Ci/MemF1D_W0704Ci",
"MemF2D_W0704Ci3/MemF2D_W0704Ci3",

"MemF1D_W0804Ci/MemF1D_W0804Ci",
"MemF1D_B0804Ci/MemF1D_B0804Ci",
#"Cur_B0509/Cur_B0509",  #Good
#"Cur_B0512Ci/Cur_B0512Ci",
#"Cur_B0509Ci/Cur_B0509Ci",  #Good
"Cur_B0512CiMore/Cur_B0512CiMore",
]
pathAll=[

]

pathAll=[



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
"C-PC040B1125D2/C-PC040B1125D2",
"C-PC067B1124D/C-PC067B1124D",
"C-PC067B1124D2/C-PC067B1124D2",
"C-PC040B1125D/C-PC040B1125D",
"C-PC040B1125D2/C-PC040B1125D2",
"C-PC0401125/C-PC0401125",
"DPPC_B0119/DPPC_B0119",
"DPPC_B0120/DPPC_B0120",


]

db=MonolayerDB("Data")

#db.removeEntry("Chol_B0910N25_BAD")
from os import listdir
folder="Data"
#pathAll=[f+"/"+f for f in listdir(folder) if "Mem" in f]

for path in pathAll:
   if path in ["MemF1Clo_W0210/MemF1Clo_W0210","MemF1_W0118/MemF1_W0118","MemF1D_W0209Ci/MemF1D_W0209Ci","MemF1D_W0210/MemF1D_W0210"]:
      continue

   path="Data/"+path+"_IMG.xlsx"
   myMonolayer=Monolayer(path)
   givenName=myMonolayer.param["Name"]
   prev="Data/"
   if "TFG" in path:
      prev=prev+"TFG/"+givenName
   #givenName="Data/"+givenName
   myMonolayer.param["HTML"]="Data/"+givenName.split("_tuned")[0]+"/"+givenName+".html"
   myMonolayer.param["IMG"]="Data/"+givenName.split("_tuned")[0]+"/"+givenName+".png"
   if "_tuned" in path:
      myMonolayer.param["HTML"]=myMonolayer.param["HTML"].replace(".html","_tuned.html")
      myMonolayer.param["IMG"]=myMonolayer.param["IMG"].replace(".png","_tuned.png")

   print(myMonolayer.param["HTML"])  

#   try:
#      print(myMonolayer.param["HTML"])
#     # givenName=myMonolayer.param["HTML"].split("Data")[-1].split("/")[-1].split(".html")[0]
#      givenName=myMonolayer.param["Name"]
#      if "_tuned" in path:
#         givenName=givenName+"_tuned"
#      myMonolayer.param["HTML"]="Data/"+givenName.split("_tuned")[0]+"/"+givenName+".html"
#      myMonolayer.param["IMG"]="Data/"+givenName.split("_tuned")[0]+"/"+givenName+".png"
#      print(myMonolayer.param["HTML"])
#   except:
#      print(path)
#      pathIn=input("HTML: ")
#      myMonolayer.param["HTML"]="Data/"+pathIn.split("_tuned")[0].split(".html")[0]+"/"+pathIn
#      pathIn=input("IMG: ")
#      myMonolayer.param["IMG"]="Data/"+pathIn.split("_tuned")[0].split(".png")[0]+"/"+pathIn
   
   myMonolayer.to_excel(path)
   
   db.to_JSON(myMonolayer)

   #db.con.commit()

