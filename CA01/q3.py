def main(n, m):
    ans = 0
    while True:
        rem = n%m
        if rem == 0:
            ans += 0
            break
        elif m % rem == 0 :
            ans += (m // rem - 1) * rem
            break
        else :
            temp = (m // rem) * rem
            ans += temp
            n = rem
            m = m - temp
            if m < 1 : 
                break

    print(ans)

if __name__ == "__main__":
    [n, m] = map(int, input().split(' '))
    main (n, m)
    
