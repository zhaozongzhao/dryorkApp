import unittest
import requests

class GetEventListTest(unittest.TestCase):
    '''查询发布会信息'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/get_event_list_sec/'

    def test_get_event_list_auth_null(self):
        '''auth为空'''
        r = requests.get(self.base_url,params={'eid':1})
        result = r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'user auth null')

    def test_get_event_list_auth_error(self):
        '''auth错误'''
        auth_user = ('abc','123')
        r = requests.get(self.base_url,auth =auth_user,params={'name':'红米1'})
        result = r.json()
        self.assertEqual(result['status'],10012)
        self.assertEqual(result['message'],'user auth fail')

    def test_get_event_list_eid_null(self):
        auth_user = ('admin2', 'zzz284117')
        r = requests.get(self.base_url, auth=auth_user, params={'name': ''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_list_eid_success(self):
        # auth_user = ('abmin2', 'zzz284117')
        # r = requests.get(self.base_url, auth=auth_user, params={'eid': 1})
        # result = r.json()
        auth_user = ('admin2', 'zzz284117')
        r = requests.get(self.base_url, auth=auth_user, params={'eid': 1})
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')












if __name__ == '__main__':
     unittest.main()