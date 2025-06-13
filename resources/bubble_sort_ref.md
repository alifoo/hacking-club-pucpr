# Bubble sort implementation references

## With 2 for loops
```python
def bubble_sort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
```

## With while loop (and - 1).

In my opinion, it is less clean.
```python
def bubble_sort(arr):
    swapped, end = True, len(arr)
    while swapped:
        swapped = False
        for i in range(1, end):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i-1]
                swapped = True
        end -= 1
    return arr
```
