import sys

num = sys.stdin.readline().strip()
num_list = [int(x) for x in num]

num_list.sort(reverse=True)

for i in num_list :
    print(i, end ='')