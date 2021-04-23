import pymysql as pymysql

conn = pymysql.connect(user='akienadmin@akiensqlserver',
                       password='Zz54821348123',
                       database='demo',
                       host='akiensqlserver.mysql.database.azure.com',
                       ssl_ca='D:\\ssl_for_example\\BaltimoreCyberTrustRoot.crt.pem')

print(conn.get_server_info())

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

conn.close()