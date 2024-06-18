#min and max values

set=set()

n=int(input("Enter number of elements:"))

for i in range(0,n):
    ele=int(input("Enter number:"))
    set.add(ele)

min=min(set)
max=max(set)

print("The minimum value is:",min)
print("The maximum value is:",max)