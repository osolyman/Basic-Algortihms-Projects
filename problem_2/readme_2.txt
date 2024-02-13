Searching for a target in a Rotetd Sorted Array:
for example:
            Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

In my solution I used binary search to find the index of a given number by searching in a rotated sorted array.
I calculated the mid and checked if the array at the index mid equals to, less or greater than the given number and depending
on which case that was, the start or the end of the list I search from or to gets changed.

Time Complexity could be O(log(n)), where n is the size of input list.
In the while loop, the search space is halved, leading to a logarithmic time complexity.

Space complexity is O(1) because the algorithm uses only a constant amount of extra space regardless of the input size.