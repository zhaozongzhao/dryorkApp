from Common.DoExel import DoExcel
from Common.myrequest import myRquest
import os

de = DoExcel(os.getcwd().replace('TestCase','TestDatas')+'/api_qcd.xlsx')
all_case_datas = de.get_caseData_all()

for case_data in all_case_datas:
    res = myRquest(case_data['url'],case_data['method'],eval(case_data['request_data']))
    print(res.text)
    # assert  res.text == case_data['response_data']
