import os
count=0
str_find=input()
#str_find='Arun'
filenames=os.listdir()
for file in filenames:
    if(file.split('.')[1]=='txt'):
        #print(file)
        #file.close()
        file=open(file, 'r')
        readnlne=file.readline()
        word_list=readnlne.split()
        #print(word_list)
        for words in word_list:
            #print(words)
            if(words==str_find):
                addedword=input()
                file=open(file.name, 'a+')
                file.writelines(addedword)
                
                print("found",file.name, file.readline())
                count+=1
                break
        break
                
        print("\n")   
    else:
        print(file)
        print("cannot be read")
        
if(count==0):
    print(f"{str_find}\t is not found")
        
    