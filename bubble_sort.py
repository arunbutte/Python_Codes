##########################bubble sort##########################################

#input from the user
n = int(input("size of list:"))
list = [int(input("enter the values:")) for x in range(n)]

def bubblesort(list):    
    k=0
    while(k<=(len(list)-1)):
        j=0
        i=0
        while (j<=(len(list)-2)):
            for i in range(0, (len(list)-1)):
                    if (list[i]>list[j+1]):
                        #print(i,j)
                        temp=list[j+1]
                        list[j+1]=list[i]
                        list[i]=temp
                    i=i+1
                    j=j+1
        k+=1            
    return list
                
print(bubblesort(list))