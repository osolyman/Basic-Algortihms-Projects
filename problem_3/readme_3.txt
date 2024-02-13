The problem here is to rearrange array digits so as to form two number such that their sum is maximum. Return these two numbers.
for example:
            for [1, 2, 3, 4, 5]
should Return   [531, 42]

in this solution the mergesort algorithm is used to sort the input list. which has time Complexity
of O(nlog(n)). after that using the function merge to merge 2 sorted lists, which has time Complexity
of O(n), where n is the number of elements in the lists.

Time Complexity could be O(nlog(n))

Space Complexity is O(n), where n is the size of the array. In mergesort algorithm we created temporary arrays.