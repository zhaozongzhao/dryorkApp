import requests

#查询发布会的接口
url = 'http://127.0.0.1:8000/api/get_event_list/'
r = requests.get(url,params={'eid':1})
result = r.json()

#断言
assert result['status'] == 200
assert result['message'] == 'success'
assert result['data']['name'] == '小米发布会'
assert result['data']['address'] == '北京市朝阳区'
assert result['data']['start_time'] == '2017-12-24T05:51:58Z'