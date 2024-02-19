from collections import deque

deq1 = deque()
deq2 = deque()

n = int(input())
L1 = list(map(int , input().split(' ')))
L2 = list(map(int , input().split(' ')))

deq1.append(L1[0])
deq2.append(L2[0])

idx1 = 1
idx2 = 1

temp1 = 0
temp2 = 0 

pop1 = False
pop2 = False

numofpops = 0

while(True) :
    
    
    if idx1 < len(L1): 
        temp1 = L1[idx1]
        if temp1 <= deq1[-1]:
            deq1.append(temp1)
            idx1 += 1
            pass
        else: 
            pop1 = True
            if numofpops == len(L1) + len(L2) - n : 
                deq1.append(temp1)
                pop1 = False
                idx1 += 1
            pass
    else:
        temp1 = -1
        pop1 = True

    if idx2 < len(L2):
        temp2 = L2[idx2]
        if L2[idx2] <= deq2[-1]:
            deq2.append(L2[idx2])
            idx2 += 1
            pass
        else :
            pop2 = True
            if numofpops == len(L1) + len(L2) - n : 
                deq2.append(temp2)
                idx2 += 1
                pop2 = False
            pass
    else:
        temp2 = -1
        pop2 = True 


   

    if pop1 and pop2 : 
        if temp1 > temp2:
            while len(deq1) != 0 and temp1 > deq1[-1]:
                deq1.pop()
                numofpops += 1
                if numofpops == len(L1) + len(L2) - n : break
                pass
            deq1.append(temp1)
            idx1 += 1
            pop1 = False
        else:
            while len(deq2) != 0 and temp2 > deq2[-1] : 
                deq2.pop()
                numofpops += 1
                if numofpops == len(L1) + len(L2) - n : break
                pass
            deq2.append(temp2)
            idx2 += 1
            pop2 = False


    if idx1 == len(L1)  and  idx2 == len(L2) :
        break


print("Answer")
for _ in range(n):
    if len(deq1) == 0:
        print(deq2.popleft(), end=' ')
    elif len(deq2) == 0: 
        print(deq1.popleft(), end=' ')
    else: 
        if deq1[0] > deq2[0] :
            print(deq1.popleft(), end=' ')
            pass
        else :
            print(deq2.popleft(), end=' ')
            pass
