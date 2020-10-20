def stringcomp(str):
    dict_str = {s:0 for s in list(dict.fromkeys(str))}
    output = ""
    for s in str:
        dict_str[s] += 1
    for s in dict_str:
        i = dict_str[s]
        print(f"{s}{dict_str[s]}")
        #output += s + str(i)
    
    