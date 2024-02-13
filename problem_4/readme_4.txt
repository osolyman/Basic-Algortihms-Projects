The problem here is Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, we must sort the array in a single traversal.
I iterated through the list to check for values 0 to sort them at the beginning of the list and check
for value 2 to sort them at the end of the list. In this case all values of 1 will be automatically sorted
between the last index carying value 0 and the first index carying value 2.

The array has been sorted in a single traversal. by using the Dutch National Flag algorithm.

Time Complexity is O(n), where n the number of elements of the input array.

Space Complexity is O(1), because we are not using any extra space to sort the array in.