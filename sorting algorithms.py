

from heapq import heapify, heappop


arr = [4,5,78,34,12,76,34,-4,0]



def selection_sort(arr): #Time Complexity: O(N^2), Space is O(1)
    '''
    Steps to selection Sort: 
    - Find the minimum element in the array, bring it to the front
    - Now move your index to 2, and find the next minimum and bring it to 2 
    - Keep going until you reach the end. You are basically doing a double loop
    - https://www.youtube.com/watch?v=xWBP4lzkoyM 
    '''
    for i in range(len(arr)):
        min_index = i
        for j in range(min_index + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j 
        temp = arr[i] 
        arr[i] = arr[min_index]
        arr[min_index] = temp 
        
    return arr

print("Selection Sort")
print(selection_sort(arr))



def bubble_sort(arr): #Time Complexity: O(N^2), Space Complexity O(1)
    '''
    Steps to Bubble Sort:
    - Keep swapping smallest to largest elements in pairs until u reach the last element (thats ur first index). 
    - Now shift ur index to one smaller, and keep swapping elements 
    - Keep doing this until ur index is the first element
    - https://www.youtube.com/watch?v=nmhjrI-aW5o
    '''
    n = len(arr)
    
    for i in range(n):
        swap = False 
        
        for j in range(0, n - i - 1): 
            if arr[j] > arr[j+1]:
                temp = arr[j] 
                arr[j] = arr[j+1]
                arr[j+1] = temp 
                swap = True 
        
        if not swap:
            break 
    
    return arr 

print("Bubble Sort")
print(bubble_sort(arr))



def insertion_sort(arr): #Time Complexity is O(N^2), Space Complexity is O(1)
    '''
    Steps to Insertion Sort
    - Take the first element, and find its place in the array by moving the other elements back by 1 space.
    - Keep doing with all elements
    - The firrst half would depict the sorted array and the second half would be unsorted array. 
    '''
    for i in range(len(arr)):
        current_element = arr[i] 
        j = i - 1 
        while j >= 0 and current_element < arr[j]:
            arr[j+1] = arr[j] 
            j -= 1 
        arr[j+1] = current_element
    return arr

print("Insertion Sort")
print(insertion_sort(arr))  

        

def merge_sort(arr): #Time Complexity is O(NLOGN), Space Complexity O(N)
    '''Steps to Merge Sort
    - Split array into equal halves
    - Keep going until it is all single elements 
    - Merge to form sorted subarrays, and eventually a sorted array 
    - https://www.youtube.com/watch?v=JSceec-wEyw
    '''
    if len(arr) > 1:
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:] 
        
        merge_sort(L)
        merge_sort(R) 
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1 
            else:
                arr[k] = R[j]
                j += 1 
            k += 1 
            
        while i < len(L):
            arr[k] = L[i] 
            k += 1 
            i += 1 
            
        while j < len(R):
            arr[k] = R[j] 
            k += 1 
            j += 1    

    return arr
print("Merge Sort")
print(merge_sort(arr))     




def quick(arr, low, high): #Time Complexity is O(n^2) WORST case, average O(NlogN), O(1) if we don't consider auxillary space for recursion, else O(N)
    '''
    Steps for Quick Sort (Divide and Conquer)
    - Pick a pivot (last point)
    - Go through each element and compare to pivot. If more do nothing. If less than pivot then swap with the prev. element (do with two pointers, i is lagging and j is forward)
    - Place the pivot in the right position (the current position of i)
    - Then look at elements after and before old pivot, and they become new pivot elements. Now redo for each of these until the resultant is a sorted array. 
    - https://www.youtube.com/watch?v=PgBzjlCcFvc
    '''
    pivot = arr[high] #Last element is pivot
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] <= pivot: 
            i = i + 1 
            temp = arr[i]
            arr[i] = temp 
            arr[j] = arr[i] 
    temp = arr[i+1]
    arr[i+1] = temp 
    arr[i+1] = pivot
    arr[high] = temp 
    
    return i + 1 

def quickSort(arr, low, high):
    if low < high:
        pivot = quick(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return arr
        
def quick_sort(arr):
    return quickSort(arr, 0, len(arr) - 1) 


print("Quick Sort")
print(quick_sort(arr))   


def heap_sort(arr): #Time Complexity: O(NlogN), Recursive Space: logN or O(1) iterative
    '''Steps for Heap Sort:
    - Heapify the array
    - Convert to max. heap (parent node is greater than child node)
    - Start Deleting Elements one by one. (In Max or Min Heaps, when an element is deleted, it is stored at the ( last position - ith time of deletion)).
    - When All Elements are removed from the Heap, we will finally have  a sorted Array. 
    - https://www.youtube.com/watch?v=MtQL_ll5KhQ 
    '''
    new_arr = [] 
    for i in range(len(arr)):
        arr[i] = -1 * arr[i] 
    heapify(arr)  #creating max heap
    
    for i in range(len(arr)-1, 0, -1):
        temp = arr[i] 
        arr[i] = arr[0] 
        arr[0] = temp 
        new_arr.append(heappop(arr))
    new_arr.append(heappop(arr))
    for i in range(len(new_arr)):
        new_arr[i] = -1 * new_arr[i] 
    return new_arr 


print("Heap Sort")
print(heap_sort(arr))  


def bitonic_sort(arr):
    return 