import sqlite3
import os
import csv


def setup():
    li = os.listdir('.\\txt')
    connect = sqlite3.connect('.\\df\\aw.db')
    cur = connect.cursor()
    cur.execute('CREATE TABLE aw (word TEXT PRIMARY KEY NOT NULL)')
    for each in li:
        with open(each + '.aw.txt', 'rt', encoding='utf-8') as rf:
            for item in rf.read().split(';'):
                if not item:
                    continue
                cur.execute(f"INSERT OR IGNORE INTO aw (word) VALUES ('{item}')")
    connect.commit()
    connect.close()
    connect = sqlite3.connect('.\\df\\st.db')
    cur = connect.cursor()
    cur.execute('CREATE TABLE st (sents TEXT PRIMARY KEY NOT NULL)')
    for each in li:
        with open(each + '.csv', 'rt', encoding='utf-8') as rf:
            c = csv.reader(rf)
            for item in c:
                try:
                    cur.execute(f"INSERT OR IGNORE INTO st (sents) VALUES ('{item[0]}')")
                except:
                    pass
    connect.commit()
    connect.close()
    connect = sqlite3.connect('.\\df\\sw.db')
    cur = connect.cursor()
    cur.execute('CREATE TABLE sw (wordlist TEXT PRIMARY KEY NOT NULL)')
    for each in li:
        with open('storey_' + each + '.csv', 'rt', encoding='utf-8') as rf:
            c = csv.reader(rf)
            for item in c:
                words = str()
                for word in item:
                    words += (word + ';')
                if not words:
                    continue
                cur.execute(f"INSERT OR IGNORE INTO sw (wordlist) VALUES ('{words}')")
    connect.commit()
    connect.close()
    print('congratulations')


if __name__ == '__main__':
    setup()
