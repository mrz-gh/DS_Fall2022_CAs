
n, m, q = map(int, input().strip().split())

sum = 0

blackpoints = set()


for _ in range(q) : 
    i, j = map(int, input().strip().split())
    
    i = i - 1
    j = j - 1

    if not ( (i, j) in blackpoints )   :
        blackpoints.add((i, j))
        if j - 1 >= 0 :
            if (i, j - 1) in blackpoints :
                if j + 1 < m : 
                    if (i, j + 1) in blackpoints:
                        sum -= 1
            else:
                if j + 1 < m :
                    if not((i, j+1) in blackpoints):
                        sum += 1

                else:
                    sum += 1

        else :
            if j + 1 < m : 
                if not((i, j+1) in blackpoints):
                    sum += 1

            else:
                sum += 1



        if i - 1 >= 0 :
            if (i - 1, j) in blackpoints :
                if i + 1 < n : 
                    if (i + 1, j) in blackpoints:
                        sum -= 1
            else:
                if i + 1 < n :
                    if not((i+1, j) in blackpoints):
                        sum += 1

                else:
                    sum += 1

        else :
            if i + 1 < n : 
                if not((i + 1, j) in blackpoints):
                    sum += 1

            else:
                sum += 1


    
    print(sum)

        
            









    

    

    
