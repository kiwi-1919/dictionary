#cython:language_level=3
cimport cython
import spacy
import csv
import os
cdef list parse_word(str txt):
    cdef list l
    #end-cdef
    l=txt.split(';')
    return l
cdef list find_by_suf(str dir,str suffix):
    cdef list l=os.listdir(dir)
    cdef list li=list()
    #end-cdef
    for each in l:
        li.append(each+suffix)
    return li
def parse_sents_to_words(csv_name):
    try:
        rf=open(csv_name,'rt',encoding='utf-8')
        wf=open('storey_'+csv_name,'wt',encoding='utf-8')
        rc=csv.reader(rf)
        wc=csv.writer(wf)
        s=spacy.load('en_core_web_lg')
        for each in rc:
            if not each:
                continue
            doc=s(each[0])
            wc.writerow([word.lemma_ for word in doc])
    except:
        raise Exception('ParseError')
    finally:
        rf.close()
        wf.close()
def choose(aw_name):
    with open(aw_name,'rt',encoding='utf-8') as rf:
        with open(aw_name+'.txt','wt',encoding='utf-8') as wf:
            solve=spacy.load('en_core_web_lg')
            for each in sorted(list(set(parse_word(rf.read()))),reverse=True):
                word=solve(each)[0].lemma_
                wf.write(word+';')
def pyfind_by_suf(dir,suffix):
    return find_by_suf(dir,suffix)