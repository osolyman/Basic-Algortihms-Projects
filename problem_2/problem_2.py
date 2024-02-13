def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list or not isinstance(number, int) or not all(isinstance(i, int) for i in input_list):
        return -1
    
    start = 0
    end = len(input_list) - 1

    while start <= end:
        mid = (start + end) // 2

        # if our target is the element of the mid index, we return that index
        if input_list[mid] == number:
            return mid
        
        # checking wether the left part is sorted
        if input_list[mid] >= input_list[start]:
            
            # if yes, we check if our target is in the left part
            if input_list[start] <= number < input_list[mid]:
                end = mid - 1

            else:
                start = mid + 1

        # checking if the right part is sorted
        else:

            # if yes, we check if our target is in the right part
            if input_list[mid] < number <= input_list[end]:
                start = mid + 1

            else:
                end = mid - 1
    
    # we return -1 if we don't find the target 
    return -1

# Test Case 1 (empty list):
print("Test Case 1: ", rotated_array_search([], 2))                                         # should return -1, because the list is empty

# Test Case 2 (very large list):
l = [(i + 1) for i in range(10000)] 
print("Test Case 2: ", rotated_array_search(l, 100))                                        # it should return 99 (index of 100)

# Test Case 3 (list of string):
print("Test Case 3: ", rotated_array_search(["a", "b", "c"], 2))                            # should return -1, because it's a list of strings

# Test Case 4 (looking for a string):
print("Test Case 4: ", rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], "test"))          # should return -1, because we don't look for an integer

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])