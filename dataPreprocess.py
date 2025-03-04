import os, pickle
import numpy as np
import pandas as pd

class DataProcesser:
    __filePath = "" 
    __data = None   

    def __init__(self):

        self.getFilePath()
        self.__readFile()
        
    def getFilePath(self):
        self.__file = []
        self.__bassPath =""
        tmpPath = ""

        self.__file = [ "S"+str(i) for i in range(2,18) ]
        self.__file.remove("S12")
        self.__bassPath = os.path.join(os.path.dirname(__file__), 'WESAD')

        for i in range(len(self.__file)):
            filePath = []
            tmpPath = os.path.join(self.__bassPath, str(self.__file[i]))
            tmpPath = os.path.join(tmpPath, str(self.__file[i])+".pkl")
            filePath.append(tmpPath)
        self.__filePath = filePath
        return self.__filePath

    def __readFile(self):
        label = [] 
        acc = []
        ecg = []
        emg = []
        eda = []
        resp = []
        temp = []
        column = [label, acc, ecg, emg, eda, resp, temp]
        for i in column:
            np.array(i)

        data = pd.DataFrame()
        for i in range(len(self.__filePath)):
            with open(self.__filePath[i], "rb") as f:
                temp = pickle.load(f, encoding="bytes")
                chest = temp[b"signal"][b"chest"]
                tempList  = chest[b"ACC"].tolist()
                tempArry = np.array(tempList).T
            tempData ={
                "ACC": chest[b'ACC'].tolist(),
                "ACC0": tempArry[0],
                "Acc1": tempArry[1],
                "ACC2": tempArry[2],
                "ECG": chest[b'ECG'].tolist(),
                "EMG": chest[b'EMG'].tolist(),
                "EDA": chest[b'EDA'].tolist(),
                "resp": chest[b'Resp'].tolist(),
                "temp": chest[b'Temp'].tolist(),
                "label": temp[b"label"].tolist(),
            }
            tempData = pd.DataFrame.from_dict(tempData)
            data = pd.concat([data,tempData],axis=1)
            data = self.__GroupByLabel(data)
            data = self.getRandomData(data)
            self.__data = data
            print(self.__data)

        return  self.__data
    
    def getData(self):
        return self.__data


    def getAllDataFrame(self):
        df = self.__readFile() 
        return df
    
    def __GroupByLabel(self, data):
        df = data
        label = df.groupby("label")
        one = label.get_group(1)
        two = label.get_group(2)
        return[one, two]
    
    def getRandomData(self, data ):
        dataOne = data[0].sample(n=40, random_state= 3)
        dataTwo = data[1].sample(n=40, random_state= 3)
        randomData = pd.concat([dataOne,dataTwo],ignore_index=True)
        randomDatadata = randomData.sample(80, random_state= 2)
        return randomDatadata
    
        


        






        
