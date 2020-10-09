import urllib.request
import base64
import os


#拍照
os.system("raspistill -o /home/pi/test/picture/test.jpg")

# 获取待测图片的base64码
f = open('/home/pi/test/picture/test.jpg', 'rb')
img = base64.b64encode(f.read())
img = str(img)
img1 = img.strip('b\'')
request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/tell_kouzhao"

params = "{\"image\":\"" + img1 + "\",\"top_num\":\"2\"}"

params = bytes(params, encoding="utf8")

access_token = '24.903690f9df31d12c07718d2eea7451b6.2592000.1597384527.282335-21369212'
request_url = request_url + "?access_token=" + access_token

request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(request)
content = response.read()

ending = 0

if content:
    #print(content)
    result = str(content,encoding='utf-8')
    data = eval(result)
    out = data["results"][0]["name"]    # 识别出的结果
    out1 = float(data["results"][0]["score"])
    if out == "kouzhao":
        if out1 > 0.8:
            ending = 1
        else:
            ending = 0
    else:
        ending = 0
fo = open("out.txt","w")
fo.write(str(ending))
fo.close()

#传输识别结果至平台
os.system("python3 data2cloud.py")

#执行传输
os.system("python transfer.py")


