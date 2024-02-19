import heapq

[n, t] = list(map(int, input().split(' ')))
In =  map(int, input().split(' '))

Li = [(enqueue_time, idx) for idx, enqueue_time in enumerate(In)]
Li = sorted(Li, key=lambda x : x[0])

ans = [0]*len(Li)

heap = []


cur_time = 0

i = 0

while i < len(Li) :
    enq_time , idx = Li[i]

    if len(heap) == 0:
        heapq.heappush(heap, idx)
        cur_time = enq_time + t
        i += 1

    elif idx < heap[0] and enq_time <= cur_time:
        ans[heapq.heappop(heap)] = cur_time
        heapq.heappush(heap, idx)
        cur_time += t
        i += 1

    elif enq_time <= cur_time:
        heapq.heappush(heap, idx)
        i += 1

    else :
        ans[heapq.heappop(heap)] = cur_time
        cur_time += t

    
    if i == len(Li):
        while len(heap) != 0:
            ans_idx = heapq.heappop(heap)
            ans[ans_idx] = cur_time
            # update cur_time
            cur_time += t


    
for val in ans:
    print(val, end=' ')

 