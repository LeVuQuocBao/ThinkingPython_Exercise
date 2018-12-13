# Writing simple text to file
# fout=open('output.txt','w')
# print(fout)
# line1='This here\'s the wattle \n'
# fout.write(line1)
# line2='the emblem of out land. \n'
# fout.write(line2)
# fout.close()
#  show curent directory
import os
# # show current relative path
# cwd = os.getcwd()
# print(cwd)
# # show  absolute path of a file
# print(os.path.abspath('Chapter14.py'))
# # Check if dir existed
# print(os.path.exists('D:\Workspace\Python\ThinkingPython'))
# # Check if this is a directory
# print(os.path.isdir('D:\Workspace\Python\ThinkingPython'))
# # Check if weather is a file True if existed, False if not.
# print(os.path.isfile('D:\Workspace\Python\ThinkingPython\\zipf.py'))
# # Prirnt list of file in dir
## print(os.listdir(cwd))
# FOLDER AND FILE EXAMINATE
def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
# walk('D:\Workspace\Python\\')
# CATCHING EXCEPTION
try:
    fin=open('ghost_file.txt')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Ok s.t is wrong')
# 14.2
def writeto(pstring,rstring,filename2,textlist):
    try:
        fwrite=open(filename2,'w')
    except:
        print('error open filename 2')
    try:
        for linetext in textlist:
            fwrite.write(linetext.replace(pstring,rstring))
    except:
        print('Problem with create file2 and past content')
def sed(pstring,rstring,filename1,filename2):
    try:
        fin=open(filename1)
    except:
        print('no such file1 found')
    try:
        textlist=[]
        for line in fin:
            textlist.append(line)
    except:
        print('Problem with open and input from filename 1')

    writeto(pstring,rstring,filename2,textlist)
# sed('he','some one','.\\142\\fileA.txt','.\\142\\fileB.txt')


## Add adtabase
import shelve
s=shelve.open('chater14testdb','c')
s.close()
print(s['1'])