import sqlite3
import tqdm
import dataframe


def compare():
    connect = sqlite3.connect('.\\df\\data.db')
    cur = connect.cursor()
    li = cur.execute("SELECT sents,id from st")
    ls = cur.execute("SELECT wordlist,id from sw")
    print("sentence")
    for each in tqdm.tqdm(li):
        if dataframe.md_5(each[0]).encode() == each[1]:
            pass
        else:
            connect.close()
            raise Exception("different")
    print("wordlist")
    for each in tqdm.tqdm(ls):
        if dataframe.md_5(each[0]).encode() == each[1]:
            pass
        else:
            connect.close()
            raise Exception("different")
    print("no error was found")
    connect.close()


if __name__ == '__main__':
    compare()
