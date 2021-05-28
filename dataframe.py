import sqlite3
import os
import csv
import tqdm


def setup():
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
                '(sents INT PRIMARY KEY NOT NULL);')
    connect.commit()
    for each in tqdm.tqdm(li):
        with open(each + '.csv', 'rt', encoding='utf-8') as rf:
            c = csv.reader(rf)
            for item in c:
                if item:
                    cur.execute(f'INSERT OR IGNORE INTO st (sents) VALUES ({int.from_bytes(item[0].encode(), "big")})')
    connect.commit()
    cur.execute('CREATE TABLE sw'
                '(wordlist INT PRIMARY KEY NOT NULL);')
    connect.commit()
    for each in tqdm.tqdm(li):
        with open('storey_' + each + '.csv', 'rt', encoding='utf-8') as rf:
            c = csv.reader(rf)
            for item in c:
                words = ';'.join(item)
                if not words:
                    continue
                cur.execute(f'INSERT OR IGNORE INTO sw (wordlist) VALUES ({int.from_bytes(words.encode(), "big")})')
    connect.commit()
    connect.close()
    print('congratulations')


if __name__ == '__main__':
    setup()
