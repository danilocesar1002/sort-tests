def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
    arr[j + 1] = temp

# Merge sort and subroutines
def merge(arr, copy, start, mid, end):
    i, j, k = start, mid, start
    while i < mid and j < end:
        if arr[i] <= arr[j]:
            copy[k] = arr[i]
            i += 1
        else:
            copy[k] = arr[j]
            j += 1
        k += 1
    
    while i < mid:
        copy[k] = arr[i]
        i += 1
        k += 1
    while j < end:
        copy[k] = arr[j]
        j += 1
        k += 1
    for i in range(start, end):
        arr[i] = copy[i]

def mergeSortHelper(arr, copy, start, end):
    if (start >= end):
        return
    if (start + 1 == end):
        copy[start] = arr[start]
        return
    # else...
    mid = (start + end) // 2

    mergeSortHelper(arr, copy, start, mid)
    mergeSortHelper(arr, copy, mid, end)
    merge(arr, copy, start, mid, end)

def mergeSort(arr):
    copy = [0] * len(arr)
    mergeSortHelper(arr, copy, 0, len(arr))
