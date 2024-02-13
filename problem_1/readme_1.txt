In my solution I used binary search to find the square root. By looping through numbers between 1 and the given number.
I calculated the mid and checked if the mid number squared equals to, less or greater than the given number. and depending
on which case that was, the start or the end of the number I search from or to gets changed.

Time Complexity could be O(log(n)). In the while loop, the search space is halved, leading to a logarithmic time complexity.

Space Complexity is O(1), because the algorithm uses only a constant amount of extra space regardless of the input size.

