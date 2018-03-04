#!/usr/bin/env python

import pymysql
import sys
print(sys.version)

print "hello peter mera"
connection = pymysql.connect(host='192.168.1.103',
                             user='peter',
                             password='Peter_Th',
                             db='test_ais',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print ("connect successful!!")

try:


    with connection.cursor() as cursor:

        # SQL
        sql = "SELECT mmsi,	Report_date, ipsender FROM position_report where Report_date > (now() - interval 3 hour) order by Report_date desc"

        # Execute query.
        cursor.execute(sql)

        print ("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)

finally:
    # Close connection.
    connection.close()
