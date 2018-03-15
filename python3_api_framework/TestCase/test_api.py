from Common.DoExel import DoExcel
from Common.myrequest import myRquest
import os
import ddt
import unittest


class TestData(unittest.TestCase):

    def setUp(self):
         pass

    @classmethod
    def setUpClass(cls):
        de = DoExcel(os.getcwd().replace('TestCase', 'TestDatas') + '/1.xlsx')
        cls.all_case_datas = de.get_caseData_all()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def test_api(self):
        for case_data in self.all_case_datas:
           res = myRquest(case_data['url'],case_data['method'],eval(case_data['request_data']))
           print(res.text)
           assert  res.text == case_data['response_data']

if __name__ == '__main__':
    unittest.main()