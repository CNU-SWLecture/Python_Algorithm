class LinearList:
    def __init__(self):
        self.data = [None, None, None, None]
        self.capacity = 4
        self.length = 0
        
    def __str__(self):
        tmp = '['
        for idx in range(self.length):
            tmp = tmp + str(self.data[idx]) + ", "
        tmp = tmp + ']'
        return tmp
            
a = LinearList()
b = LinearList()

print(a)
# a를 출력하면 나올 문자열을 정의하기 위해서 '__str__'이하 코드를 사용함