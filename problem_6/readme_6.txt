In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time.

initializing the min and max values with the first element of the list,
then we compare the min and max with every element in the list by doing
a single traversal. each time we compare the elements we update the min and max
if it's necessary.

during this single traversal, we have a time complexity of O(n), where n is the
number of elements of the list.

The space complexity is O(1) because the function uses a constant amount of extra 
space regardless of the size of the input list. 