class Stack: 
    def __init__(self):
        self.items = list() 

    def is_empty(self): # 현재 스택이 비었는지 확인하는 함수 
        return True if len(self.items) == 0 else False 
    
    def push(self, item): # 스택에 item을 추가하는 함수 
        self.items.append(item)  

    def pop(self): # 스택의 마지막 item을 빼고 그 값을 반환하는 함수 
        if not self.is_empty(): return self.items.pop() 

    def peek(self): # 스택의 마지막 item을 반환하는 함수 
        if not self.is_empty(): return self.items[-1]


# 1. 중위 표기법을 후위 표기법으로 바꾸는 함수입니다. 
def infix_to_postfix(string): 
    stack = Stack() # 연산할 우선순위를 저장할 스택 
                    # -> 우선순위가 낮을수록 스택의 밑에 저장
                    # -> 우선순위가 높을수록 스택의 위에 저장

    ret = list()    # 최종적으로 반환할 요소를 저장하는 리스트

    for elem in string.split(): 
        if elem.isnumeric(): # 숫자라면 무조건 결과 리스트에 추가
            ret.append(elem) 
            continue         # 다음 iteration 진행(밑의 코드 실행x, 다음 elem으로 진행)

        if elem == '(': stack.push(elem) # 여는 괄호는 일단 스택에 저장 

        elif elem in ['+', '-']:                          # 사칙연산 중 가장 우선순위가 낮음( '+-' < '*/' )
            tmp = stack.peek()                            # 일단 스택 가장 위의 요소를 보고, 
            while not stack.is_empty() and tmp != '(':    # 만약 스택이 비어있지 않고 괄호가 아니면,
                ret.append(stack.pop())                   # 스택의 가장 위인 연산자가 우선순위가 높으므로 먼저 ret에 추가
                tmp = stack.peek()                        # 다음 stack에 남은 요소를 확인, 스택이 비어있거나 '('이라면 while 문 종료!
            stack.push(elem)                              # + 또는 - 연산보다 우선순위가 높은 연산자를 다 뺐으니 이제 + 또는 - 를 ret에 추가

        elif elem in ['*', '/']:                          # 사칙연산 중 가장 우선순위가 높음 
            tmp = stack.peek()                            # 스택의 가장 위의 요소를 보고, 
            if tmp in ['*', '/']: ret.append(stack.pop()) # 만약 동일한 순위일 경우, 
                                                          # 순서에 따라 연산을 해야하므로 앞에 있는 연산 먼저 빼고 ret에 추가
            stack.push(elem)                              # 그 다음 stack에 저장
        
        elif elem == ')':                # 괄호의 마지막이 오면 무조건 이전 괄호 이전의 모든 연산을 후위표기법으로 넣어야 하므로
            while stack.peek() != '(':   # 여는 괄호가 올때까지
                ret.append(stack.pop())  # 모든 연산자를 ret에 추가하면서 stack에 뺀다.
            stack.pop()                  # 여는 괄호는 아직 stack에 남아있으므로 한번 더 pop!

    while not stack.is_empty():          # 아직 더 stack에 남은 연산이 없을때 까지
        ret.append(stack.pop())          # pop하면서 나온 값들을 ret에 추가
    
    return ' '.join(ret)                 # 빈칸을 사이에 두고 join한 string을 반환

# 2. 후위 표기법을 사칙연산으로 계산값을 return하는 함수입니다. - 힌트
def eval_postfix(string):
    stack = Stack() 

    for elem in string.split():   # 빈칸을 기준으로 나눕니다. 
        if elem.isnumeric():      # 숫자가 맞다면, stack에 push!
            stack.push(int(elem)) # 사칙연산을 위해 미리 정수형으로 변환!
            continue 
        
        num2 = stack.pop() # 가장 위의 원소를 pop!
        num1 = stack.pop()

    return stack.peek() 