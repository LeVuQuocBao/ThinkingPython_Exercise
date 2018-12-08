import random
from Chapter8 import countCh


def findCh_mat(string, charater):
    i = 0
    locmat = []
    while not (i > len(string) - 1):
        # print(str(i)+string[i])
        if string[i] == charater:
            # print('found'+str(i))
            locmat.append(i)
        i += 1
    return locmat


fin = open('words_simple.txt')
i = 0
wordlist = []
for line in fin:
    word = line.strip()
    if len(word) > 4 and len(word) < 8:
        wordlist.append(word);
# CREATE RANDOM WORD
randn = random.randint(0, len(wordlist))
ANSWER = wordlist[randn]
# print(ANSWER)
foundALL = []
life = 6
tried = []
fail=0
# Main program
while True:
    if fail == 2:
        for i in range(len(ANSWER)):
            if not (i in foundALL):
                print('Clue:'+ANSWER[i])
                break
    for i in range(len(ANSWER)):
        if i in foundALL:
            print(ANSWER[i], end='')
        else:
            print('#', end='')
    print('\n')
    print(str(life) + 'life left')
    print('Tried: ', end='')
    print(tried)
    # print(foundALL)
    # mask='#'*len(ANSWER)
    # print(mask)
    G = input('Guest character?')
    if G in tried:
        print('Already try this, others please..')
    else:
        tried.append(G)
        print('%d %s in the answer' % (countCh(ANSWER, G), G))
        found = findCh_mat(ANSWER, G)
        if len(found) == 0:
            life -= 1
            fail = fail + 1
        else:
            fail = 0
        foundALL.extend(found)
        # print(foundALL)
        # print()
        if len(foundALL) == len(ANSWER):
            print('Congratulation you found the word ' + ANSWER + ', good job!')
            break
        if life == 0:
            print('Sorry, It''s ' + ANSWER + ', Game over!')
            break
        print('\n' * 80)
