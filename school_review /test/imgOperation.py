import random
from PIL import Image
import matplotlib.pyplot as plt
import os

points=(5,20,35,50)
dir ="/home/drjr/Desktop/p/"
for name in os .listdir(dir):
    file=dir+name;
    img=Image.open(file)
    i = 0;
    for pit in points:
        subImg=img.crop((pit,0,pit+15,30))
        subName=name[i]+str(random.randint(100,999))
        subImg.save("/home/drjr/Desktop/sub/"+subName,"jpeg")
        i=i+1
def imgSplit(location):
    img = Image.open(location)
    i = 0;
    imgs=[]
    for pit in points:
        subImg = img.crop((pit, 0, pit + 15, 30))
        imgs.append(subImg)
    return imgs