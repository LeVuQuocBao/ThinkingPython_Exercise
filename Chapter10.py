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
demolist=[1,2,3,4,5]
print(middle(demolist))
print(demolist)
def chop(listin):
    del listin[0]
    del listin[-1]
print(chop(demolist))
print(demolist)
