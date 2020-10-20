##########################Quick sort##########################################
#input from the user
#n=4
#list=[12, 3, 10, 8]

n = int(input("size of list:"))
list = [int(input("enter the values:")) for x in range(n)]

list_length = len(list)

def partition(list,low,high):
    i = (low - 1)
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] =  list[j], list[i]
    list[i+1],list[high] = list[high],list[i+1]
    return (i+1)

def quickSort(list, low, high):
    if low < high:
        partition_index = partition(list,low,high)
        quickSort(list, low, partition_index - 1)
        quickSort(list, partition_index + 1, high)

quickSort(list, 0, list_length -1)
print(list)
    
    