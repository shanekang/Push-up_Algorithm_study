import sys 

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    
    mid = len(alist)//2
    left = alist[:mid]
    right = alist[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []

    while (i<len(left)) & (j<len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    
    while (i<len(left)):
        sorted_list.append(left[i])
        i+=1

    while (j<len(right)):
        sorted_list.append(right[j])
        j+=1
    
    return sorted_list
    
n, k = map(int, sys.stdin.readline().split()) 
alist = list(map(int, sys.stdin.readline().split())) 
merge_sort(alist) 

print(alist[k-1])