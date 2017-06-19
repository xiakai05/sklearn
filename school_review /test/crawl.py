import requests
import time
import random

prefix="51370120140607"
url="http://xq.cdzk.net/CaptchaCode?w=78&h=31"
for i in range(3000):
    response=requests.get(url)
    if response.status_code==200:
        open("/home/drjr/Desktop/p/"+str(i),"wb").write(response.content)
    time.sleep(1)
