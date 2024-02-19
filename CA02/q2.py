from collections import deque
def main(n, L):
    deq1 = deque(L)
    deq2 = deque()
    start = 0
    end = -1
    while (True):
        
        while True:
            if len(deq1) == 0 : return
            temp = deq1.popleft()
            if temp == 0 : start += 1
            if temp > 0 :
                deq2.append(temp - 1)
                break

        end = start
        while True :

            if len(deq1) != 0 : element = deq1.popleft()
            else : break

            if element >= temp:
                deq2.appendleft(element - 1)
                end = end + 1
            else:
                deq1.appendleft(element)
                break


        deq1.extendleft(deq2)
        deq2.clear()

        str = f"{start + 1} {end + 1}"
        print (str)    

        



if __name__ == "__main__":
    n = int(input())
    L = list(map(int , input().split(' ')))
    main(n, L)