import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n) :
    command = input().strip()
    if ' ' in command :
        command, num = command.split(" ")
    if command == 'push' : stack.append(int(num))
    if command == 'top' :
        if not stack : print(-1)
        else : print(stack[len(stack) - 1])
    if command == 'pop' :
        if not stack : print(-1)
        else : print(stack.pop())
    if command == 'size' : print(len(stack))
    if command == 'empty' :
        if not stack : print(1)
        else : print(0)