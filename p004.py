def palindromechecker(num1,num2):
    
    numberstring = str(num1*num2)
    reverse = numberstring[::-1]
    
    if numberstring == reverse:
        return True
    return False

def largest_palindrome_in_range(lower_limit, upper_limit):
    
    palindrome = 0
    for i in range(lower_limit, upper_limit+1):
        for j in range(lower_limit, upper_limit+1):
            if palindromechecker(j, i):
                if palindrome < i*j:
                    palindrome = i*j
                
    return palindrome
    
print(largest_palindrome_in_range(100, 999))
