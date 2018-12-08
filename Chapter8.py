def findCh(*args):
    '''Find index of a charater in give string'''
    varargin = args
    if len(varargin)==1:
        print('Not enough input argument!')
        return -1
    if len(varargin)==2:
        string=varargin[0]
        character=varargin[1]
        i = -1
        while True:
            i = i + 1
            if i == len(string):
                break
            if string[i] == character:
                return i
        return -1
    if len(varargin) == 3:
        string = varargin[0]
        character = varargin[1]
        a=varargin[2]
        i=a
        while True:
            i=i+1
            if i==len(string):
                break
            if string[i]==character:
                return i
        return -1
    if len(varargin) == 4:
        string = varargin[0]
        character = varargin[1]
        a=varargin[2]
        b=varargin[3]
        i=a
        while True:
            i=i+1
            if i==b:
                break
            if string[i]==character:
                return i
        return -1
# print(findCh('banana','a',2,4))
def countCh(*args):
    varargin=args
    if len(varargin)==1:
        print('not enought input argument')
    if len(varargin)==2:
        string=varargin[0]
        character=varargin[1]
        count=0
        for i in string:
            if i == character:
                count+=1
        return count
    if len(varargin)==3:
        string = varargin[0]
        character = varargin[1]
        a=varargin[2]
        count = 0
        for i in range(a,len(string)-1):
            if string[i] == character:
                count += 1
        return count
print(countCh('black rashberry','b',0))