import sqlite3

import os
import platform

sys = platform.system()
folder = os.getcwd()
shortdir = folder
if sys == 'Darwin':
    longdir = shortdir + '/db/test.db'
elif sys == 'Windows':
    longdir = shortdir + r'/db/test.db'
else:
    print 'Failed to find database directory.'

conn = sqlite3.connect(longdir)
cursor = conn.cursor()


def read():
    selection = cursor.execute('SELECT * FROM resources;')
    data = selection.fetchall()
    return data


def read_users():
    selection = cursor.execute('SELECT * FROM users;')
    data = selection.fetchall()
    return data


def complete(field, user, date, record):
    print field, user, date, record
    cursor.execute('UPDATE resources SET %sCheck = 1, %sUsrID = ?, %sDate = ? WHERE ID = ?'
                   % (field , field, field),
                   (user, date, record))
    conn.commit()


def update_gis(field, value, record):
    cursor.execute('UPDATE resources SET %s = ? WHERE ID = ?' % (field), (value, record))
    conn.commit()


def update_gis_text(value, record):
    cursor.execute('UPDATE resources SET Note = ? WHERE ID = ?', (value, record))
    conn.commit()
