def palindrom_permutation(str):    
    str = str.lower()
    import itertools
    permut = [''.join(p) for p in permutations(str)]
    #print(permut)
    count = 0
    for i in range(len(permut)):
        element = permut[i]
        #print(i, element,element[::-1] )
        if element ==  element[::-1]:
            return True
            break
        else:
            pass
    return False