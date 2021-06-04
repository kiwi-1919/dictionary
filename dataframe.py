import csv
import hashlib
import os
import sqlite3

import tqdm

i = 0
n = 0


def md_5(byte):
    m = hashlib.md5()
    m.update(byte)
    return m.hexdigest()


def setup():
    global i
    global n
    li = os.listdir('.\\txt')
    connect = sqlite3.connect('.\\df\\data.db')
    cur = connect.cursor()
    try:
        cur.execute('drop table aw')
        cur.execute('drop table st')
        cur.execute('drop table sw')
        connect.commit()
    except:
        pass
    cur.execute('''CREATE TABLE aw
    (word TEXT PRIMARY KEY NOT NULL);''')
    connect.commit()
    for each in tqdm.tqdm(li):
        with open(each + '.aw.txt', 'rt', encoding='utf-8') as rf:
            for item in rf.read().split(';'):
                if not item:
                    continue
                cur.execute(f"INSERT OR IGNORE INTO aw (word) VALUES ('{item}')")
    connect.commit()
    cur.execute('''CREATE TABLE st (index INTEGER PRIMARY KEY NOT NULL,sents BLOB NOT NULL,id BLOB NOT NULL);''')
    connect.commit()
    for each in tqdm.tqdm(li):
        with open(each + '.csv', 'rt', encoding='utf-8') as rf:
            c = csv.reader(rf)
            for item in c:
                if item:
                    i += 1
                    cur.execute(
                        f'INSERT INTO st (index,sents,id) VALUES (?,?,?)'
                        , (i, sqlite3.Binary(item[0].encode()), sqlite3.Binary(md_5(item[0].encode()).encode())))
    connect.commit()
    cur.execute('''CREATE TABLE sw (index INTEGER PRIMARY KEY NOT NULL,wordlist BLOB NOT NULL,id BLOB NOT NULL);''')
    connect.commit()
    for each in tqdm.tqdm(li):
        with open('storey_' + each + '.csv', 'rt', encoding='utf-8') as rf:
            c = csv.reader(rf)
            for item in c:
                words = ';'.join(item)
                if not words:
                    continue
                n += 1
                cur.execute(
                    f'INSERT INTO sw (index,wordlist,id) VALUES (?,?,?)',
                    (n, sqlite3.Binary(words.encode()), sqlite3.Binary(md_5(words.encode()).encode())))
    connect.commit()
    connect.close()
    if n == i:
        print('congratulations')
    else:
        print('emm...')


if __name__ == '__main__':
    setup()
