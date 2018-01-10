import  unittest
import requests
import os,sys
from test_pyrequest.db_fixture import  test_data

class AddEventTest(unittest.TestCase):
    '''添加发布会'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_event/'

    def tearDown(self):
        pass

    def test_add_event_all_null(self):
        '''所有参数都为空'''
        payload  = {'eid':'','name':'','limit':'','status':'','address':'=',
                   'start_time':'='}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')

    def test_add_even_eid_exist(self):
        '''id 已经存在'''
        payload = {'eid': 1, 'name': '红米6', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        print(r.json())
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'event id already exists')

    def test_add_even_name_exist(self):
        '''名称已经存在'''
        payload = {'eid': 8, 'name': '红米1', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10023)
        self.assertEqual(self.result['message'],'event name already exists')


    def test_add_even_data_type_error(self):
        '''日期格式错误'''
        payload = {'eid': 8, 'name': '红米7', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],10024)
        self.assertEqual(self.result['message'],'start_time 格式错误')


    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid': 11, 'name': '红米7', 'limit': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42'}
        print(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')

if __name__ == '__main__':
    #test_data.init_data()
    unittest.main()