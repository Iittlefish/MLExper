from dataPreprocess import DataProcesser
from sklearn.model_selection import train_test_split

dp = DataProcesser()
data = dp.getData()
print(data)

label = data["label"]
data = data.drop("label", axis= 1)
xTrain, xTest, yTrain, yTest = train_test_split(data, label, test_size=0.2, random_state=302)