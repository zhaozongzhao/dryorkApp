#unittest  + ddt

from Common.DoExel import DoExcel
from Common.myrequest import myRquest
import os
import ddt
import unittest
from Common import Log
#传入测试地址返回测试数据
path =os.path.split(os.path.realpath(__file__))[0].replace('TestCase', 'TestDatas') + '/api_qcd.xlsx'
print(path)
de = DoExcel(path,log=Log)
all_case_datas = de.get_caseData_all()


@ddt.ddt
class TestData(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        #执行结束，修改初始数据保证测试完成
        de.Modify_init_data()
        de.save_excel(path)

    def setUp(self):
         pass

    def tearDown(self):
        pass

    @ddt.data(*all_case_datas)
    def test_api(self,case_data):
        res = myRquest(case_data['url'],case_data['method'],eval(case_data['request_data']))
        print(res.text)
        if case_data['is_all'] == 0 :
           assert  res.text == case_data['response_data']
        else:
           self.assertIn( case_data['response_data'],res.text)

if __name__ == '__main__':
    unittest.main()