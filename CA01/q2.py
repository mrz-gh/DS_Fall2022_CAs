def main ():
    n = int(input())
    L = []
    Dic = dict()
    for i in range(n):
        first_letter = input()[0]
        if first_letter in Dic.keys():
            Dic[first_letter] += 1
        else:
            Dic.update({first_letter : 1})
        pass

    l = []
    Occurrence : bool = False
    for key in Dic.keys():
        if Dic[key] >= 5:
            l.append(key)
            Occurrence = True

   
    if Occurrence is False:
        print("How long must I suffer")
    else:
        print(''.join(sorted(l)))


if __name__ == "__main__":
    main()