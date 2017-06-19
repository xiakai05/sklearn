# encoding=utf-8
import Image
import os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics, neighbors
from sklearn import svm
from sklearn.externals import joblib

dir="/home/drjr/Desktop/sub/"
def loadData():
    X=[]
    Y=[]
    for name in os.listdir(dir):
        file=dir+name
        X.append(np.array(Image.open(file).convert("L")).flatten())
        Y.append(name[0])
    return X,Y

X,Y=loadData()
model=svm.LinearSVC()
# model=LogisticRegression()
xt,xs,yt,ys=train_test_split(X,Y,test_size=0.1, random_state=22)
model.fit(xt,yt)
pre=model.predict(xs)
print metrics.classification_report(ys,pre)
joblib.dump(model,"../model/svm.pkl")
