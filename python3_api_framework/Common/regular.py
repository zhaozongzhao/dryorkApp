import re
resonseData ='{"status":1,"code":"10001","data":{"id":1620,"regname":"æç©º","pwd":"E10ADC3949BA59ABBE56E057F20F883E","mobilephone":"18301565624","leaveamount":"100.00","type":"1","regtime":"2018-03-21 19:03:16.0"},"msg":"充值成功"}'
related_exp = '$user_id=.*"id":(\d*).*'
temp = related_exp.split('=')
regular = temp[1]
print(regular)
id = re.findall(regular,resonseData)
print(id)