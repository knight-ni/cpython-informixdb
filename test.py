import informixdb
import traceback
import sys

conn = informixdb.connect('odbc_demodb@ol_gbasedbt10','gbasedbt','P@ssw0rd0LD')
cursor = conn.cursor()
cursor.execute('SELECT tabname11 FROM systables')
ret = cursor.fetchall()
print(ret)
