from suds.client import Client

url = 'http://localhost:7080/webservices/WebServiceTestBean?wsdl'
client = Client(url)


#使用库 suds_jurko : https://bitbucket.org/jurko/suds
# #web dervers 查询 :http：//www.webxml.com.cn/zh_cn/web_services.aspx
#
# #电话号码查询
# url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
# client = client(url)
# print(client)