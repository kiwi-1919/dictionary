import sqlite3
import os
import csv


def setup():
    li = os.listdir('.\\txt')
    connect = sqlite3.connect('.\\df\\aw.db')
    cur = connect.cursor()
    cur.execute('CREATE TABLE aw (word TEXT)')
    for each in li:
        with open(each + '.aw.txt', 'rt') as rf:
            for item in rf.read().split(';'):
                cur.execute(f"INSERT INTO aw VALUES('{item}')")
    connect.commit()
    connect.close()
    connect = sqlite3.connect('.\\df\\st.db')
    cur = connect.cursor()
    cur.execute('CREATE TABLE st (sents TEXT)')
    for each in li:
        with open(each + '.csv', 'rt') as rf:
            c = csv.reader(rf)
            for item in c:
                try:
                    cur.execute(f"INSERT INTO st VALUES('{item[0]}')")
                except:
                    pass
    connect.commit()
    connect.close()
    connect = sqlite3.connect('.\\df\\sw.db')
    cur = connect.cursor()
    cur.execute('CREATE TABLE sw (wordlist TEXT)')
    for each in li:
        with open('storey_' + each + '.csv', 'rt') as rf:
            c = csv.reader(rf)
            for item in c:
                words = str()
                for word in item:
                    words += (word + ';')
                cur.execute(f"INSERT INTO sw VALUES('{words}')")
    connect.commit()
    connect.close()
    print('congratulations')


if __name__ == '__main__':
    setup()
