# this is for binary search algorithm
#time complexity of binary search  is 0(logn)
def binarysearch(li,target):
    low=0
    high=len(li)-1
    while low<=high:
        mid=(low+high)//2
        if li[mid]==target:
            return mid
        else:
            if mid<target:
                low=mid
            else:
                high=mid
li=[1,3,5,6,7,8,90,3454,4567,7890,98765]
binarysearch(li,4567)
#linear searching in datastuctures with python
#time complexity of 
def linear(li,target):    
    for i in range(len(li)):
        if li[i]==target:
            return i
linear(li,7)
