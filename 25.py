#print text from one file to another

file_old=open("Q6 demo.txt",'r')

f=file_old.read()

file_new=open('Q25 demo.txt','w')

print(f,file=file_new)