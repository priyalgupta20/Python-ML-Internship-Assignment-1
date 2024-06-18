#calculator

a=float(input("Enter number 1:"))
b=float(input("Enter number 2:"))
op=input("Enter operator:")

if op=="+":
    print("Sum is",a+b,end=".")
elif op=="-":
    print("Difference is",a-b,end=".")
elif op=="*":
    print("Product is",a*b,end=".")
elif op=="/":
    if b!=0:
        print("Quotient is",a/b,end=".")
    else:
        print("Denominator cannot be zero.")
else:
    print("Invalid input")