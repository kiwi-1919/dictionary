import sqlite3
import tqdm
import dataframe


def generate(iter):
    l = [each for each in iter]
    for item in l:
        yield item


def compare():
    connect = sqlite3.connect('.\\df\\data.db')
    cur = connect.cursor()
    li = generate(cur.execute("SELECT sents,id from st"))
    ls = generate(cur.execute("SELECT wordlist,id from sw"))
    connect.close()
    print("sentence")
    for each in tqdm.tqdm(li):
        if dataframe.md_5(each[0]).encode() == each[1]:
            pass
        else:
            raise Exception("different")
    print("wordlist")
    for each in tqdm.tqdm(ls):
        if dataframe.md_5(each[0]).encode() == each[1]:
            pass
        else:
            raise Exception("different")
    print("no error was found")


if __name__ == '__main__':
    compare()
