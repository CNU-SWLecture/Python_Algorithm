def selectionSort(ary) :
    n = len(ary)
    for i in range(0, n-1) :
        minIdx = i
    for k in range(i+1, n) :
        if (ary[minIdx] > ary[k]) :
            minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
print('정렬 전-->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후-->', dataAry)