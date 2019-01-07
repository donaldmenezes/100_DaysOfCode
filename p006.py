def diff_of_squares(num):
    
    sum_of_squares = int((num*(num+1)*(2*num+1))/6)
    
    square_of_sum = int(num*(num+1)/2)**2
    
    return square_of_sum - sum_of_squares
    

print(diff_of_squares(100))
