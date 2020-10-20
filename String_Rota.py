def rotation_string(str):
    l  = []
    #str = ""
    for i in str:
        l.append(i)
    #print(l)
    for j in range(len(l) // 2):
        a = l[j]
        b = l[-(j+1)]
        l[j] = b
        l[-(j+1)] = a
    return l