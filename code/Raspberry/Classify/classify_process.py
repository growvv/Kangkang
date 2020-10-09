import urllib
import base64

# 获取待测图片的base64码
f = open('../picture/test.jpg', 'rb')
img = base64.b64encode(f.read())
img = str(img)
img1 = img.strip('b\'')
request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/mygarbage"

params = "{\"image\":\"" + img1 + "\",\"top_num\":\"2\"}"

params = bytes(params, encoding="utf8")

access_token = '24.08f031c77a555d714fe82708488cfe84.2592000.1597397411.282335-19166676'
request_url = request_url + "?access_token=" + access_token

request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(request)
content = response.read()

ending = -1

if content:
    print(content)
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
print(ending)
