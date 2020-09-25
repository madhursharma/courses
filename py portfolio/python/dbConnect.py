# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:47:56 2020

@author: msharma
"""

import mariadb
import sys

class DBConnection:
    _dbconn = None
    
    def __init__(self):
        self._dbconn = None
        
    
    def getConnection(self):
        if not self._dbconn:
            self._dbconn = self.__connect__()
        return self._dbconn
    
        
    def __connect__(self):
        try:
            conn = mariadb.connect(
                user="root",
                password="hereY0uG0!",
                host="ubu2",
                port=3306)
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return None
    
    
    def run(cur, sql):
    
        if(cur != None):
            return cur.execute(sql)
    
    def print(cur):
    
        for row in cur:
            print(row)



db = DBConnection()
conn = db.getConnection()


if not conn is None:
    cur = conn.cursor()
    ## Get Databases
    print("SHOW Databases")
    rows = cur.execute("SHOW DATABASES")
    
    for row in cur:
        print(row)
        
    ##print(cur)
    
    cur.execute("USE erdm")
    cur.execute("SHOW TABLES")
    for row in cur:
        print(row)
   
    print("Get contents of test_contacts")
    cur.execute("select * from test_contacts")
    for row in cur:
       print (row)

#conn.commit()
conn.close()
print("connection close")