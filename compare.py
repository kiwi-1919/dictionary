import sqlite3
from dataframe import md_5
import tqdm
import struct


def compare():
    connect = sqlite3.connect('.\\df\\data.db')
    cur = connect.cursor()
    content = cur.execute('SELECT sents,id from st')
    for each in tqdm.tqdm(content):
        if not each:
            continue
        value = md_5(struct.unpack('s', each[0]))
        if value == each[1]:
            pass
        else:
            raise Exception('A difference has been found.')
    content = cur.execute('SELECT wordlist,id from sw')
    for each in tqdm.tqdm(content):
        if not each:
            continue
        value = md_5(struct.unpack('s', each[0]))
        if value == each[1]:
            pass
        else:
            raise Exception('A difference has been found')
    connect.close()


if __name__ == '__main__':
    compare()
