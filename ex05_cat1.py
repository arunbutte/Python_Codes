filename1='new2.txt'
filename2='new.txt'
filename3=input("enter the destination file")
#open('new5.txt')
f3=open(filename3, 'w+')

f1=open(filename1, 'r')

f3.writelines(f1)
f3.writelines(" ")
f2=open(filename3, 'r')
f3.writelines(f2)
    
print(f3.readline())