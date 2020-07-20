#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It is O(n), the number of operations for the loop will grow at the same rate than the input.


b)  O(n log n), the first loop will increase its operations in n fashion (size of array) and the second one will be at a log of n speed, due to j doubling its size every time.


c) O(n), because its decreasing by 1 each time, meaning that it will take the same time of recursions as the size of the input. 

## Exercise II


for n stores or the building, go to the median, drop an egg, if it breaks then go to the [:median]//2.
 if it doesnt break then go to the [median:]//2.
 
 repeat proces until you find the floor where it doesnt/does break depending on first result. 

 it would be a binary search, so Runtime would be O(log n)