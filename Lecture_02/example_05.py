x=int(input("x: "))
op=input("op: ")
y=int(input("y: "))

if op == "+":
    z=x+y
elif op == "-":
    z=x-y
elif op == "*":
    z=x*y
elif op == "/":
    z=x/y
else:
    print("연산자가 잘못 입력되었습니다.")

print(x, op, y, "=", z)