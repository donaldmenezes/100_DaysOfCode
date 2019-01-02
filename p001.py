def sumOfMultiples(num, fact1, fact2):
    """
    Assumes num, fact1 and fact2 are non-negative. 
    Returns the sum of multiples of fact1 and fact2 below num.
    
    >>> sumOfMultiples(10,3,5)
    23
    
    """
    
    numOfMultiples1 = (num-1)//fact1
    numOfMultiples2 = (num-1)//fact2
    numOfMultiples12 = (num-1)//(fact1 * fact2)
    
    #sum of arithmetic progression
    #using arithmetic progression for constant time O(1).
    sumOfMultiples1 = numOfMultiples1 * fact1 * (1+numOfMultiples1) / 2
    sumOfMultiples2 = numOfMultiples2 * fact2 * (1+numOfMultiples2) / 2
    sumOfMultiples3 = numOfMultiples12 * fact1 * fact2 * (1+numOfMultiples12) / 2
    
    return sumOfMultiples1 + sumOfMultiples2 - sumOfMultiples3
    
    
print(sumOfMultiples(1000, 3, 5))
