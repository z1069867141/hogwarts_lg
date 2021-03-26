import pymysql as pymysql

conn = pymysql.connect(user='akienadmin@akiensqlserver',
                       password='Zz54821348123',
                       database='demo',
                       host='akiensqlserver.mysql.database.azure.com')
print(conn)