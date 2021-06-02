import csv
import os
import sqlite3
import hashlib
import tqdm
import struct

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
    cur.execute('CREATE TABLE st'
                '(sents TEXT PRIMARY KEY NOT NULL,'
                'id TEXT NOT NULL);')
    connect.commit()
    for each in tqdm.tqdm(li):
        with open(each + '.csv', 'rt', encoding='utf-8') as rf:
            c = csv.reader(rf)
            for item in c:
                if item:
                    i += 1
                    cur.execute(
                        f'INSERT OR IGNORE INTO st (sents,id) VALUES ("{struct.pack("s",item[0].encode()).decode()}",'
                        f'"{md_5(item[0].encode())}")')
    connect.commit()
    cur.execute('CREATE TABLE sw'
                '(wordlist TEXT PRIMARY KEY NOT NULL,'
                'id TEXT NOT NULL);')
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
                    f'INSERT OR IGNORE INTO sw (wordlist,id) VALUES ("{struct.pack("s",words.encode()).decode()}",'
                    f'"{md_5(words.encode())}")')
    connect.commit()
    connect.close()
    if n == i:
        print('congratulations')
    else:
        print('emm...')


if __name__ == '__main__':
    setup()
