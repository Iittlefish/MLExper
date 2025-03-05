from dataPreprocess import DataProcesser


# get the dataset from WESAD and turn into .csv file
dp = DataProcesser()
data = dp.getData()
dp.toCsv()
