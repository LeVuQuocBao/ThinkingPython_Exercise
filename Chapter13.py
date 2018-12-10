# 13.1
from structshape import structshape
import string


# read file
def readfile(filedir):
    fin = open(filedir)
    linelist = list()
    for line in fin:
        linelist.append(line)
    return linelist


def linebreake_punctclear(listin):
    outlist = []
    for line in listin:
        linelist = line.split(' ')
        out = punctuation_del(linelist)
        outlist.append(out[:])
    return outlist


def punctuation_del(listin):
    '''receive list of word and clear out any punctuation in the list
    input=list word with punctuation
    output=list word without punctuation'''
    listout = []
    for word in listin:
        wordlist = list(word)
        cleanWordlist = []
        for i, char in enumerate(wordlist):
            if char not in punctdict and char not in whitedict:
                cleanWordlist.append(char)
        word = ''.join(cleanWordlist)
        listout.append(word.lower())
    return listout


def puncutation_dict():
    dictout = {}
    punclist = string.punctuation
    for puncChar in punclist:
        dictout[puncChar] = puncChar
    return dictout


def whitespace_dict():
    dictout = {}
    whitelist = string.whitespace
    for whitechar in whitelist:
        dictout[whitechar] = whitechar
    return dictout


def extract_words_only(listin):
    '''process out put from linebreake_punctclear which is a list of list n string
    input: list of list of n string
    process: get only character string => create list to output
    output list of string from character only'''
    outlist = []
    for curlist in listin:
        for string in curlist:
            if not string.isdigit() and string != '':
                outlist.append(string)
    return outlist

def words_histogram(listin):
    histout=dict()
    for word in listin:
        histout[word]=histout.setdefault(word,0)+1
    sortlist=[]
    totalWords=0
    for key,value in histout.items():
        sortlist.append((value,key))
        totalWords=totalWords+value
    sortlist.sort(reverse=True)
    return histout,sortlist,totalWords
textread = readfile('book1Chapter13ex132.txt')
print(textread)
punctdict = puncutation_dict()
whitedict = whitespace_dict()
book_stringlist = linebreake_punctclear(textread[23:])
words_in_book = extract_words_only(book_stringlist)
word_hist,sort_hist,totalwords=(words_histogram(words_in_book))
print('Most use words and freq',sort_hist)
print('Total used words',totalwords)
print('Total diffent words in book are:',len(word_hist.keys()))

