def solution(n):
    answer = [True] * (n+1)
    
    sqrt_n = int(n ** 0.5)
    for i in range(2, sqrt_n+1):
        if answer[i] == True:
            for j in range(i+i, n+1, i):
                answer[j] = False
    
    return len([i for i in range(2,n+1) if answer[i] == True])

n = 8
print(solution(n))