#unittest  + ddt

from Common.DoExel import DoExcel
from Common.myrequest import myRquest
import os
import ddt
import unittest

de = DoExcel(os.getcwd().replace('TestCase', 'TestDatas') + '/1.xlsx')
all_case_datas = de.get_caseData_all()


@ddt.ddt
class TestData(unittest.TestCase):

    def setUp(self):
         pass

    def tearDown(self):
        pass

    @ddt.data(*all_case_datas)
    def test_api(self,case_data):
        res = myRquest(case_data['url'],case_data['method'],eval(case_data['request_data']))
        print(res.text)
        assert  res.text == case_data['response_data']

if __name__ == '__main__':
    unittest.main()