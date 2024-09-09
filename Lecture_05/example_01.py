class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [None for _ in range(self.size)]
        self.top = -1
    
    def isFull(self):
        if self.size - 1 == self.top:
            return True
        else:
            return False
    
    def push(self, new_data):
        if self.isFull() == True:
            print('스택이 가득 찼습니다.')
            return
        self.top =+ 1
        
        
    def print(self):
        print(self.data)
a = Stack(10)
b = Stack(5)
b.push('커피')
b.push('주스')
print()
    