import requests

def myRquest(url,method,request_data):
    #传入参数发送http请求
    if method == 'get':
         res = requests.get(url,request_data)
    elif method == 'post':
         res =  requests.post(url,data=request_data)
    else:
        print('没有数据')
    return  res
