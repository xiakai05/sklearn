from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import BernoulliRBM
import  numpy as np
import Image
import os
from sklearn.model_selection import train_test_split
from sklearn import metrics, svm


def loadData():
    X,Y=[],[]
    for name in os.listdir("/home/drjr/Desktop/p/"):
        file="/home/drjr/Desktop/p/"+name;
        X.append(np.array(Image.open(file).convert("L")).flatten())
        Y.append(name)
    return X,Y
model=LogisticRegression()
X,Y=loadData()
xt,xs,yt,ys=train_test_split(X,Y,test_size=0.2, random_state=111)
model.fit(xt,yt)
pre=model.predict(xs)
metrics.classification_report(ys,pre)