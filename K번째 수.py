# Merge Sort로 구현시, 무난하게 풀립니다6^^7

# ================ HINT =============================================
# ================ quick sort =======================================
import sys 
sys.setrecursionlimit(100000)

def set_pivot(alist, start, end): 
    values = [(i, alist[i]) for i in [start, (start+end)//2 , end]] 
    values.sort(key=lambda x:x[1]) 
    return values[1][0] 

# Lomuto Partition 
# Hoare Partition으로 구현하니 시간초과 납니다ㅠㅠ
def partition(alist, start, end): 
    if len(alist) > 2:
        p_idx = set_pivot(alist, start, end) 
        # 처음, 중앙, 마지막 값 중 가장 중앙값의 인덱스를 반환합니다.
        alist[end], alist[p_idx] = alist[p_idx], alist[end]
        
    pivot = alist[end] 

    a = start 
    for i in range(start, end): 
        if alist[i] <= pivot: 
            alist[i], alist[a] = alist[a], alist[i] 
            a += 1 
    alist[a], alist[end] = alist[end], alist[a] 
    return a 

def quick_sort(alist, start, end, k): 
    # Naive quick sort 이후의 k값을 찾기엔 시간초과가 발생하여, k의 위치에 해당하는 부분만
    # 정렬하도록 함으로써 불필요한 부분까지의 정렬을 고려하지 않아야 시간 내에 통과하게 됩니다. 
    # 즉, k값의 위치를 매번 quick sort 함수를 재귀호출할 때마다 고려하면서 진행해야 합니다.

    if start >= end: 
        return alist[start] 

    p = partition(alist, start, end) 
    # 현재 partition 함수가 완료되면 pivot을 기준으로 왼쪽은 pivot보다 작은 값들만 존재하고, 
    # pivot의 오른쪽은 pivot보다 큰 값들만 존재합니다. 
    # 그렇다면, pivot의 인덱스가 k보다 큰지, 작은지만 파악하고 k에 존재하는 리스트만 찾아 
    # 재귀적으로 호출하면서 탐색하면 됩니다.

    pp = p - start + 1 # pp는 k와 pivot 인덱스를 비교하기 위해 조정한 값입니다...
                       # 설명을 어떻게,,,,ㅠㅠ 죄송합니다. 내일 이 부분 더 알려드릴께욥

    # k 와 조정된 pivot 값을 비교하여 선택적으로 다음 quick sort할 범위를 구합니다.
    # 여기 부분에 어떤 quick_sort(?, ?, ?, ?)를 넣으면 좋을지 고민하시고 구현하시면 됩니다.
    if k == pp: 
        return 0
    elif k < pp: 
        return quick_sort(None, None, None, None)
    else: 
        return quick_sort(None, None, None, None) 


n, k = map(int, sys.stdin.readline().split()) 
alist = list(map(int, sys.stdin.readline().split())) 

print(quick_sort(alist, 0, n-1, k) )