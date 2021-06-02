import sqlite3

import tqdm


def compare():
    connect = sqlite3.connect('.\\df\\data.db')
    cur = connect.cursor()
    content = cur.execute('SELECT sents,id from st')
    for each in tqdm.tqdm(content):
        if not each:
            continue
        value = hash(str(bytes([int(item) for item in each[0]]), 'utf-8'))
        if f'{value}' == each[1]:
            pass
        else:
            raise Exception('A difference has been found.')
    content = cur.execute('SELECT wordlist,id from sw')
    for each in tqdm.tqdm(content):
        if not each:
            continue
        value = hash(str(bytes([int(item) for item in each[0]]), 'utf-8'))
        if f'{value}' == each[1]:
            pass
        else:
            raise Exception('A difference has been found')
    connect.close()


if __name__ == '__main__':
    compare()
