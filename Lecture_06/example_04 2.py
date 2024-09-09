from operator import itemgetter
def makeIndex(arr, pos):
    beforeArr = 0
    
def bookSearch(arr, fData):
    pos = -1
    start = 0
    end = len(arr) - 1
    while (start <= end):
        mid = (start + end) // 2
        if fData == arr[mid][0]:
            return arr[mid][1]
        elif fData > arr[mid][0]:
            start = mid + 1
        else:
            end = mid - 1
    return arr
            
    

bookArr = [['어린왕자', '생떽쥐베리'], 
           ['이방인', '까뮈'], 
           ['부활', '톨스토이'], 
           ['신곡', '단테'], 
           ['돈키호테, 세르반테스'], 
           ['동물농장', '조지오웰'], 
           ['데미안', '헤르만헤세'], 
           ['파우스트', '괴테'], 
           ['대지', '펄벅']
           ]
print('# 책장의 도서 ==> ', bookArr)
nameIndex = makeIndex(bookArr, 0)
print('# 도서명 색인표 ==> ', nameindex)
nameIndex = makeIndex(bookArr, 0)

findName = '신곡'
if findPos != -1: