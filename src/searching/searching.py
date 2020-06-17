# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, floor, ceiling):
    # Your code here
    # Check base
     if floor >= ceiling:
         return -1

     midpoint = (ceiling - floor) // 2 + floor
     # If element is present at the middle
     if target == arr[midpoint]:
         return midpoint
     # If element is smaller than mid, then it can only be present in left subarray
     elif target < arr[midpoint]:
         return binary_search(arr, target, floor, midpoint + 1)
     # Else the element can only be present in right subarray 
     elif target > arr[midpoint]:
         return binary_search(arr, target, midpoint - 1, ceiling)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

