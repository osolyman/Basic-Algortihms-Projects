import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints or not all(isinstance(i, int) for i in ints):
        return None
    
    minimum = maximum = ints[0]

    # itrating through list to compare every 2 integers
    for num in ints[1:]:
        
        if num < minimum:
            minimum = num
        
        elif num > maximum:
            maximum = num
            
    return minimum, maximum

# Test Case 1 (empty inputs):
print("Test Case 1: ", get_min_max([]))                       # should return None, because it's an empty list

# Test Case 2 (very large numbers):
l = [i for i in range(6, 10000)]
print("Test Case 2: ", get_min_max(l))                        # should return (6, 9999)

# Test Case 3 (list of the same numbers):
print("Test Case 3: ", get_min_max([7, 7, 7, 7, 7]))          # should return (7, 7), minimum and maximum have the same value l3[0]

# Test Case 4 (list of strings):
print("Test Case 4: ", get_min_max(["a", "b", "c"]))          # should return None

### Example Test Case of Ten Integers
                
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")