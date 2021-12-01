import informixdb
import traceback
import sys
import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

conn = informixdb.connect('odbc_demodb@ol_gbasedbt10','gbasedbt','P@ssw0rd0LD')
cursor = conn.cursor()
cursor.execute('SELECT created FROM systables')
ret = cursor.fetchone()
print(ret)

