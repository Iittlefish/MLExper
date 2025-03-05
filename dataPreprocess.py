import os, pickle
import numpy as np
import pandas as pd

class DataProcesser:
    __filePath = []
    __data = None   

    def __init__(self):     #init new object. get all the file path of dataset
        self.__file = []
        self.__bassPath =""
        
        self.__file = [ "S"+str(i) for i in range(2,18) ]
        self.__file.remove("S12")
        self.__bassPath = os.path.join(os.path.dirname(__file__), 'WESAD')
        filePath = []
        for i in range(len(self.__file)):
            tempPath = os.path.join(self.__bassPath, str(self.__file[i]))
            tempPath = os.path.join(tempPath, str(self.__file[i]))
            tempPath = tempPath + ".pkl"
            filePath.append(str(tempPath))
            self.__filePath.append(str(filePath[i]))

    def __readFile(self):       #read WESAD file, get the data and concat to a dataframe
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
                signalData = temp[b"signal"]
                chest = signalData[b"chest"]
                tempList  = chest[b"ACC"].tolist()
                tempArry = np.array(tempList).T
                length = len(tempArry[0])
            tempData ={
                "ACC0": tempArry[0],
                "Acc1": tempArry[1],
                "ACC2": tempArry[2],
                "ECG": chest[b'ECG'].reshape(length,),
                "EMG": chest[b'EMG'].reshape(length,),
                "EDA": chest[b'EDA'].reshape(length,),
                "resp": chest[b'Resp'].reshape(length,),
                "temp": chest[b'Temp'].reshape(length,),
                "label": temp[b"label"].reshape(length,),
            }
            print(tempData)
            tempData = pd.DataFrame.from_dict(tempData)
            randomData = self.getRandomData(tempData)
            print(len(randomData))
            print(len(data))
            print("-------")
            data = pd.concat([data,randomData], ignore_index= 1)
        self.__data = pd.concat([self.__data,data], axis=1)
        print(len(self.__data))
        return  self.__data
    
    def getData(self):      #return dataset
        data = self.__readFile()
        self.__data = data
        return self.__data
    
    def __GroupByLabel(self, data):     #group the dataset by label
        df = data
        label = df.groupby("label")
        one = label.get_group(1)
        two = label.get_group(2)
        return[one, two]
    
    def getRandomData(self, data ):     #return sample and randon data
        groupData = self.__GroupByLabel(data)
        dataOne = groupData[0].sample(n=40, random_state= 3)
        dataTwo = groupData[1].sample(n=40, random_state= 3)
        randomData = pd.concat([dataOne,dataTwo],ignore_index=True)
        randomData = randomData.sample(80, random_state= 2)
        print(len(randomData))
        return randomData
    
    def toCsv(self):        #turn the WESAD file to the .CSV file, WESAD file is too big.
        if (type(self.__data) != pd.DataFrame):
            self.__readFile()
        self.__data.to_csv("./dataSet.csv")
    
    def toNpArray(self):    #turn the dataset to np array by read WESAD file.
        if (self.__data == None):
            self.__readFile()
        npArray = self.__data.to_numpy()
        return npArray
        


        






        
