import heapq



(n, q, k) = map(int, input().strip().split(' '))
arr =  list(map(int, input().strip().split(' ')))

minheap = []
maxheap = []


if n >= k:
    arr = sorted(arr)
    minheap = arr[k:]
    
    arr = arr[0:k]
    arr.reverse()
    maxheap = list(map(lambda x : -x , arr))


else:
    maxheap = list(map(lambda x : -x, arr))
    heapq.heapify(maxheap)



for i in range(q):
    line = input().strip()

    if line[0] == 'p':
        if n < k:
            print(-1)
        else:
            print(-maxheap[0])



    elif line[0] == '+':
        (_, x) = line.split(' ')
        x = int(x)
        
        if n < k :
            heapq.heappush(maxheap, -x)            

        else:
            if x < -maxheap[0]:
                heapq.heappush(minheap,  -(heapq.heapreplace(maxheap, -x)))
            else : 
                heapq.heappush(minheap, x)


        n += 1



    elif line[0] == '-':
        if n >= k :
            heapq.heappop(maxheap)
            n -= 1
            if len(minheap) != 0:
                heapq.heappush(maxheap, -(heapq.heappop(minheap)))
