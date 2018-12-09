# 10.1
def nested_sum(list_in):
    total = 0
    for intlist in list_in:
        total = total + sum(intlist)
    return total


# print(nested_sum([[2,3],[5,6],[12,11]]))
# 10.2
def capitalize_all(string):
    res = []
    for s in string:
        res.append(s.capitalize())
    return res


def nested_capitalize(listString):
    outList = []
    for t in listString:
        outList.append(capitalize_all(t))
    return outList


# print(capitalize_all(['apple', 'ice cream', 'wheat']))
# print(nested_capitalize([['book', 'pen'], ['table', 'oven'], ['phone', 'glass']]))

# 10.3
def sum_cumulative(listNum):
    cumulative=[]
    for i,value in enumerate(listNum):
        if i==0:
            cumulative.append(value)
        else:
            cumulative.append(value+sum(listNum[:i]))
    return cumulative
# print(sum_cumulative([1,2,3,4]))
# 10.4
def middle(listin):
    listout=listin[1:len(listin)-1]
    return listout
# demolist=[1,2,3,4,5]
# print(middle(demolist))
# print(demolist)
def chop(listin):
    del listin[0]
    del listin[-1]
# print(chop(demolist))
# print(demolist)

#  EX. 10.6
def is_sorted(listin):
    sorted=listin[:]

    sorted.sort()
    if sorted == listin:
        return True
    else:
        return False
# print(is_sorted(['a','b','f','e']))
#  EX. 10.7
def is_anagram(worda,wordb):
    wordatmp=[]
    wordbtmp=[]
    wordatmp.extend(worda)
    wordbtmp.extend(wordb)
    print(worda)
    print(wordb)
    wordatmp.sort()
    wordbtmp.sort()
    print(wordatmp)
    print(wordbtmp)
    if wordatmp==wordbtmp:
        return True
    else:
        return False
# print(is_anagram('stop','spot'))
# 10.8
def has_duplicates(listin):
    for i,element in enumerate(listin):
        if listin.count(element) != 1:
            return True
    return False
# print(has_duplicates(['apple','pine','cake']))
def remove_duplicate(listin):
    for i,element in enumerate(listin):
        if listin.count(element)!=1:
            del listin[i]
# duplist=['glass','student','table','student','glass']
# print(duplist)
# remove_duplicate(duplist)
# print(duplist)
def readword_append(wordfile):
    import time
    # timestart=time.time()
    fin=open(wordfile)
    listword=[]
    for line in fin:
        listword.append(line.strip())
    # timeused=time.time()-timestart
    # print(timeused)
    return listword
def readword_sumidiom(wordfile):
    import time
    timestart=time.time()
    fin=open(wordfile)
    listword=[]
    for line in fin:
        listword=listword+[line.strip()]
    timeused=time.time()-timestart
    print(timeused)
    return listword,timeused
# outlist,time=readword_append('words.txt')
# outlist,time=readword_sumidiom('words.txt')