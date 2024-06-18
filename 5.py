#print in text file

str=input("Enter string: ")

name=open('Q5 demo.txt','w')
print("String is",str,end='.',file=name)