import os
import random
import tqdm
import sqlite3
from dataframe import md_5


def check(path=None):
    if not path:
        connect = sqlite3.connect('.\\df\\data.db')
        cur = connect.cursor()
        try:
            cur.execute('drop table hash')
            connect.commit()
        except:
            pass
        cur.execute('CREATE TABLE hash (value BLOB,id BLOB);')
        connect.commit()
        for each in tqdm.tqdm(os.listdir('.\\txt')):
            with open(os.path.join('.\\txt', each), 'rt', encoding='utf-8') as rf:
                value = md_5(rf.read().encode()).encode()
                id = os.path.join('.\\txt', each).encode()
                cur.execute(f'INSERT OR IGNORE INTO hash (value,id) VALUES (?,?)',
                            (sqlite3.Binary(value), sqlite3.Binary(id)))
        connect.commit()
        connect.close()
    else:
        connect = sqlite3.connect('.\\df\\data.db')
        cur = connect.execute("SELECT value from hash")
        with open(path, 'rt', encoding='utf-8') as rf:
            hash_value = md_5(rf.read().encode()).encode()
        for each in cur:
            if hash_value in each:
                connect.close()
                raise Exception('SameFileError')
            else:
                pass
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
            if os.listdir('.\\txt'):
                check(path=each)
            os.system(
                f'copy {each} {os.path.join(os.curdir, "txt", str(random.randint(0, 1000000000000000000)) + ".txt")} '
                f'/-Y')
    except:
        print('fail')
        pass


def main():
    if os.listdir('.\\txt'):
        check()
    if input('add or not:y/o') == 'y':
        add()


if __name__ == '__main__':
    main()
