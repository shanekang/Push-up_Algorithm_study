

t = int(input("몇개의 케이스를 입력하시겠습니까? >> ")) # 3개
count = [1,2,4]
for i in range(3, 11):
    count.append(count[i-1]+count[i-2]+count[i-3])
for j in range(t):
    n = int(input("1, 2, 3의 합으로 나타낼 정수를 입력하세요. >> ")) # 4, 7, 10
    print(count[n-1])