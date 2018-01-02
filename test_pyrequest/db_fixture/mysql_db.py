from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
import pymysql.cursors

#---------------------读取配置文件中的信息————————————
#获取当前目录
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
#配置文件的path
file_path = base_dir + '/db_config.ini'

#直接读取文件内容
cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db   = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


#======================================================封装mysql的基本操作=============================================
class DB:
    def __init__(self):
        try:
            #连接数据库
            self.conn = connect(host =host,
                                user = user,
                                password = password,
                                db = db,
                                charset = 'utf8mb4',
                               # cursorcalss = cursors.DictCursor
                                cursorclass = pymysql.cursors.DictCursor
                                 )
        except OperationalError as e:
            print('mysql error %d %s'%(e.args[0],e.args[1]))


    #清除表数据
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.conn.commit()


    #插入表数据
    def inster(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = 'INSERT INTO'+table_name+'('+key+')VALUES('+value+")"
        print(real_sql)
        with self.conn.cursor() as cursors:
            cursors.execute(real_sql)
        self.conn.commit()

    #关闭数据库
    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = DB()
    table_name = "sign_event"
    data = {'id': 1, 'name': '红米', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
            'start_time': '2018-02-20 00:25:42'}
    table_name2 = "sign_guest"
    data2 = {'realname': 'alen', 'phone': 12312341234, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1}

    db.clear(table_name)
    db.inster(table_name,data)
    # db.close()