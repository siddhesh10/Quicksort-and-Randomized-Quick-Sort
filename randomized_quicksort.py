#randomized quicksort

import random
def partition(arr,low,high):
    pindex = low         
    pivot_index = random.randint(low,high-1)
    pivot=arr[pivot_index]
    
    arr[high],arr[pivot_index]=arr[pivot_index],arr[high]
    
    for j in range(low , high):
 
        if   arr[j] <= pivot:
            arr[pindex],arr[j] = arr[j],arr[pindex]
            pindex = pindex + 1
 
    arr[pindex],arr[high] = arr[high],arr[pindex]
    return (pindex)
 

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
print(arr)
