import unittest
from HTMLTestRunner import HTMLTestRunner
from TestCase import test_api_v5
from Common import dir_config
import os
import time


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTest(test_loader.loadTestsFromModule(test_api_v5))
    filename  = dir_config.report_dir +time.strftime('%Y-%m-%d',time.localtime(time.time()))+'_report.html'
    html_report  = open(filename,'wb')
    runner = HTMLTestRunner(html_report,title='Api test report')
    runner.run(test_suite)
