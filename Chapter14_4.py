from Chapter14runcmd import runcmd
import os
from pprint import pprint
from structshape import structshape


def md5cal(path):
    ''' Receive a directory made from home <str> + dir <str> and calculate md5 check sum for [filename] file
     return md5 result <str>'''
    md5 = runcmd('cd ./143 && md5 ' + path)
    md5list = md5.split('  ')
    return md5list[0]


def filedictcreate(searchDir, ext, filedict):
    '''Receive a searchDir <str> , scan through this Dir and note all path of a txt file'''
    for itemname in os.listdir(searchDir):
        path = os.path.join(searchDir, itemname)
        if os.path.isdir(path):
            filedictcreate(path, ext, filedict)
        else:
            if path.endswith(ext):
                filedict[path] = 1
    return filedict


def createmd5dict(searchDir, ext):
    '''Receive a searchDir and scan for mp3 file with filedict
    then calculate md5 checksum for each key in filedict'''
    filedict = {}
    listfile = filedictcreate(searchDir, ext, filedict)  # return all *.ext in dir
    for key in listfile:
        listfile[key] = md5cal(key)
    return filedict


def dupplicatedfile(searchDir, ext):
    '''Get a listfile<dict> which is ['filename':md5 value]
     find duplicated and return duplicated dict<dict>'''
    dictfile = createmd5dict(searchDir, ext)
    listfile = list(dictfile.keys())
    duppdict = {}
    for i in range(len(listfile) - 1):
        for j in range(i + 1, len(listfile)):
            if dictfile[listfile[i]] == dictfile[listfile[j]]:
                try:
                    if listfile[i] in duppdict[dictfile[listfile[i]]]:
                        pass
                    else:
                        duppdict.setdefault(dictfile[listfile[i]], []).append(listfile[i])
                except:
                    duppdict.setdefault(dictfile[listfile[i]], []).append(listfile[i])
                try:
                    if listfile[j] in duppdict[dictfile[listfile[i]]]:
                        pass
                    else:
                        duppdict.setdefault(dictfile[listfile[i]], []).append(listfile[j])
                except:
                    duppdict.setdefault(dictfile[listfile[i]], []).append(listfile[j])
    return duppdict


if __name__ == '__main__':
    # find all *.txt file in a path and sub-path, return those duplicated
    duplicate = dupplicatedfile('D:/Workspace/Python/ThinkingPython', '.txt')
    pprint(duplicate)
