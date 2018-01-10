import unittest,requests,hashlib
from  time import time

class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_event_sign/'
        #app_key
        self.api_key = '123456'
        #当前时间
        now_time = time()
        self.client_time = str(now_time).split('.')[0]
        #sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_request_error(self):
        '''请求方式错误'''
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'request error')


    def test_add_event_sign_null(self):
        '''签名为空'''
        payload = {'eid': 13, 'name': '红米7', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42', 'time': self.client_time, 'sign': ''}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user sign null')


    def test_add_event_time_out(self):
        '''时间超出'''
        now_time = str(int(self.client_time)-61)
        payload = {'eid': 13, 'name': '红米7', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42', 'time': now_time, 'sign': 'abc'}

        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10013)
        self.assertEqual(result['message'], 'user sign timeout')


    def test_add_event_sign_error(self):
        '''签名错误'''
        payload = {'eid': 13, 'name': '红米7', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42', 'time': self.client_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10014)
        self.assertEqual(result['message'], 'user sign error')


    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid': 13, 'name': '红米7', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42','time':self.client_time,'sign':self.sign_md5}
        r = requests.post(self.base_url,data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')

