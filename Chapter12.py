from structshape import structshape
# 12.1 Most frequent
def hist_text(string):
    hisdict = dict()
    for char in string:
        hisdict[char] = hisdict.setdefault(char, 0) + 1
    return hisdict


def most_frequent(listin):
    ''' Analyze histogram of words usage'''
    # initialize totalHis with empty dict
    totalHis = dict()
    for string in listin:
        # Produce 1 dict of str -> int every string in words list:
        onetextHist = hist_text(string)
        # extend totalHis with onetextHist:
        for char, count in onetextHist.items():
            totalHis[char] = totalHis.setdefault(char, 0) + count
    # sorting totalHis with decreasing freq order:
    charlist = list(totalHis)
    freq = list(totalHis.values())
    listHisTuple = list(zip(freq, charlist))
    listHisTuple.sort()
    print(structshape(listHisTuple))
    return totalHis


# fin=open('words.txt')
# wordslist=[]
# for line in fin:
#     wordslist.append(line.strip())
# print(wordslist)
# print(structshape(wordslist))
# print(most_frequent(wordslist))
def signature(s):
    """Returns the signature of this string, which is a string
    that contains all of the letters in order.
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


# 12.5 Metathesis pair
def word_L_classification(listin):
    '''Input a list of string
    output: a dict of ({length of string(int):[wordlist have the same length]'''
    Ldict = dict()
    for string in listin:
        strL = len(string)
        Ldict.setdefault(strL, []).append(string)
    return Ldict


def devide_list(listin):
    ''' receive list of words and devide in to dict of same charater word'''
    dictout = {}
    for i, word in enumerate(listin):
        t = signature(word)
        if t not in dictout:
            dictout[t] = [word]
        else:
            dictout[t].append(word)
    # delete all dictionary item have only one world in list
    delkeylist = []
    for key in dictout:
        if len(dictout[key]) == 1:
            delkeylist.append(key)
    print(delkeylist)
    for delkey in delkeylist:
        del dictout[delkey]
    return dictout


def metathesis_test(str1, str2):
    dif = 0
    for i, char in enumerate(str1):
        if dif > 2:
            return False
        if char != str2[i]:
            dif += 1
    return True


fin = open('words.txt')
wordslist = []
for line in fin:
    wordslist.append(line.strip())
devided_word = devide_list(wordslist)
metathesis_List = []
for key in devided_word:
    # (devided_word[key]) is a list of word\
    # print(key)
    # print(devided_word[key])
    currentlist = devided_word[key]
    for i in range(0, len(currentlist)):
        for k in range(i + 1, len(currentlist)):
            if (metathesis_test(currentlist[i], currentlist[k])) == True:
                metathesis_List.append(tuple((currentlist[i], currentlist[k])))
print(metathesis_List)
print(structshape(metathesis_List))