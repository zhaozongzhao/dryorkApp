import requests
import unittest

class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/get_event_list/'

    def test_get_event_null(self):
        '''发布会id为空'''
        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')

    def test_get_even_error(self):
        '''发布会id不存在'''
        r = requests.get(self.url,params={'eid':'5'})
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],'query result is empty')

    def test_get_event_success(self):
        '''发布会id为1'''
        r = requests.get(self.url,params={'eid':1})
        result = r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')
        self.assertEqual(result['data']['name'] ,'小米发布会')
        self.assertEqual(result['data']['address'] , '北京市朝阳区')
        self.assertEqual(result['data']['start_time'] , '2017-12-24T05:51:58Z')

if __name__ == '__main__':
    #获取TestSuit实例化对象
    suite = unittest.TestSuite()
    #将测试用例添加到容器中
    suite.addTest(GetEventListTest('test_get_event_null'))
    suite.addTest(GetEventListTest('test_get_even_error'))
    suite.addTest(GetEventListTest('test_get_event_success'))
    #创建执行的TextTestRunner类实例化对象
    runner = unittest.TextTestRunner()
    runner.run(suite)
