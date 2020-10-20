##########################Merge sort##########################################
#input from the user
#n=4
#list=[12, 3, 10, 8]
n = int(input("size of list:"))
list = [int(input("enter the values:")) for x in range(n)]
def mergersort(list):
    if len(list)>1:
        div=len(list)//2 #absolute  divide
        lsl=list[:div]
        rsl=list[div:]

        mergersort(lsl)
        mergersort(rsl)

        i=0
        j=0
        k=0
        while i < len(lsl) and j < len(rsl):
            if (lsl[i] <= rsl[j]):
                list[k]=lsl[i]
                i=i+1
            else:
                list[k]=rsl[j]
                j=j+1
            k=k+1

        while i < len(lsl):        
            list[k]=lsl[i]
            i=i+1
            k=k+1

        while j < len(rsl):        
            list[k]=rsl[j]
            j=j+1
            k=k+1

    return list

print(mergersort(list))            