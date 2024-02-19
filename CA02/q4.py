from collections import deque

n = int(input())
L = list(map(int ,input().split(' ')))
L.insert(0, 0)
L.append(0)
stack = deque()


Ans_L = []

for i in range(n+1):
    temp = L[i+1] - L[i]
    if temp > 0:
        for _ in range(temp) : stack.append(i+1)
    
    elif temp < 0 : 
        for _ in range(-temp) : 
            Ans_L.append((stack.pop(), i))


Ans_L = sorted(Ans_L)

for (start, end) in Ans_L:
    print(f"{start} {end}")

