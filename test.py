# -*- coding: utf-8 -*-
import io
import os
import sys
import json
import numpy as np
import datetime
import decimal

coding = 'utf-8'

def test():
    import informixdb
    conn = informixdb.connect('odbc_demodb@ol_gbasedbt10','gbasedbt','P@ssw0rd0LD')
    conn.autocommit = 1  # WE NEED THIS FOR DDL TX COMMIT
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
    stmt_list.append(',udate')
    stmt_list.append(',udatetime')
    stmt_list.append(',ufloat')
    stmt_list.append(',udecimal')
    stmt_list.append(',utext')
    stmt_list.append(',uclob')
    stmt_list.append(',ubyte')
    stmt_list.append(',ublob')
    stmt_list.append(')')
    stmt_list.append(' values(?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(',?')
    stmt_list.append(')')
    stmt = ''.join(stmt_list)

    print(stmt)
    params = []
   
    uid = int(666)
    params.append(uid)

    uname = '卡布达'
    params.append(uname)

    udate = datetime.date(2021,12,3)
    params.append(udate)

    udatetime = datetime.datetime.now()
    params.append(udatetime)

    ufloat = float(514.123)
    params.append(ufloat)

    udecimal = decimal.Decimal('123123.412')
    params.append(udecimal)

    with open('/etc/passwd', 'rb') as f:
        utext = f.read()
    params.append(utext)

    uclob = conn.Sblob(1)   # DEFINED IN SOURCE FILE
    with open('/etc/services', 'r') as f:
        uclob.write(f.read())
    uclob.close()
    params.append(uclob)

    with open('./cat.jpg', 'rb') as f:
        ubyte = f.read()
    params.append(ubyte)

    ublob = conn.Sblob(0)    # DEFINED IN SOURCE FILE
    with open('./cat.jpg', 'rb') as f:
        ublob.write(f.read())
    ublob.close()
    params.append(ublob)

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

    print('')

    lobbuf_size=int(4096)
    for row in ret:
        for idx,col in enumerate(row):
            type = cursor.description[idx][1]
            if(type == 'text'):
                with open('./text_passwd', 'wb') as f:
                    f.write(col)
            elif (type == 'byte'):
                with open('./byte_cat.jpg', 'wb') as f:
                    f.write(col)
            elif(cursor.description[idx][1] == 'fixed udt \'clob\''):
                col.open()
                with open('./clob_services', 'wb') as f:
                    while (1):
                        buf=col.read(lobbuf_size)
                        if(buf):
                            f.write(buf)
                        else:
                            break
                col.close()
            elif (cursor.description[idx][1] == 'fixed udt \'blob\''):
                col.open()
                with open('./blob_cat.jpg', 'wb') as f:
                    while (1):
                        buf=col.read(lobbuf_size)
                        if(buf):
                            f.write(buf)
                        else:
                            break
                col.close()
            else:
                print(col)
    
    conn.close()
    sys.exit(0)

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    test()


