# 11.1
from Chapter10 import readword_append
import time
def dictgromword(wordfile):
    fin=open(wordfile)
    dictout=dict()
    for line in fin:
        dictout[line.strip()]='Null'
    return dictout
# dictout=dictgromword('words.txt')
# print(dictout)
# listout=readword_append('words.txt')
# print(listout)
# startsearch=time.time()
# print('trousers'in dictout)
# print(time.time()-startsearch)
# startsearch=time.time()
# print('trousers'in listout)
# print(time.time()-startsearch)
#  11.2
def histogram_char(string):
    d=dict()
    for c in string:
        d[c]=d.get(c,0)+1
    return d
def print_his(h):
    for i in h:
        print(i,h[i])
# print(histogram_char('schooled'))
# h=histogram_char('parrot')
# print_his(h)
# 11.3
def keys(h):
    '''return key of input h dictionary'''
    outstring=[]
    for text in h:
        outstring.append(text)
    return outstring
h=histogram_char('carrot')
print_his(h)
print(keys(h))
# 11.4
def reverse_lookup(h,n):
    listout=[]
    for i in h:
        if h[i]==n:
            listout.append(i)
    return listout
print(reverse_lookup(h,1))
