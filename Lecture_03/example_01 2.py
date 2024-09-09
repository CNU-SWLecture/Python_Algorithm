# def addNumber(n):
#     if n <= 1:
#         return 1
#     return addNumber(n-1) + n
    
# print(addNumber(10))

def mulNumber(n):
    if n<= 1:
        return 1
    return mulNumber(n-1) * n

print(mulNumber(10))