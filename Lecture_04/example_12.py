from example_09 import LinearList

a = LinearList()
select = -1
while select != 4:
    select = int(input("선택하세요 (1. 추가, 2: 삽입, 3: 삭제, 4: 종료) --> "))
    if select == 1:
        data = input("추가할 데이터 --> ")
        a.append(data)
        print(a)
    elif select == 2:
        pos = int(input('삽입할 위치 --> '))
        data = input('추가할 데이터 --> ')
        a.insert(pos, data)
        print(a)
    elif select == 3:
        
        pass
    else:
        pass
a.append(5)
a.append(4)
a.append(0)
print(a)