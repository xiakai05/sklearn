import Image
import os
import numpy as np
from sklearn.externals import joblib

X=[]
Y=[]
for name in os.listdir("/home/drjr/Desktop/p/"):
    s="/home/drjr/Desktop/p/"+name
    img=Image.open(s)
    X.append(np.array(img.convert("L")).flatten())
    Y.append(name[-2])
model=joblib.load("../model/logic.pkl")
print model.predict(X)
print Y
