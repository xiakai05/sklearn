import requests

prefix="51370120140607"
url="http://xq.cdzk.net/IDExist/"
for i in range(3000):
    s=str(i)
    s=s.zfill(4)
    fullStr=prefix+s
    param={"id":fullStr}
    response=requests.get(url,param)
    if(response.content=="true"):
        print fullStr
