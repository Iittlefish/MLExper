from dataPreprocess import DataProcesser


# get the dataset from WESAD and turn into .csv file
dp = DataProcesser()
data = dp.getData()
dp.toCsv()




#data = pd.read_csv("./dataSet.csv")
'''
data = data.drop("label", axis= 1)
xTrain, xTest, yTrain, yTest = train_test_split(data, label, test_size=0.2, random_state=302)

model = AdaBoostClassifier(random_state=304, learning_rate= 0.8)
model.fit(xTrain, yTrain)
model.predict(xTest, yTest)
'''