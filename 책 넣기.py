'''책 넣기
시간 제한 : 2초메모리 제한 : 256MB
문제 설명
당신은 상자에 책을 넣고 있는데, 상자의 무게 제한을 넘지 않고 최대한 많이 넣어야 한다. 한 상자에 최대한 많이 책을 넣은 다음 상자를 닫고 봉인한 후, 다음 상자에 책을 넣을 수 있다. 책은 차곡차곡 쌓여있는데, 무조건 가장 위에서부터 책을 꺼내야 한다.

책들의 무게는 weights로써 주어진다. 이 배열의 첫 번째 요소가 쌓여있는 책 중에서 가장 위에 있는 책이고, 배열의 마지막 요소가 가장 밑에 있는 책이다. 상자에 담을 수 있는 최대 무게는 maxWeight로 주어진다. 책을 전부 담기 위한 상자의 최소 개수를 구하시오.

참고 / 제약 사항
Weights는 0개 이상 50개 이하의 요소를 가지고 있다.
1 <= maxWeight <= 1000
1 <= weights[n] <= maxWeight
테스트 케이스
weights = [1,1,1,7,7,7]
maxWeight = 8리턴(정답): 4
weights = [1]
maxWeight = 1리턴(정답): 1
weights = [1,15,1,15,1,15,1,15,1,15]
maxWeight = 15리턴(정답): 10
weights = []
maxWeight = 1리턴(정답): 0
weights = [5,5,5,5,5,5]
maxWeight = 10리턴(정답): 3
5킬로그램인 책 6개가 있고, 각 상자에 10키로씩 담을 수 있다 (책 2개). 즉, 상자는 총 3개만 있으면 된다.'''

class Solution:
    def solution(self, weights, maxWeight):
        count = 0
        sum_weight = 0
        len_weight = len(weights)
        for i in range(len_weight):
            sum_weight = sum_weight + weights[i]
            if sum_weight == maxWeight:
                count+=1
                sum_weight=0
            elif i == len_weight-1:
                count+=1 
                continue
            elif sum_weight < maxWeight and sum_weight + weights[i+1] > maxWeight:
                count+=1
                sum_weight=0
            elif sum_weight > maxWeight:
                count+=1
                sum_weight=0
           
        return count
sol1 = Solution()


weights = [1,1,1,7,7,7]
maxWeight = 8
print(sol1.solution(weights, maxWeight))
