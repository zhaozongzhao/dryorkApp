import requests

#查询发布会的接口
url = 'http://127.0.0.1:8000/api/get_event_list_sec/'
auth_user = ('admin2','zzz284117')
r = requests.get(url,auth = auth_user,params={'eid':1})
result = r.json()
print(result)

#断言
assert result['status'] == 200
assert result['message'] == 'success'
