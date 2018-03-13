from Common.DoExel import DoExcel
from Common.myrequest import myRquest
import os

de = DoExcel(os.getcwd().replace('TestCase','TestDatas')+'/api_qcd.xlsx')
all_case_datas = de.get_caseData_all()
print('所有数据',all_case_datas)
for case_data in all_case_datas:
    print('循环数据',case_data)
    res = myRquest(case_data['url'],case_data['method'],eval(case_data['request_data']))
    print('响应值',res.text)