from openpyxl import load_workbook
import os
class DoExcel:

    def __init__(self,excelpath):
        wb = load_workbook(excelpath)
        self.sh_case_data  = wb["case_data"]

    def get_caseData_all(self):
        all_case_datas = []
        for index in range(2,self.sh_case_data.max_row+1):
            case_data = {}
            case_data['id'] = self.sh_case_data.cell(row=index,column=1).value
            case_data['method'] = self.sh_case_data.cell(row=index, column=5).value
            case_data['url'] = self.sh_case_data.cell(row=index, column=6).value
            case_data['request_data'] = self.sh_case_data.cell(row=index, column=7).value
            case_data['response_data'] = self.sh_case_data.cell(row=index, column=8).value
            all_case_datas.append(case_data)
        return all_case_datas

if __name__ == '__main__':

  de = DoExcel(os.getcwd().replace('TestCase','TestDatas')+'/api_qcd.xlsx')
  all_case_datas = de.get_caseData_all()
  print(all_case_datas)