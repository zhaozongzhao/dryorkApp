import os

base_dir = os.path.split(os.path.realpath(__file__))[0].replace("Common","")

#日志目录
log_dir = base_dir + "Loger/"

#测试报告目录
report_dir = base_dir + "HtmlReport/"


#测试用例目录
casedata_dir = base_dir+'TestDatas/'
