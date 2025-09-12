def merge_sort(data):
    if len(data) < 2:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


def merge(left, right):
    i = j = 0
    final = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1

    final.extend(left[i:])
    final.extend(right[j:])

    return final


print(merge_sort((50, 23, 56, 10, 30, 88, 79)))
