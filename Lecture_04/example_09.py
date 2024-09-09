class LinearList:
    def __init__(self):
        self.data = [None, None, None, None]
        self.capacity = 4
        self.length = 0
        
    def __str__(self):
        tmp = '['
        for idx in range(self.length):
            tmp = tmp + str(self.data[idx])
            if idx != self.length - 1:
                tmp = tmp  + ','
        tmp = tmp + ']'
        return tmp
    
    def extend(self):
        if self.length == self.capacity:
            self.capacity = self.capacity * 2
            b = [None for x in range(self.capacity)]
            for idx in range(self.length):
                b[idx] = self.data[idx]
            self.data = b
        
    
    def append(self, data):
        if self.length < self.capacity:
            self.data[self.length] = data
            self.length += 1
            
        if self.length == self.capacity:
            self.capacity = self.capacity * 2
            b = [None for x in range(self.capacity)]
            for idx in range(self.length):
                b[idx] = self.data[idx]
            self.data = b
                
    def insert(self, index, data):
        if index < 0:
            print("index is wrong!")
            return
        self.extend()    
        if self.length < self.capacity:
            for idx in range(self.length, index, -1):
                self.data[idx] = self.data[idx-1] 
            self.data[index] = data       
            self.length += 1
            
    def delete(self, index):
        if index < 0 or index >= self.length:
            print("범위를 벗어났습니다.")
            return
        if index < self.length:
            for idx in range(index, self.length-1, 1):
                self.data[idx] = self.data[idx + 1]
                self.length -= 1
                
    def pop_back(self):
        if self.length > 0:
            self.length -= 1
        
            
a = LinearList()
a.append(5)
a.append(10)
a.append(0)
a.append(0)
a.insert(2, 100)
print(a)
