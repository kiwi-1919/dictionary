import os
import random
import tqdm
import sqlite3
import hashlib


def check(path=None):
    if not path:
        connect = sqlite3.connect('.\\df\\data.db')
        cur = connect.cursor()
        try:
            cur.execute('drop table hash')
            connect.commit()
        except:
            pass
        cur.execute('CREATE TABLE hash (value TEXT);')
        connect.commit()
        for each in tqdm.tqdm(os.listdir('.\\txt')):
            with open(os.path.join('.\\txt', each), 'rt') as rf:
                value = hashlib.sha1(rf.read().encode())
                cur.execute(f'INSERT OR IGNORE INTO hash (value) VALUES ("{value}")')
        connect.commit()
        connect.close()
    else:
        connect = sqlite3.connect('.\\df\\data.db')
        cur = connect.cursor()
        with open(path, 'rt') as rf:
            hash_value = hashlib.sha1(rf.read().encode())
        cur.execute("PRAGMA table_info(hash)")
        if (hash_value) in cur.fetchall():
            connect.close()
            raise Exception('SameFileError')
        else:
            connect.close()


def add():
    l = list()
    while True:
        if input('continue/not:y/o') == 'y':
            l.append(input('add from where'))
        else:
            break
    try:
        for each in tqdm.tqdm(l):
            check(path=each)
            os.system(
                f'copy {each} {os.path.join(os.curdir, "txt", str(random.randint(0, 1000000000000000000)) + ".txt")} '
                f'/-Y')
    except:
        print('fail')
        pass


if __name__ == '__main__':
    check()
    if input('add or not:y/o') == 'y':
        add()
