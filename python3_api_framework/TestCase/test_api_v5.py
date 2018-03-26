#unittest  + ddt

from Common.DoExel import DoExcel
from Common.myrequest import myRquest
import ddt,time,os,unittest
from Common.myLogger import MyLoggger
from Common.dir_config import *
from Common import parsing_response

logger = MyLoggger("zzz",log_dir+time.strftime('%Y-%m-%d %H%M',time.localtime(time.time()))+'.log')

#传入测试地址返回测试数据
path = casedata_dir +'/api_qcd.xlsx'
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
        logger.info('################################开始执行测试用例#######################')


    def tearDown(self):
        logger.info('################################执行测试结束#######################')

    @ddt.data(*all_case_datas)
    def test_api(self,case_data):
        logger.info('接口请求地址：{}'.format(case_data['url']))
        logger.info('接口请求类型：{}'.format(case_data['method']))
        logger.info('接口请求数据：{}'.format(case_data['request_data']))


        #eval中参数不能为Non
        res = myRquest(case_data['url'],case_data['method'],case_data['request_data'])
        logger.info('返回状态码：{}'.format(res.status_code))
        logger.info('接口返回数据：')
        logger.info(res.text)
        logger.info('接口请求期望数据：')
        #判断测试数据到当中，是否有关联字段，如果有，则需要提取出来，按表达式提取，并且赋值给指定变量
        if 'related_exp' in case_data.keys():
            logger.info('需要从响应结果中提取数据')
            res = parsing_response.get_relatedData_from_response(res.text,case_data['related_exp'])




        logger.info(case_data['response_data'])
        logger.info('期望结果与实际结果的比对方式：')
        if case_data['is_all'] == 0 :
            logger.info('全职匹配模式')
            try:
               assert  res.text == case_data['response_data']
               logger.info('结果比对成功，测试通过')
            except AssertionError:
                logger.info('结果匹配成功')
                raise  AssertionError
        else:
            logger.info('部分匹配模式')
            try:
                self.assertIn(case_data['response_data'], res.text)
                logger.info('结果比对成功，测试通过')
            except AssertionError:
                logger.info('结果匹配成功')
                raise AssertionError




if __name__ == '__main__':
    unittest.main()