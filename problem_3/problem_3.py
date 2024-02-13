def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0 or not all(isinstance(i, int) for i in input_list):
        return None
    
    def mergesort(items):
        if len(items) <= 1:
            return items
        
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        left = mergesort(left)      # using recursion to sort the left half
        right = mergesort(right)    # using recursion to sort the right half

        return merge(left, right)   # merging left and right lists
    
    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        # moving through our lists until we have exhausted one
        while left_index < len(left) and right_index < len(right):
            
            # if the left's item is larger, we append it and increment the index
            if left[left_index] > right[right_index]:
                merged.append(left[left_index])
                left_index += 1

            # otherwise, we append the right's item and increment the index
            else:
                merged.append(right[right_index])
                right_index += 1

        # appending any leftovers.
        merged += left[left_index:]
        merged += right[right_index:]

        return merged
    
    sorted_list = mergesort(input_list)

    num1 = ""
    num2 = ""
    for i, num in enumerate(sorted_list):
        if i % 2 == 0: # if even index, we add it's element to num1
            num1 += str(num)

        else:           # if odd index, we add it's element to num2
            num2 += str(num)
    
    return [int(num1), int(num2)] # we return the integer value of both numbers

# Test Case 1 (empty list):
print("Test Case 1: ", rearrange_digits([]))                                 # should return None

# Test Case 2 (all digits between 0 and 9):
print("Test Case 2: ", rearrange_digits([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))     # should return [97531, 86420]

# Test Case 3 (list of the same number):
print("Test Case 3: ", rearrange_digits([2, 2, 2, 2, 2]))                    # should return [222, 22]

# Test Case 4 (list of strings):
print("Test Case 4: ", rearrange_digits(["a", "b", "c"]))                    # should return None

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]