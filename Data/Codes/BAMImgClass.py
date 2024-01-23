# -*- coding: utf-8 -*-
"""
Created on 05/04/21 at 15:13:02

@author: M. Pedrosa Bustos
"""


from monolayerClass import Monolayer
import pandas as pd

class BAMImg:


    def GetIMg(self, imgpath):
        '''
            Load img based on the img name in
            the pandas DataFrame
            
        '''
        #imread.
        return
    
    def SaveTable(self):
        '''
            Saves table with img inserted on it
            worksheet.write(row_num, col_num, col_data)
            
        '''        
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('pandas_image.xlsx', engine='xlsxwriter')
        return

    def path_to_image_html(path):
        #return '<img src="'+ path + '" height="50%" max-width="300px" >'
        if "nan" in path:
            return ""
        return '<img src="'+ path + '" >'     

    def SaveTableHTML(myData,pathImg):
        '''
            Saves table as PDF with img inserted on it
            
        '''        

        if type(myData)==str:
            pathMonolayer=myData
            myData=Monolayer(pathMonolayer)
            name=pathMonolayer.split("/")[-1]
            path=pathMonolayer.split(name)[0]
        else:
            name=myData.param["Name"]
            pathAll=pathImg.split("/")[:-1]
            path=""
            for p in pathAll:
                path+=p+"/" 
            pathImg=pathImg.split("/")[-1]


        pd.set_option('display.max_colwidth', None)
        myData.data["IMG"]="BAMRAW/"+myData.data["BamFile"].astype(str)
        #display(HTML(myData.data.to_html(escape=False ,formatters=dict(image=path_to_image_html))))
        columnsShow=['Mma[A^2/molec]',	'SP[mN/m]', "IMG","BamFile"]

        pd.set_option('colheader_justify', 'center')


        html_string = '''
        <!DOCTYPE html>
        <html>
        <head><title>HTML Pandas Dataframe with CSS</title></head>
        <link rel="stylesheet" type="text/css" href="../../Codes/df_style.css"/>      
 <link rel="stylesheet" type="text/css" href="https://jsxgraph.org/distrib/jsxgraph.css" />
 <script type="text/javascript" src="https://jsxgraph.org/distrib/jsxgraphcore.js">
     <script type="text/javascript" src="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraphcore.js"></script>
     <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
     <script src="/assets/functions/functionsLoadIndividual.js"></script> 
      </script>
        <body>
        <div class="title isotherm_data"><h2>
        '''
        html_string+=name
        html_string+= '''
        </h2>
        <div id="myIsothermPlot" style="display:none">
        '''
        html_string+=name

        html_string+= '''
        </div>

<div id="headerIMG">
        <div id="jxgbox" class="jxgbox_Data" style="width:600px; max-width:100%; height:350px;margin:50px"></div>

<div id="BAMimg"></div>
<div id="Slider"></div>
</div>
'''
     #<img src="myIMG" height="100%"></div>
        html_string+= '''
        <div class="div_isotherm_data">
            {table}
            </div>
        </body>
        </html>
        '''
        #html_string=html_string.replace("myIMG",pathImg)
        pathFinal=path+name+'.html'
        with open(pathFinal, 'w') as f:
            f.write(html_string.format(table=myData.data.to_html(escape=False, classes='isotherm_data',columns=columnsShow, formatters=dict(IMG=BAMImg.path_to_image_html),
                na_rep="",index=False)))
        return pathFinal

    def CreateIndexHTML(pathAll):

        '''
        Creates the div with the different isotherms for the webpage
        

        '''
        from datetime import datetime
        i=0
        Total='''<div class="isotherm_button">
        
        '''
        dictIsotherms=pd.DataFrame([],columns=["date","text"])
        for path in pathAll:
            myData=Monolayer(path+"_IMG.xlsx")
            myPath=path.split(".xslx")[0].split("Data/")[-1]
            pathImg=path.split("Data/")[-1]+".png"
            refButton='''<div class="overlay">

            '''
            img='<img src="./Data/'+pathImg+' class="button">'
            divBackground='''
            <div class="button">
            '''

            refButton+=img+divBackground+'<a href="./Data/'+myPath+'.html" class="button">'
            substance='<h2 class="button">%s</h2>' %(myData.param["Substance1"])
            textButton='V= %d ul [%.2f %s]<br>T= %d °C; speed= %.0f %s' %(
                                            myData.param["Volume1"],myData.param["Concentration1"],myData.param["Unit1"],
                                            myData.param["Temperature"],myData.param["Speed"],myData.param["Unit Speed"])
            date="Date: %s" %(myData.param["Date"].strftime("%d/%m/%Y"))
            finalButton=refButton+substance+"<br>"+date+"<br>"+textButton
            finalButton+='''</a>
                </div>
            </div>
            '''
            dictIsotherms=dictIsotherms.append({"date":myData.param["Date"],"text":finalButton},ignore_index=True)
        sortedKeys=dictIsotherms.sort_values("date",ascending=False)
        for index,row in sortedKeys.iterrows():
            Total=Total+row["text"]
        return Total+'</div>'

    def AppendAbs(pathAbs,myData,save):
    
        '''
            Need to have abs as sql
            If pathSave=None, return monolayer with all data. Else, save to excel

        '''
        import sqlite3

        if type(myData)==str:

            myData=Monolayer(myData)
        if "BamFile" in list(myData.data.columns):
            raise TypeError ("BamFile already append!")
        connection = sqlite3.connect(":memory:")
        cursor = connection. cursor()
        sql_file = open(pathAbs)
        sql_as_string = sql_file. read()
        sql_as_string=sql_as_string.replace("DROP TABLE","DROP TABLE IF EXISTS")
        cursor.executescript(sql_as_string)

        f=pd.read_sql("SELECT * FROM LBTr0Res",connection)
        f=f.rename(columns={"Time":"T[s]","Barrier":"Bpos[mm]"})
        f["T[s]"]=f["T[s]"].round(decimals=2)
        
        f["Bpos[mm]"]=f["Bpos[mm]"]*1e3        #Convert to mm
        f["Bpos[mm]"]=f["Bpos[mm]"].round(decimals=3)

        myData.data["Bpos[mm]"]=myData.data["Bpos[mm]"].round(decimals=3)
        myData.data["T[s]"]=myData.data["T[s]"].round(decimals=2)

        f=f[["T[s]","Bpos[mm]","BamFile"]]
        myData2=pd.merge(myData.data, f, how="outer", on=["T[s]","Bpos[mm]"])
        if len(myData2)!=len(myData.data):
            raise EnvironmentError("Unable to append files")

        myData.data=myData2

        if save!=None:
            myData.to_excel(save)

        else:
            return myData
    