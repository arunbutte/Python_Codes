def cutby_byte(string, b1, b2):
    str=[]
    for words in string:
        str.append(words)
    str.pop(b1)
    print(str)
    if(b1>b2):
        str.pop(b2)
    else:
        b2=b2-1
        str.pop(b2)
    return print(str) 

cutby_byte('Kirlosker', 6, 3)