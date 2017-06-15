# encoding=utf-8
import Image
import os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics, neighbors
from sklearn import svm
from sklearn.externals import joblib

#验证码识别 逻辑回归

def loadData():
    X=[]
    Y=[]
    for name in os.listdir("/home/drjr/Desktop/clearyzm/"):
        fn = "/home/drjr/Desktop/clearyzm/" + name
        img = Image.open(fn)
        arr= np.array(img.convert("L"))
        X.append(arr.flatten())
        Y.append(name[-2])
    return X,Y

model=LogisticRegression()
# model=svm.LinearSVC()
X,Y=loadData()
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.5, random_state=12)
model.fit(X_train,y_train)
predict=model.predict(X_test)
print(metrics.classification_report(y_test, predict))
# print metrics.confusion_matrix(y_test,predict)

joblib.dump(model,"../model/logic.pkl")
