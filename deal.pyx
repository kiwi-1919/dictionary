#cython:language_level=3
cimport cython
import spacy
import os
import tqdm
from libc.stdio cimport *
import csv
cdef str char_p_to_str(char* c):
    cdef bytes b=<bytes>c
    cdef str res=b.decode()
    #end-cdef
    return res
cdef char* str_to_char_p(str s):
    cdef bytes b=s.encode()
    cdef char* c=<char*>b
    #end-cdef
    return c
cdef list find_txt(str txt_dir):
    cdef list l=list()
    #end-cdef
    for each in os.listdir(txt_dir):
        l.append(os.path.join(txt_dir,each))
    return l
cdef void parse_sents(str path):
    solve=spacy.load('en_core_web_lg')
    solve.max_length=1000000
    with open(path,'rt',encoding='utf-8') as rf:
        with open(os.path.splitext(path)[0]+'.csv','wt',encoding='utf-8') as wf:
            c=csv.writer(wf)
            for each in solve(rf.read()).sents:
                c.writerow([str(each)])
cdef void parse_all_word(str path):
    cdef FILE* rf=fopen(str_to_char_p(path),'rb')
    cdef FILE* wf=fopen(str_to_char_p(path+'.aw'),'wb')
    cdef char c
    cdef bytes b1='a'.encode()
    cdef char a=<char>int.from_bytes(b1,'big')
    cdef bytes b2='z'.encode()
    cdef char z=<char>int.from_bytes(b2,'big')
    cdef bytes b3='A'.encode()
    cdef char A=<char>int.from_bytes(b3,'big')
    cdef bytes b4='Z'.encode()
    cdef char Z=<char>int.from_bytes(b4,'big')
    cdef bytes b5=';'.encode()
    cdef char sep=<char>int.from_bytes(b5,'big')
    #end-cdef
    while True:
        if fread(&c,1,1,rf)==1:
            if (c>=a and c<=z) or (c>=A and c<=Z):
                fwrite(&c,1,1,wf)
            else:
                fwrite(&sep,1,1,wf)
        else:
            break
    fclose(rf)
    fclose(wf)
cdef list parse(str string):
    solve=spacy.load('en_core_web_lg')
    solve.max_length=1000000
    doc=solve(string)
    return [each.lemma_ for each in doc]
def setup():
    for each in tqdm.tqdm(find_txt('.\\txt')):
        parse_sents(each)
        parse_all_word(each)