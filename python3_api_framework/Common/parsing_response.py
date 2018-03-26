
#根据表达式，从响应结果中提取相应数据，并赋值给指点变量
def get_relatedData_from_response(resonseData,related_exp):
    '''
    :param resonseData 响应数据
    :param related_exp 提取表达式
    :return 返回提取的值
    '''
    if resonseData is None or resonseData == '':
        return
    if related_exp is None or related_exp == '':
        return
    #对第二个表达式进行分割
    temp = related_exp.split('=')
    print(temp[0])
    #将响应数据转化为字典
    data = eval(resonseData)
    keys_list = temp[1].split('.')
    res = get_data(data,keys_list)
    return {temp[0]:res}

#根据传入的表达式，从字典提取相关数据（列表中的额每一个数据都是字典中的key名）
def get_data(dicteobj,keys_list):
    value = dicteobj[keys_list[0]]
    if  len(keys_list) >1:
        keys_list = keys_list[1:]
        res = get_data(value,keys_list)
        return res

    return value

resonseData ='{"status":1,"code":"10001","data":{"id":1620,"regname":"æç©º","pwd":"E10ADC3949BA59ABBE56E057F20F883E","mobilephone":"18301565624","leaveamount":"100.00","type":"1","regtime":"2018-03-21 19:03:16.0"},"msg":"充值成功"}'
related_exp = '$user_id=data.id'


if __name__ == '__main__':
    res = get_relatedData_from_response(resonseData,related_exp)
    print(res)