import os, pickle
import numpy as np
import pandas as pd

class DataProcesser:
    __filePath = "" 
    __data = None   

    def __init__(self):

        self.getFilePath()
        self.__readFile()
        self.getAllData()
        self.__GroupByLabel()
        self.getRandomData()
    
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

        for i in range(len(self.__filePath)):
            with open(self.__filePath[i], "rb") as f:
                tmp = pickle.load(f, encoding="bytes")
                chest = tmp[b"signal"][b"chest"]
            data ={
                "ACC": chest[b'ACC'].tolist(),
                "ECG": chest[b'ECG'].tolist(),
                "EMG": chest[b'EMG'].tolist(),
                "EDA": chest[b'EDA'].tolist(),
                "resp": chest[b'Resp'].tolist(),
                "temp": chest[b'Temp'].tolist(),
                "label": tmp[b"label"].tolist(),
            }
            #print(len(data))
            print("wating...")
            self.__data = data
        return  self.__data

    def getAllData(self):
        self.__data = self.__readFile()
        return self.__data

    def getAllDataFrame(self):
        df = pd.DataFrame.from_dict(data=self.__data)
        return df
    
    def __GroupByLabel(self):
        df = self.getAllData()
        df = self.getAllDataFrame()
        label = df.groupby("label")
        one = label.get_group(1)
        two = label.get_group(2)
        return(one, two)
    def getRandomData(self):
        dataOne, dataTwo = self.__GroupByLabel()
        dataOne = dataOne.sample(n=40, random_state= 3)
        dataTwo = dataTwo.sample(n=40, random_state= 3)
        data = pd.concat([dataOne,dataTwo],ignore_index=True)
        data = data.sample(80, random_state= 2)
        return data
    
    #def random40Data(self):
    #    data = self.__get40Data()
        


        






        
