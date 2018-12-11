# # 13.1
# from structshape import structshape
# import string
#
#
# # read file
# def readfile(filedir):
#     fin = open(filedir)
#     linelist = list()
#     for line in fin:
#         linelist.append(line)
#     return linelist
#
#
# def linebreake_punctclear(listin):
#     outlist = []
#     for line in listin:
#         linelist = line.split(' ')
#         out = punctuation_del(linelist)
#         outlist.append(out[:])
#     return outlist
#
#
# def punctuation_del(listin):
#     '''receive list of word and clear out any punctuation in the list
#     input=list word with punctuation
#     output=list word without punctuation'''
#     listout = []
#     for word in listin:
#         wordlist = list(word)
#         cleanWordlist = []
#         for i, char in enumerate(wordlist):
#             if char not in punctdict and char not in whitedict:
#                 cleanWordlist.append(char)
#         word = ''.join(cleanWordlist)
#         listout.append(word.lower())
#     return listout
#
#
# def puncutation_dict():
#     dictout = {}
#     punclist = string.punctuation
#     for puncChar in punclist:
#         dictout[puncChar] = puncChar
#     return dictout
#
#
# def whitespace_dict():
#     dictout = {}
#     whitelist = string.whitespace
#     for whitechar in whitelist:
#         dictout[whitechar] = whitechar
#     return dictout
#
#
# def extract_words_only(listin):
#     '''process out put from linebreake_punctclear which is a list of list n string
#     input: list of list of n string
#     process: get only character string => create list to output
#     output list of string from character only'''
#     outlist = []
#     for curlist in listin:
#         for string in curlist:
#             if not string.isdigit() and string != '':
#                 outlist.append(string)
#     return outlist
#
#
# def words_histogram(listin):
#     histout = dict()
#     for word in listin:
#         histout[word] = histout.setdefault(word, 0) + 1
#     sortlist = []
#     totalWords = 0
#     for key, value in histout.items():
#         sortlist.append((value, key))
#         totalWords = totalWords + value
#     sortlist.sort(reverse=True)
#     return histout, sortlist, totalWords
#
#
# textread = readfile('book1Chapter13ex132.txt')
# # print(textread)
# # punctdict = puncutation_dict()
# # whitedict = whitespace_dict()
# # book_stringlist = linebreake_punctclear(textread[23:])
# # words_in_book = extract_words_only(book_stringlist)
# # word_hist,sort_hist,totalwords=(words_histogram(words_in_book))
# # print('Most use words and freq',sort_hist)
# # print('Total used words',totalwords)
# # print('Total different words in book are:',len(word_hist.keys()))
# # 13.3 Print most 20 frequently used
# # top20=sort_hist[0:20]
# # top20words=[]
# # for tup in top20:
# #     top20words.append(tup[1])
#
# # print('Most 20 frequently used:',top20words)
#
#
# # Ex. 13.5
# from random import random, randint, choice
#
#
# def histogram(listin):
#     '''Take a list of char in, return histogram dict out'''
#     dictout = {}
#     for char in listin:
#         dictout[char] = dictout.setdefault(char, 0) + 1
#     return dictout
#
#
# def choose_from_hist(histin):
#     # extract list from histin
#     dicttmp = dict(histin)
#     tmplist = []
#     for key, value in dicttmp.items():
#         for i in range(value):
#             tmplist.append(key)
#     # outchar= tmplist[randint(0,len(tmplist)-1)]
#     outchar = choice(tmplist)
#     return outchar
#
#
# # textlist=['a','b','c','d','a','b','a']
# # histtest=histogram(textlist)
# # for i in range(10):
# #     print(choose_from_hist(histtest))
import sys, string, random

# global variables
suffix_map = {}
prefix = ()


def process_file(filename, order=2):
    fp = open(filename)
    skip_header(fp)
    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def skip_header(fp):
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_word(word, order=2):
   global prefix
   if len(prefix)<order:
       prefix +=(word,)
       return
   try:
       suffix_map[prefix].append(word)
   except KeyError:
       suffix_map[prefix]=[word]

   prefix=shift(prefix,word)
def random_text(n=100):
    start=random.choice(list(suffix_map.keys()))
    for i in range(n):
        suffixes=suffix_map.get(start,None)
        if suffixes == None:
            random_text(n-1)
            return
        word=random.choice(suffixes)
        print(word)
        start = shift(start,word)
def shift(t,word):
    return t[1:]+(word,)
def main(filename='',n=100,order=2,*args):
    try:
        n=int(n)
        order = int(order)
    except:
        print(' Usage: randomtext.py filename [# of words] [prefix length]')
    else:
        process_file(filename,order)
        random_text(n)
main('emma.txt',100,2)