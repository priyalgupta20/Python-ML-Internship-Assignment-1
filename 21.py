#count occurence

list=[]

n=int(input("Enter number of elements:"))

for i in range(0,n):
    ele=input("Enter number:")
    list.append(ele)

test=input("Enter element to check:")

print(test,"occurs",list.count(test),"times.")