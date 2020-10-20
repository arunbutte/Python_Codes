#using stack determine if the parentesis are balanced
from stack import Stack 

#copy this module file i.e., stack.py
""""
def matched(s1, s2):
    open=["(", "{", "["]
    close=[")", "}", "]"]
    count=0
    for i in range(0,3):
        if s1==open[i] and s2==close[i]:
            count+=1
        else:
            count
    if count>0:
        return True
    else:
        return False
"""

def matched(p1, p2):
    if p1 == "(" and p2 == ")" :
        return True
    elif  p1 == "{" and p2 == "}" :
        return True
    elif  p1 == "[" and p2 == "]" :
        return True
    else:
        return False
      
    
def balanced_paren(string):
    s=Stack()
    balanced=True
    i=0
    #print("1",len(string), string)
    while (i < len(string)) and balanced:
        paren=string[i]
        #print("2", string[i])
        if paren in "([{":
            s.push(paren)
            #s.push(open_paren))
            #print("4", s.print())
        else:
            if s.is_empty():
                balanced=False
                #print("5", balanced)
            else:
                left_stack=s.pop()
                #print("6", s.print(), close_paren)
                if not matched(left_stack, paren):
                    balanced=False
                    #print("7", balanced)                    
        print("8",i)               
        i+=1
        print("9",i)

    if s.is_empty() and balanced:
        return True
    else:
        return False
		

print(balanced_paren("(((({}))))"))

print(balanced_paren("[][]]]"))
print(balanced_paren("[][]"))