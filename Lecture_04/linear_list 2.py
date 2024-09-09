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