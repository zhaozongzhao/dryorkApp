import unittest
from HTMLTestRunner import HTMLTestRunner
from TestCase import test_api_v2
from Common import dir_config
import os


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTest(test_loader.loadTestsFromModule(test_api_v2))

    # html_report = dir_config.htmlreport+'/htmlTestReport/'
    html_report  = open(dir_config.report_dir+'result.html','wb')
    runner = HTMLTestRunner(html_report,title='Api test report')
    runner.run(test_suite)
