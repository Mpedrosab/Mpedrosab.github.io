"""""
Created on Fri Apr 23 15:13:02 2021

@author: M. Pedrosa Bustos
"""


import sqlite3
import atexit
import pandas as pd
import json
import simplejson
#==============================================================================
# CLASS TO EDIT MONOLAYER DATABASE
#==============================================================================


class MonolayerDB():

    def __init__(self, path):

        self.path=path
        if path[-1]!="/":
            path=path+"/"

        self.pathParam=path+"ParamDB.json"
        self.pathData=path+"DataDB.json"


    def to_JSON(self,data):
        '''
            Saves parameters of each isotherm to JSON files

        '''   
        import datetime
        name=data.param["Name"]
        #data.param.pop("Name")
        if (isinstance(data.param["Date"], datetime.date) ):
            data.param["Date"]=data.param["Date"].strftime("%Y-%m-%d %H:%M:%S")
        parameters={name:data.param}
        #parameters=parameters.set_index("Name",drop=True)           #Uses the name as index of the pandas
           # data=data.replace({',': ';'}, regex=True)

        try:
            with open(self.pathParam) as data_file:
                dataOut = json.load(data_file)
        except:
            print("creating "+self.pathParam)
            dataOut={}

        dataOut[name]=parameters[name]
        with open(self.pathParam, 'w') as data_file:
            dataOut = simplejson.dump(dataOut, data_file, ignore_nan=True)


        #data.to_json(self.pathParam,orient="index")
        #print("Param Data saved to "+self.pathParam)
        if "Membrane" in data.param["Substance1"]:
            data.data["AreaPerMass"]=data.data["Area[cm^2]"]*1E2/(data.param["Volume1"]*1E-3*data.param["Concentration1"])
            x='['+','.join(["%.3f" %(a) for a in data.data['AreaPerMass']])+']'
            xParam="mm^2/mg"

        else:    
            x='['+','.join(["%.3f" %(a) for a in data.data['Mma[A^2/molec]']])+']'
            xParam='Mma[A^2/molec]'
        y='['+','.join(["%.3f" %(a) for a in data.data['SP[mN/m]']])+']'
        #data.data["BamFile"]=""
        img='['+','.join(["%s" %(a) for a in data.data["BamFile"]])+']'
        #print(x,y)

        dataValues={name:{
        "xData": x,
        "xParam":xParam,
        'yData': y,
        "yParam": "SP [mN/m]",
        'BAMimg': img}}


        #data=pd.DataFrame(data.data, index=[0])
        #dataValues=dataValues.set_index("Name",drop=True)           #Uses the name as index of the pandas
           # data=data.replace({',': ';'}, regex=True)

        try:
            with open(self.pathData) as data_file:
                dataOut = json.load(data_file)
        except:
            print("creating "+self.pathData)
            dataOut={}

        dataOut[name]=dataValues[name]
        with open(self.pathData, 'w') as data_file:
            dataOut = simplejson.dump(dataOut, data_file, ignore_nan=True)

        return

    def removeEntry(self,name):
        '''
            Only need to open DB and put name. Do not need to save later
        
        '''
        with open(self.pathParam) as data_file:
            data = json.load(data_file)
            data.pop(name)
        with open(self.pathParam, 'w') as data_file:
            data = json.dump(data, data_file)
        with open(self.pathData) as data_file:
            data = json.load(data_file)
            data.pop(name)
        with open(self.pathData, 'w') as data_file:
            data = json.dump(data, data_file)

        return
        
    def ReadSQL_ABSFormat(self,datapath):
        connection = sqlite3.connect(":memory:")
        cursor = connection. cursor()
        sql_file = open(datapath)
        sql_as_string = sql_file. read()
        sql_as_string=sql_as_string.replace("DROP TABLE","DROP TABLE IF EXISTS")
        cursor.executescript(sql_as_string)
        

    def DataToPandas(self,dataTable,path=None):
        if path is None:
            path=self.path
        if path[-1]!="/":
            path=path+"/"
        with open(path+dataTable) as data_file:
            data = json.load(data_file)
        data=pd.DataFrame.from_dict(data,orient="index")
        #data=pd.read_sql_query("SELECT * FROM %s" %(dataTable), self.con)
        return data

    def SQLtoExcel(self,path,dataTable):
        data=self.DataToPandas(path+"/"+dataTable)

        data.to_excel(path)
        print("Data saved to "+path)
        return
#from monolayerDBClass import *
#print ("h")