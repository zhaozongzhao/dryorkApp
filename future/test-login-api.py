import requests
import unittest

class GetLoginTest(unittest.TestCase):
    '''前程贷登陆接口测试'''

    def setUp(self):
        self.url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'

    def test_login_success(self):
        '''功能验证'''
        params = {'mobilephone':'18301565568','pwd':'123456'}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],1)
        self.assertEqual(result['code'],'10001')
        self.assertEqual(result['msg'],'登录成功')

    def test_pwd_error(self):
        '''密码错误'''
        params = {'mobilephone':'18301565568','pwd':'12345'}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20111')
        self.assertEqual(result['msg'],'用户名或密码错误')

    def test_user_error(self):
        '''用户名错误'''
        params = {'mobilephone':'183015655','pwd':'123456'}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20111')
        self.assertEqual(result['msg'],'用户名或密码错误')

    def test_phone_null(self):
        '''用户名为空'''
        params = {'mobilephone':'','pwd':'123456'}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20103')
        self.assertEqual(result['msg'],'手机号不能为空')

    def test_pwd_null(self):
        '''密码为空'''
        params = {'mobilephone':'18301565568','pwd':''}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20103')
        self.assertEqual(result['msg'],'密码不能为空')

    def test_user_pwd_null(self):
        '''用户名密码都为空'''
        params = {'mobilephone':'','pwd':''}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20103')
        self.assertEqual(result['msg'],'手机号不能为空')

    def test_pwd_error2(self):
        '''用户名密码都为空'''
        params = {'mobilephone':'','pwd':''}
        r = requests.get(self.url,)
        result = r.json()
        print(result)
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20103')
        self.assertEqual(result['msg'],'手机号不能为空')


if __name__ == '__main__':
    unittest.main()