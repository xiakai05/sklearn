import random
from PIL import Image
import matplotlib.pyplot as plt
import os

points=(5,20,35,50)
dir ="/home/drjr/Desktop/p/"
for name in os .listdir(dir):
    file=dir+name;
    img=Image.open(file)
    for pit in points:
        i=0;
        subImg=img.crop((pit,0,pit+15,30))
        subName=name[i]+str(random.randint(100,999))
        subImg.save("/home/drjr/Desktop/sub/"+subName,"jpeg")
        i=i+1
