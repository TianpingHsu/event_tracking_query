#!/usr/bin/python3

import pymysql

# connect a database
db = pymysql.connect(host='172.25.11.125', user='client', password='Qnsz@2022', database='sd_dataserver')

cursor = db.cursor()

#https://alpha-test.oi.plus/api/log/dot/query/{tracdId}

sql = """SELECT * FROM sd_log_dot_record WHERE dot_key="createMeeting";"""

cursor.execute(sql)

results = cursor.fetchall()
for item in results:
    print(item)

# close db
db.close()
