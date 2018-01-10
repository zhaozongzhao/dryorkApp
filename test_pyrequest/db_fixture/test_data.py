import sys
sys.path.append('../db_fixture')
from  test_pyrequest.db_fixture.mysql_db import DB

#创建测试数
datas = {
    #发布会数据
    "sign_event":[{'id':1,'name':'红米1','`limit`':2000,'status':1,'address':'北京会展中心',
                   'start_time':'2016-08-20 00:25:42','create_time':'2018-02-20 00:25:42'},
                  {'id': 2, 'name': '红米2', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42','create_time':'2018-02-20 00:25:42'},
                  {'id': 3, 'name': '红米3', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42','create_time':'2018-02-20 00:25:42'},
                  {'id': 4, 'name': '红米3note', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42','create_time':'2018-02-20 00:25:42'},
                  {'id': 5, 'name': '红米4', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42','create_time':'2018-02-20 00:25:42'},
                  {'id': 6, 'name': '红米5', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
                   'start_time': '2016-08-20 00:25:42','create_time':'2018-02-20 00:25:42'}],
   #嘉宾表数据
    "sign_guest":[{'realneme':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'event_id':1,
                   'cread_time': '2018-02-20 00:25:42'},
                  {'realneme': '老王', 'phone': 12312341235, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1,
                   'cread_time': '2018-02-20 00:25:42'},
                  {'realneme': '老李', 'phone': 12312341236, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 2,
                   'cread_time': '2018-02-20 00:25:42'},
                  {'realneme': '老毛', 'phone': 12312341237, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 5,
                   'cread_time': '2018-02-20 00:25:42'},
                  {'realneme': '老赵', 'phone': 12312341238, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 5,
                   'cread_time': '2018-02-20 00:25:42'}]

}

#将测试数据插入表
def init_data():
    db = DB()
    for tablename,data in datas.items():
        db.clear(tablename)
        for d in data:
            db.inster(tablename,d)
    db.close()

if __name__ == '__main__':
    init_data()