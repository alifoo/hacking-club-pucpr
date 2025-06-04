*This resource is a work in progress. In the future, I will add more complete explanations, a Brazillian Portuguese verion and images.*

## O(log(n))

An algorithm is generally a log n if it's a divide and conquer type. They grow according to the input size, but only according to the log of the input.


### Sorting algorithms

#### Bubble sort
Easy to implement but very slow. It has O(nˆ2) because it has a while outer loop and for inner loop. Implementation:
```
def bubble_sort(arr):
    swapping, end = True, len(arr)
    while swapping:
        swapping = False
        for i in range(1, end):
            if arr[i - 1] > arr[i]:
                swap = arr[i - 1]
                arr[i - 1] = arr [i]
                arr[i] = swap
                swapping = True
        end -= 1
    return arr
```
#### Merge sort (divide and conquer)

A little bit faster. O(n log n) because it needs to be called recursively log n times. It occupies more spsace in memory (more space complexity) because it requires copies of the original list.
Split the list into 2 parts untit we have several lists of 1 item, then we start merging them back together.

Implementation:
```
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    half = len(nums) // 2
    sorted_left_side, sorted_right_side = merge_sort(nums[:half]), merge_sort(nums[half:])
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final
```

A log n algorithm divide the work. A n log n algorithm do a logarithmic work for every item of a list.
How many times can you divide by n before reaching 1? log n times. Id. est. log n recursion levels.

Total work = log(n) levels × n work per level
            = O(n log n)

#### Insertion sort (nˆ2) - A look back algorithm
It's slow, but really good for small lists. Stable, does not change the relative order of elements with equal keys, can sort a list as it receives it. Tiny memory footprint.
```
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums
```
The outer loop always executes n times, and the inner loop depends on the input. O average case é 0(nˆ2) porque o inner loop executa geralmente metade do tempo.
If the array is pre-sorted, it will be O(n) because the inner loop will never execute.

#### Quicksort (n log n) - Default sorting for PostgreSQL

Used in the real world. Divide and conquer. partition() is 0(n), the complexity of quicksort is dependent on how many times partition() is called. The worst case is if the input is already sorted, because then partition would be called n times, resulting in a O(nˆ2) algorithm.
```
def quick_sort(nums, low, high):
    if low < high:
        pivot = partition(nums, low, high)
        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i + 1
```

To prevent a 0(nˆ2), we can basically make a shuffling before sorting. Or selecting three elements: the first, middle and last of each partition is chosen and the median is found between them, that then is used as pivot.

#### Selection sort
```
def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(smallest_idx + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]

    return nums
```


## Polynomial vs. Exponential
Broadly speaking, algorithms can be classified into two categories:

"Polynomial time"
"Exponential time"
polynomial vs exponential

Technically O(n!) is "factorial" time, but let's lump them together for simplicity

An algorithm runs in "Polynomial time" if its runtime does not grow faster than n^k, where k is any constant (e.g. n^2, n^3, etc) and n is the size of the input.

To put it simply, polynomial time algorithms can be useful, but exponential time algorithms are almost always too slow to be practical (unless you're trying to force someone to be slow, like in the case of cryptography and security). Even when n is as low as 20, 2^n is already over a million!

Ou seja, Polynomial time são os algoritmos práticos para resolver em computadores.

# Big O Categories Review
Big-O	Name	Description

O(1)	constant	Best The algorithm always takes the same amount of time, regardless of how much data there is. Example: Looking up an item in a list by index

O(log n)	logarithmic	Great Algorithms that remove a percentage of the total steps with each iteration. Very fast, even with large amounts of data. Example: Binary search

O(n)	linear	Good 100 items, 100 units of work. 200 items, 200 units of work. This is usually the case for a single, non-nested loop. Example: unsorted array search.

O(n log n)	"linearithmic"	Okay This is slightly worse than linear, but not too bad. Example: mergesort and other "fast" sorting algorithms.

O(n^2)	quadratic	Slow The amount of work is the square of the input size. 10 inputs, 100 units of work. 100 Inputs, 10,000 units of work. Example: A nested for loop to find all the ordered pairs in a list.

O(n^3)	cubic	Slower If you have 100 items, this does 100^3 = 1,000,000 units of work. Example: A triple nested for loop to find all the ordered triples in a list.

O(2^n)	exponential	Horrible We want to avoid this kind of algorithm at all costs. Adding one to the input doubles the amount of steps. Example: Brute-force guessing results of a sequence of n coin flips.

O(n!)	factorial	Even More Horrible The algorithm becomes so slow so fast, that is practically unusable. Example: Generating all the permutations of a list

