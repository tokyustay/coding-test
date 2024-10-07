n = int(input())

for i in range(n) :
    s = input()
    s += " "
    stack=[]
    for j in s :
        if j!= " " :
            stack.append(j)
        else :
            while stack:
                print(stack.pop(), end ='')
            print(' ', end='')