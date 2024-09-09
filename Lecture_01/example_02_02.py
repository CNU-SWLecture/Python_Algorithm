x = int(input("x : "))
op = input("operator : ")
y = int(input("y : "))

if op == "+":
    ans=x+y
elif op =="-":
    ans=x-y
elif op == "*":
    ans=x*y
elif op == "/":
    ans=x/y
    
print("ans : ", ans)
