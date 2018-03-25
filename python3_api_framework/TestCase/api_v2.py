#unittest  + ddt

from Common.DoExel import DoExcel
from Common.myrequest import myRquest
import ddt,time,os,unittest
from Common.myLogger import MyLoggger
from Common.dir_config import *
logger = MyLoggger("zzz",log_dir+time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))+'.log')

#传入测试地址返回测试数据
path = casedata_dir +'/api_qcd.xlsx'
logger.info('测试数据地址'+str(path))
de = DoExcel(path,logger)
all_case_datas = de.get_caseData_all()



@ddt.ddt
class TestData(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        #执行结束，修改初始数据保证测试完成
        de.Modify_init_data()
        de.save_excel(path)

    def setUp(self):
        logger.info('开始执行')


    def tearDown(self):
        logger.info('执行结束')

    @ddt.data(*all_case_datas)
    def test_api(self,case_data):
        if case_data['request_data'] is not None:
          #eval中参数不能为None
          logger.info('发送请求'+str(case_data))
          res = myRquest(case_data['url'],case_data['method'],eval(case_data['request_data']))
          logger.info('返回数据'+str(res.text))
          if case_data['is_all'] == 0 :
              assert  res.text == case_data['response_data']
          else:
              self.assertIn( case_data['response_data'],res.text)
        else:
           logger.info('发送没有请求数据'+str(case_data))
           res = myRquest(case_data['url'],case_data['method'],request_data = None)
           logger.info('返回数据'+str(res.text))
           if case_data['is_all'] == 0 :
                assert  res.text == case_data['response_data']
           else:
                self.assertIn( case_data['response_data'],res.text)


if __name__ == '__main__':
    unittest.main()