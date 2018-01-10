import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from  test_pyrequest.db_fixture import test_data

#指定测试用例的为当前文件
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
    test_data.init_data()#初始化数据

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/'+now+'_resilt.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='客户管理系统接口测试报告',
        description = '实现示例'
    )
    runner.run(discover)
    fp.close()
