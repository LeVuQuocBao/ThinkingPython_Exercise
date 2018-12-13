import os
def runcmd(*arg):
    ''' A short function to execute cmd command
        [cmdin]<str> and retrun output<str>, report
        run status if needed. runcmd('command','rp')'''
    if len(arg)==2:
        cmdin=arg[0]
        statusout=arg[1]
    if len(arg)==1:
        cmdin = arg[0]
        statusout='No'
    fp=os.popen(cmdin)
    out=fp.read().strip()
    st=fp.close()
    if statusout=='rp':
        return (out,st)
    elif statusout=='No':
        return (out)
if __name__== '__main__':
    output=runcmd('cd','rp')
    print(output)
print(__name__)