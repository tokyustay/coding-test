array = [0]*5
lenth = []

for i in range(0,5) :
    sen = input()
    array[i] = [x for x in sen]
    lenth.append(len(array[i]))

max_len = max(lenth)


for i in range(0,max_len) :
    for j in range(0, 5) :
        if len(array[j]) > i :
            print(array[j][i], end='')

