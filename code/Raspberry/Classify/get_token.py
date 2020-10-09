# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ZN1Q0HhRmkUieMqyl5aEVetv&client_secret=MX3oCU4NMMrnyR0UKDCCuN9mop2qUsgc'
response = requests.get(host)
if response:
    print(response.json())