import requests
import unittest

class GetRegisteredTest(unittest.TestCase):
    '''前程贷注册接口测试'''
    def setUp(self):
        self.url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'

    def test_registered_success(self):
        '''功能验证'''
        params = {'mobilephone':'18301565568','pwd':'123456','regname':'星空'}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],1)
        self.assertEqual(result['code'],'10001')
        self.assertEqual(result['msg'],'注册成功')

    def test_mobilephone_null(self):
        '''手机号码为空'''
        params = {'mobilephone':'','pwd':'123456','regname':'星空'}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20103')
        self.assertEqual(result['msg'],'手机号不能为空')

    def test_pwd_null(self):
        '''密码为空'''
        params = {'mobilephone':'18301565568','pwd':'','regname':'星空'}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20103')
        self.assertEqual(result['msg'],'密码不能为空')

    def test_regname_null(self):
        '''注册名为空'''
        params = {'mobilephone':'18301565567','pwd':'123456','regname':''}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],1)
        self.assertEqual(result['code'],'10001')
        self.assertEqual(result['msg'],'注册成功')

    def test_registered_repeat(self):
        '''重复注册认证'''
        params = {'mobilephone':'18301565567','pwd':'123456','regname':''}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20110')
        self.assertEqual(result['msg'],'手机号码已被注册')

    def test_mobilephone_format(self):
        '''手机格式验证'''
        params = {'mobilephone':'183015655','pwd':'123456','regname':''}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20109')
        self.assertEqual(result['msg'],'手机号码格式不正确')

    def test_pwd_length(self):
        '''密码长度验证'''
        params = {'mobilephone':'183015655','pwd':'123','regname':''}
        r = requests.get(self.url,params=params)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20108')
        self.assertEqual(result['msg'],'密码长度必须为6~18')



if __name__ == '__main__':
  unittest.main()