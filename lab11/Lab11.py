# coding=utf-8
# 雲林縣社區整體照顧服務體系C級單位
# 	https://ws.yunlin.gov.tw/001/Upload/539/opendata/0/1823/7662b5e1-13d9-4ffb-8082-acabb2b5378c.json

import pymysql.cursors
import requests
import json


test = requests.get("https://ws.yunlin.gov.tw/001/Upload/539/opendata/0/1823/7662b5e1-13d9-4ffb-8082-acabb2b5378c.json")
r = json.loads(test.text)

try:
    connection = pymysql.connect(host='192.168.137.165',
                                 user='E94124028',
                                 password='093366',
                                 database='wordpress',    
                                 cursorclass=pymysql.cursors.DictCursor)
    print("連線成功")
except Exception as error:
    print(error)


with connection: #build connection
    with connection.cursor() as cursor: #recive data

        sql = "INSERT INTO `雲林縣社區整體照顧服務體系C級單位` (`序號`, `所屬鄉鎮市`, `據點單位名稱`, `服務地址`, `類型`) VALUES (%s, %s, %s, %s, %s)" #bulid index
        for i in range( len( r ) ):
            cursor.execute(sql, (r[i]['序號'], r[i]['所屬鄉鎮市'],r[i]['據點單位名稱'],r[i]['服務地址'],r[i]['類型']))

    connection.commit()
    cursor.close()