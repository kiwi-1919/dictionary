import sqlite3
import spacy


def match(string=None):
    s = spacy.load("en_core_web_lg")
    word = s(string)[0].lemma_
    connect = sqlite3.connect('.\\df\\data.db')
    li = connect.execute("SELECT ind,wordlist from sw")
    ls = connect.execute("SELECT word from aw")
    lt = list(connect.execute("SELECT sents from st"))
    for each in ls:
        if each[0] == word:
            print("exist")
            break
        else:
            print("nothing", end=";")
    index = list()
    for each in li:
        wordlist = each[1].decode()
        if wordlist.find(word) != -1:
            index.append(each[0])
        else:
            print("nothing", end=";")
    for each in index:
        yield lt[each - 1]
    connect.close()


if __name__ == '__main__':
    try:
        l = match(input("word"))
    except:
        raise Exception("???")
    try:
        n = 0
        for each in l:
            print(each[0].decode())
            n += 1
            if n >= 5:
                break
    except:
        pass
