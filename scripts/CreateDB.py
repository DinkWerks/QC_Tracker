import sqlite3

import os
import platform

sys = platform.system()
folder = os.getcwd()
shortdir = folder[:-7:]
if sys == 'Darwin':
    longdir = shortdir + 'db/test.db'
elif sys == 'Window':
    longdir = shortdir + 'db\test.db'
else:
    print 'Failed to find database directory.'

conn = sqlite3.connect(longdir)
cursor = conn.cursor()


def create_rsrc_tbl():
    cursor.execute(
        "CREATE TABLE resources(ID INTEGER PRIMARY KEY AUTOINCREMENT, QuadID INTEGER, PriNum TEXT, Trinomial TEXT, "
        "DBCheck integer, DBUsrID integer, DBDate TEXT, PDFCheck integer, PDFUsrID integer, PDFDate TEXT, "
        "GISCheck integer, GISUsrID integer, GISDate TEXT, Missing integer, Voided integer, "
        "GISSizeINC integer, GISShapeINC integer, GISLocINC integer, GISDupe integer, GISOther integer, Note TEXT)")


def insert_resource(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
    cursor.execute("INSERT INTO "
                   "resources (QuadID,PriNum,Trinomial,DBCheck,DBUsrID,DBDate,PDFCheck,PDFUsrID,PDFDate,"
                   "GISCheck,GISUsrID,GISDate,Missing,Voided,"
                   "GISSizeINC,GISShapeINC,GISLocINC,GISDupe,GISOther,Note)"
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t))


def create_user_tbl():
    cursor.execute("CREATE TABLE users(ID INTEGER PRIMARY KEY AUTOINCREMENT, Signature TEXT, UsrName TEXT)")


def add_user(a, b):
    cursor.execute("INSERT INTO users (Signature,UsrName) VALUES (?, ?)", (a, b))


create_rsrc_tbl()
create_user_tbl()

add_user('', '')
add_user('neic', 'Northy the  Archive')
add_user('KD', 'Kyle Deutsch')
insert_resource(10, 'P-04-1001', 'CA-BUT-1001', 1, 1, '8/30/2016', 1, 1, '8/30/2016', 1, 2, '8/31/2016', 0, 0, 1, 0, 1,
                0, 0, 'Size hella wrong')
insert_resource(10, 'P-04-1002', 'CA-BUT-1002', 1, 1, '8/30/2016', 1, 1, '8/30/2016', 1, 2, '8/31/2016', 0, 0, 0, 0, 0,
                0, 1, 'I just dont like this one.')
insert_resource(10, 'P-04-1003', 'CA-BUT-1003', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, 0, 0, 0,
                0, 0, '')
insert_resource(10, 'P-04-1004', 'CA-BUT-1004', 0, 0, '', 0, 0, '', 0, 0, '', 0, 0, 0, 0, 0,
                0, 0, '')

conn.commit()
conn.close()
