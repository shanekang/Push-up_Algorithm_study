def MergeSort(list):

    if len(list) < 1 :
        return

    mid = len(list)//2
    left_list, right_list = list[:mid], list[mid:]

    MergeSort(left_list)
    MergeSort(right_list)


    i,j,k = 0,0,0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            list[k] = left_list[i]
            i += 1
        else :
            list[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        list[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        list[k] = right_list[j]
        j += 1
        k += 1

n, k = map(int, sys.stdin.readline().split()) 
list = [*map(int, sys.stdin.readline().split())]

MergeSort(list)
print(list[k-1])