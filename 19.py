#remove punctuations

str=input("Enter string...")
punc=''',.?/'";:!@#$%^&*-_`~(){}[]<>'''

for p in str:
    if p in punc:
        str=str.replace(p," ")

print(str)