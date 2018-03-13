import requests

def myRquest(url,method,request_data):
    if method == 'get':
         print('请求参数',url,method,type(request_data),request_data)
         res = requests.get(url,request_data)
    elif method == 'post':
         res =  requests.post(url,data=request_data)
    else:
        print('没有数据')
    return  res
