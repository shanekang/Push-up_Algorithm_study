def solution():
    arr.sort(reverse=True) #가장 무거운 무게부터 정렬 한다. 
    for i in range(N): 
        arr[i] = arr[i] * (i + 1) #로프가 버틸수 있는 가장 무거운 무게는 이 식으로 곱하여 값이 커지지 않는다. 
    return max(arr) #그 다음  로프가 버틸수있는 무게부터 이 식에 해당되어 곱해진다.
                    # 그 값들중 가장 큰 무게 값을 리턴한다. 
 
 
N = int(input()) #N개의 로프값을 input받는다.
arr = [] #입력 받을 숫자들을 저장할 리스트
for _ in range(N): #N개 만큼 로프가 버틸 수 있는 값을 input 받는다.
    arr.append(int(input()))
 
print(solution())
