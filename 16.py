#frequency of letters

str=input("Enter string:")

tup=tuple(str)

for s in tup:
    print("Frequency of",s,"is",tup.count(s))