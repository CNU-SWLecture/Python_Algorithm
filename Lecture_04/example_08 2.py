class LinearList:
    def __init__(self):
        self.data = [None, None, None, None]
        self.capacity = 4
        self.length = 0
        
    def __str__(self):
        tmp = '['
        for idx in range(self.length):
            if idx != self.length:
                tmp = tmp + str(self.data[idx]) + ','
        tmp = tmp + ']'
        return tmp
    
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
                
        print(data)
            
a = LinearList()
a.append(5)
a.append(10)
a.append(0)
a.append(0)
a.append(30)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
print(a)
