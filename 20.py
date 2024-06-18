#sum of list elements

list=[]

n=int(input("Enter number of elements:"))

for i in range(0,n):
    ele=int(input("Enter number:"))
    list.append(ele)

sum=sum(list)
print("Sum is",sum,end=".")