def toBinary(n): 
  
    # Check if the number is Between 0 to 1 or Not 
    if(n >= 1 or n <= 0): 
        return "ERROR"
  
    answer = "" 
    frac = 0.5
    answer = answer + "."
  
    # Setting a limit on length: 32 characters. 
    while(n > 0): 
  
        # Setting a limit on length: 32 characters 
        if(len(answer) >= 32): 
            return "ERROR"
  
        # Multiply n by 2 to check it 1 or 0 
        b = n * 2
        print(b)
        if (b >= 1): 
  
            answer = answer + "1"
            n = b - 1
            print(1, answer, n)
  
        else: 
            answer = answer + "0"
            n = b 
            print(2, answer, n)
  
    return answer