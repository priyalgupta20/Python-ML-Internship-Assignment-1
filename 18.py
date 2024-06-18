#anagram

str1=input("Enter string 1:")
str2=input("Enter string 2:")
set1=set(str1)
set2=set(str2)
if set1==set2:
    print("Anagrams")
else:
    print("Not anagrams")