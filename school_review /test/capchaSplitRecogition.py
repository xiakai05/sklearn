import Image
import os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics, neighbors
from sklearn import svm
from sklearn.externals import joblib
import matplotlib.pyplot as plt



points=(5,20,35,50)
def imgSplit(location):
    img = Image.open(location)
    i = 0;
    imgs=[]
    for pit in points:
        subImg = img.crop((pit, 0, pit + 15, 30))
        imgs.append(subImg)
    return imgs

model=joblib.load("../model/svm.pkl")
for name in os.listdir("/home/drjr/Desktop/yzm/"):
    file="/home/drjr/Desktop/yzm/"+name
    img1,img2,img3,img4= imgSplit(file)



    X=[]
    for img in (img1,img2,img3,img4):
        X.append(np.array(img.convert("L")).flatten())
    print name+","+str(model.predict(X))



