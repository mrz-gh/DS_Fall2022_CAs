def CompareStr (In1 : str, In2: str):
    for i in range (min(len(In1), len(In2))):
        if (In1 < In2) or (In1 == In2):
            return True
        elif In1 > In2:
            return False
        pass    
    pass


def Merge (A : list, Index : list, start : int, end: int) -> None :
    middle = (start + end) // 2
    Left : list = A[start : middle + 1] 
    Right : list = A[middle + 1 : end + 1]
    LeftIndex : list = Index[start : middle + 1] 
    RightIndex : list = Index[middle + 1 : end + 1]
    Left.append('zzzzzzzzzzzzzzzz')
    Right.append('zzzzzzzzzzzzzzzz')
    i = j = 0
    for k in range (start, end + 1, 1):
        if CompareStr(Left[i], Right[j]) :
            A[k] = Left[i]
            Index[k] = LeftIndex[i]
            i = i + 1
            pass
        else:
            A[k] = Right[j]
            Index[k] = RightIndex[j]
            j = j + 1
            pass
        pass

def MergeSort(A : list, Index :list,  start : int , end : int) -> None :
    if start < end :
        middle = (start + end) // 2
        MergeSort (A, Index= Index, start= start, end= middle)
        MergeSort (A, Index= Index, start= middle + 1, end= end)
        Merge(A, Index= Index, start= start, end= end)
        pass
    pass

    

if __name__ == "__main__":

    [r, _] = map(int, input().split(' '))
    Columns = input().split(',')
    Data : list[list] = []
    for i in range (r) :
        L = input().split(',')
        Data.append(L)
        pass

    Li = []
    [_, _, Keyword] = input().split(' ')
    j = Columns.index(Keyword)
    for i in range(r):
        Li.append(Data[i][j])
        pass

    Index = list(range(r))
    MergeSort(Li, Index, 0, r-1)

    for i in Index:
        print(','.join(Data[i]))

    pass