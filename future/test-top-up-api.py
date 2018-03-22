import requests
import unittest

class GetTopUpTest(unittest.TestCase):
    '''前程贷注册接口测试'''
    def setUp(self):
        self.url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'

    def tearDown(self):

    def test_topup_success(self):
        '''功能验证'''
        data = {'mobilephone':'18301565568','amount':'100'}
        r = requests.post(self.url,data=data)
        print(r.text)

    def test_mobilephone_null(self):
        '''手机号为空'''
        data = {'mobilephone':'','amount':'100'}
        r = requests.post(self.url,data=data)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20103')
        self.assertEqual(result['msg'],'手机号不能为空')

    def test_amount_null(self):
        '''金额为空'''
        data = {'mobilephone':'18301565568','amount':''}
        r = requests.post(self.url,data=data)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20115')
        self.assertEqual(result['msg'],'请输入金额')

    def test_mobilephone_error(self):
        '''手机格式错误'''
        data = {'mobilephone':'18301565','amount':'10'}
        r = requests.post(self.url,data=data)
        result = r.json()
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20109')
        self.assertEqual(result['msg'],'手机号码格式不正确')

    def test_mobilephone_error1(self):
        '''手机号不存在'''
        data = {'mobilephone':'12345678911','amount':'10'}
        r = requests.post(self.url,data=data)
        result = r.json()
        print(result)
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20104')
        self.assertEqual(result['msg'],'此手机号对应的会员不存在')

    def test_amount_error(self):
        '''输入金额的金额小数大于两位'''
        data = {'mobilephone':'18301565568','amount':'0.0001'}
        r = requests.post(self.url,data=data)
        result = r.json()
        print(result)
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20116')
        self.assertEqual(result['msg'],'输入金额的金额小数不能超过两位')

    def test_amount_error2(self):
        '''输入金额的金额小数0'''
        data = {'mobilephone':'18301565568','amount':'-1'}
        r = requests.post(self.url,data=data)
        result = r.json()
        print(result)
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20117')
        self.assertEqual(result['msg'],'请输入范围在0到50万之间的正数金额')


    def test_amount_error3(self):
        '''输入金额的金额非数字'''
        data = {'mobilephone':'18301565568','amount':'hshsh'}
        r = requests.post(self.url,data=data)
        result = r.json()
        print(result)
        self.assertEqual(result['status'],0)
        self.assertEqual(result['code'],'20118')
        self.assertEqual(result['msg'],'请输入数字')


if __name__ == '__main__':
  unittest.main()