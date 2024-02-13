def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) == 0 or not all(isinstance(i, int) for i in input_list):
        return None

    next_pos_0 = 0 # pointer for next position of 0
    front_index = 0
    next_pos_2 = len(input_list) - 1 # pointer for next position of 2

    # iterate through the list
    while front_index <= next_pos_2:

        # we swap the current element with the element at next_pos_0
        # if current_element is 0
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1             # now we increment it
            front_index += 1            # now we increment it

        # if current element is 1, we just move to the next element
        elif input_list[front_index] == 1:
            front_index += 1
        
        # if current element is 2, we swap it with element at next_pos_2
        # and now we decrement next_pos_2    
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        
        else:
            return None
    
    return input_list

# Test Case 1:
print("Test Case 1: ", sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))         # should return [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

# Test Case 2 (empty list):
print("Test Case 2: ", sort_012([]))                                        # should return None

# Test Case 3 (input includes other numbers):
print("Test Case 3: ", sort_012([0, 0, 2, 2, 2, 1, 1, 3, 2, 0, 4]))         # should return None, because we used other numbers like 3, 4

# Test Case 4 (list of strings):
print("Test Case 4: ", sort_012(["a", "b", "c", "a"]))                      # should return None

'''def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) '''