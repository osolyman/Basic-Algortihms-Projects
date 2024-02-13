def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    
    if isinstance(number, str):
        return -1
    
    if number < 0 or not isinstance(number, int):
        return -1
    
    start = 1
    end = number

    while start <= end:
        mid = (start + end) // 2
        mid_square = mid * mid

        # returning mid if it's square is equal to the number
        if mid_square == number:
            return mid
        
        # if the square of mid is less than the number, then it lies on the right half of that mid
        elif mid_square < number:
            start = mid + 1
            result = mid

        # otherwise, it lies on the left half of the mid    
        else:
            end = mid - 1
    
    return result

# Test Case 1 (null input):                  # should return 0
result_1 = sqrt(0)
if result_1 == -1:
    print("Test Case 1: Invalid input: Please enter a non-negative integer.")
else:
    print("Test Case 1:", result_1)              

# Test Case 2 (very large number):           # should return 1252       
result_2 = sqrt(1568212)
if result_2 == -1:
    print("Test Case 2: Invalid input: Please enter a non-negative integer.")
else:
    print("Test Case 2:", result_2)

# Test Case 3 (negative number):             # should print "Invalid input: Please enter a non-negative integer."
result_3 = sqrt(-85)         
if result_3 == -1:
    print("Test Case 3: Invalid input: Please enter a non-negative integer.")
else:
    print("Test Case 3:", result_3)

# Test Case 4 (string):                      # should print "Invalid input: Please enter a non-negative integer."
result_4 = sqrt("test")         
if result_4 == -1:
    print("Test Case 4: Invalid input: Please enter a non-negative integer.")
else:
    print("Test Case 4:", result_4)         

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")