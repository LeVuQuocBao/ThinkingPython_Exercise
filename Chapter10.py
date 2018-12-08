# 10.1
def nested_sum(list_in):
    total=0
    for intlist in list_in:
       total=total+sum(intlist)
    return total
# print(nested_sum([[2,3],[5,6],[12,11]]))
def capitalize_all(string):
    res=[]
    for s in string:
        res.append(s.capitalize())
    return res
def nested_capitalize(listString):
    outList=[]
    for t in listString:
        outList.append(capitalize_all(t))
    return outList
print(capitalize_all(['apple','ice cream','wheat']))
print(nested_capitalize([['book','pen'],['table','oven'],['phone','glass']]))