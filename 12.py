#sum of digits

def sum_digits(n):
    sum=0
    for i in str(n):
        sum=sum+int(i)
    return sum

num=input("Enter number:")
print("The sum of the digits of the number is",sum_digits(num))