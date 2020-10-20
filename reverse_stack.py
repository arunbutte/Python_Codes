from stack import Stack

def rever_string(stack, input_string):    
    for i in range(len(input_string)):
        s.push(input_string[i])
    
    reverse_string=""
    while not s.is_empty():
        reverse_string=reverse_string + s.pop()
        
    return reverse_string


s=Stack()
input_string1="hello Xyzz"
print(rever_string(s, input_string1))