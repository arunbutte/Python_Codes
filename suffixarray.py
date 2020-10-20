def suffixarray(string):
    suffix_arrays=[]
    for i in range(0,len(string)):
        suffix_arrays.append(string[i:])
    return print(suffix_arrays)

suffixarray("arun")