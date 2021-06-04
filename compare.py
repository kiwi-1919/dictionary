import sqlite3
import tqdm
import dataframe


def generate(li):
    ls = [each for each in li]
    print(len(ls))
    for item in tqdm.tqdm(ls):
        yield item


def compare():
    connect = sqlite3.connect('.\\df\\data.db')
    li = generate(connect.execute("SELECT sents,id from st"))
    ls = generate(connect.execute("SELECT wordlist,id from sw"))
    print("begin")
    for each in zip(li, ls):
        if dataframe.md_5(each[0][0]).encode() == each[0][1] and dataframe.md_5(each[1][0]).encode() == each[1][1]:
            pass
        else:
            connect.close()
            raise Exception("different")
    print("no error was found")
    connect.close()


if __name__ == '__main__':
    compare()
