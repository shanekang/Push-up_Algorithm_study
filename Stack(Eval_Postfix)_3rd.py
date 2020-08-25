# Stack Class -> (구현 완료) 
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



# ===========================================================================
# 중위 표기법을 후위 표기법으로 바꾸는 함수입니다. 이 부분을 작성해 주시면 됩니다.
# !!여기 부분을 추가로 구현해 주세요!! => 라고 적힌 부분을 구현하시면 됩니다! 
# 참고: 오히려 제가 Base로 제시한 코드가 각자 이해 하기에 훨씬 더 어려울 수도 있어요..
# 가급적이면 원리만 이해하시고, 본인만의 코드로 짜시는 것을 추천드립니다! 

def infix_to_postfix(string): 
    stack = Stack()
    numlist = []

    for i in string.split(' '):
    
        # i가 숫자일 경우 numlist에 추가
        if i.isnumeric() :
            numlist.append(i)

        # i가 '(', ')'일 경우
        elif i == ')' :
            while stack.peek() != '(' :
                numlist.append(stack.pop())
            stack.pop()

        elif i == '(' :
            stack.push(i)

        # i가 연산자(*,/)
        elif i in ['*','/'] :
            while stack.peek() in ['*','/'] :
                numlist.append(stack.pop())
            stack.push(i)


        # i가 연산자(+,-)
        elif i in ['+','-'] :
            while stack.peek() in ['*','/','+','-'] :
                numlist.append(stack.pop())
            stack.push(i)

            
    while not stack.is_empty():
        numlist.append(stack.pop())

    return ' '.join(numlist)
						# 계산할때를 대비해서, ' '띄어서 join해야함! 으

# ====================밑의 부분 부터는 건드리지 않으셔도 됩니다 ==============
# =========================================================================
# 2. 후위 표기법을 사칙연산으로 계산값을 return하는 함수입니다. -> (구현 완료)
def eval_postfix(string):
    stack = Stack() 

    for elem in string.split(): # 빈칸을 기준으로 나눕니다. 
        if elem.isnumeric(): # 숫자가 맞다면, stack에 push!
            stack.push(int(elem)) # 사칙연산을 위해 미리 정수형으로 변환!

        else:  
            num2 = stack.pop() # 가장 위의 원소를 pop!
            num1 = stack.pop() 

            if elem == '+': stack.push(num1 + num2) 
            elif elem == '-': stack.push(num1 - num2) 
            elif elem == '*': stack.push(num1 * num2) 
            else: stack.push(num1 / num2)
            

    return stack.peek() # stack에 남은 가장 마지막 숫자를 반환 

# ======== CODES FOR TEST =======================================
def expr_test(infix):
    postfix = infix_to_postfix(infix)
    result = eval_postfix(postfix)
    print("'%s' => '%s' = %.2f" % (infix, postfix, result))

if __name__ == '__main__':
    expr_test("14 + 3 - 2")
    expr_test("4 + 23 - 4 / 2")
    expr_test("1 + 2 * 43 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 1 + 2 ) * 10 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 150 + 60 / 2 * 2 + ( ( 78 - 20 ) + ( 60 / 3 ) ) + 15 )")