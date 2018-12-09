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
# h=histogram_char('carrot')
# print_his(h)
# print(keys(h))
# 11.4
def reverse_lookup(h,n):
    listout=[]
    for i in h:
        if h[i]==n:
            listout.append(i)
    return listout
# print(reverse_lookup(h,1))
def reversed_dict(h):
    invers=dict()
    for key in h:
        val =h[key]
        if val not in invers:
            invers[val]=[key]
        else:
            invers[val].append(key)
    return invers
# print(reversed_dict(h))
def reversed_dict_setdef(h):
    print(h)
    invers=dict()
    for key in h:
        print('key', '-', 'val')
        val =h[key]
        print(key,'-',val)
        invers.setdefault(val, list()).append(key)
    return invers
# print(reversed_dict_setdef(h))
# 11.6 Fibonacci compare
def fibonaccy_recursion(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonaccy_recursion(n-1)+fibonaccy_recursion(n-2)
def fibonaccy_memo(n):
    '''using memo technique to reduce calculation time for fibonacci number'''
    # print(knownF)
    if n in knownF:
        return knownF[n]
    else:
        newF=fibonaccy_memo(n-1)+fibonaccy_memo(n-2)
        knownF[n]=newF
    return newF
starttime=time.time()
print(fibonaccy_recursion(30))
print('used time',time.time()-starttime)
starttime=time.time()
knownF={0:0,1:1}
print(fibonaccy_memo(100))
print('used time',time.time()-starttime)
