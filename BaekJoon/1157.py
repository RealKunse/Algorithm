dictionary = {'a': 0}

word = input()
word = word.upper()
for i in word:
    if i not in dictionary.keys():
        dictionary[i] = 1
    else:
        dictionary[i] = dictionary[i] + 1

answ = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

if answ[0][1] == answ[1][1]:
    print('?')
else:
    print(answ[0][0])