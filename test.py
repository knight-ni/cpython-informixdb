# -*- coding: utf-8 -*-
import informixdb
import io
import os
import sys
import json
import numpy as np
import datetime

coding = 'utf-8'

def test():
    import informixdb
    conn = informixdb.connect('odbc_demodb@ol_gbasedbt10','gbasedbt','P@ssw0rd0LD')
    conn.autocommit = 1  # WE NEED THIS FOR DDL TX COMMIT
    print(type(conn))
    cursor = conn.cursor()
    cursor.execute("drop table if exists ifxdbtest;")
    stmt_list = ['create table ifxdbtest(']
    stmt_list.append('uid integer')
    stmt_list.append(',uname varchar(100)')
    stmt_list.append(',udate date')
    stmt_list.append(',udatetime datetime year to fraction(5)')
    stmt_list.append(',ufloat float')
    stmt_list.append(',udecimal decimal(12,3)')
    stmt_list.append(',utext text')
    stmt_list.append(',uclob clob')
    stmt_list.append(',ubyte byte')
    stmt_list.append(',ublob blob')
    stmt_list.append(',primary key (uid)')
    stmt_list.append(') put ublob in (')
    stmt_list.append('sbdbs')
    stmt_list.append(');')
    stmt = ''.join(stmt_list)
    print(stmt)
    cursor.execute(stmt)

    stmt_list = ['insert into ifxdbtest(']
    stmt_list.append('uid')
    stmt_list.append(',uname')
    stmt_list.append(')')
    stmt_list.append(' values(?')
    stmt_list.append(',?')
    stmt_list.append(')')
    stmt = ''.join(stmt_list)

    print(stmt)
    params = []
   
    uid = int(666)
    params.append(uid)

    uname = '卡布达'
    params.append(uname)

    cursor.prepare(stmt)
    ret = cursor.execute(None,params)
    print('Rows Affected:' + str(ret))
  
    stmt = "select * from ifxdbtest"
    cursor.execute(stmt)
    colno = len(cursor.description)
    print('Column Number:' + str(colno))
    print('')

    for r in cursor.description:
        print("Name:" + r[0] + "\t", end='')
        print("Type:" + r[1] + "\t", end='')
        print("Xid:" + str(r[2]) + "\t", end='')
        print("Length:" + str(r[3]) + "\t", end='')
        print("Nullable:" + str(r[6]))
    ret = cursor.fetchall()
    #print(type(ret[0][0]))
 
    
    conn.close()
    sys.exit(0)

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    test()


