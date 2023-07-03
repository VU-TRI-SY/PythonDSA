#selection sort, insertion sort, bubble sort: O(n^2)
#merge sort

def selection_sort(arr): #O(n^2)
    n = len(arr)
    # i is the first index in the unsorted segment
    for i in range(n): 
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def merge(arr, left, mid, right):
    #left part: [left, mid]
    #right part: [mid+1, right]
    left_part = arr[left:mid+1] #left --> (mid+1)-1
    right_part = arr[mid+1:right+1]
    idx = left
    i = 0
    j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            arr[idx] = left_part[i]
            i += 1
        else:
            arr[idx] = right_part[j]
            j += 1
        idx += 1

    while i < len(left_part):
        arr[idx] = left_part[i]
        i += 1
        idx += 1
    
    while j < len(right_part):
        arr[idx] = right_part[j]
        j += 1
        idx += 1


def merge_sort(arr, left, right): #left and right just are identifier
    # sort the array in [left, right]
    # if left > right:
    #     print("Invalid case")
    #     return
    
    if right - left + 1 > 1: #the part has more than 1 elements  
        mid = (left + right) // 2
        merge_sort(arr, left, mid) #apply merge sort for the left part
        merge_sort(arr, mid+1, right) #apply merge sort for the right part
        merge(arr, left, mid, right) #merge left and right part

# arr = [1,5,8,0,3,6,9]
arr = [5,4, 3,2,1,0] #list
merge_sort(arr, 0, len(arr)-1)
print(arr)


# bubble sort: O(n^2)
# merge sort: O(n.log(n))