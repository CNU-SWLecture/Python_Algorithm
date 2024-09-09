def seqSearch(data, find_data):
    idx = -1
    for i in range(len(data)):
        if data[i] == find_data:
            idx = i
    return idx
    
data = [188, 150, 168, 162, 105, 120, 177, 50]
find_data1 = 120
find_data2 = 50

idx1 = seqSearch(data, find_data1)
if idx1 -1:
    print('찾는 데이터가 없습니다.')
else:
    print(idx1)
    print(data[idx1])

idx2 = seqSearch(data, 50)