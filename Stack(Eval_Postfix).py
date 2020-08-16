    # Stack Class 부분부터 pass 구문을 지우고 구현해 주세요!
    class Stack: 
        def __init__(self):
            self.items = list() 
            self.size=-1
        def is_empty(self): # 현재 스택이 비었는지 확인하는 함수 
            return self.items==[]
        
        def push(self, item): # 스택에 item을 추가하는 함수 
            self.items.append(item)
            self.size+=1

        def pop(self): # 스택의 마지막 item을 빼고 그 값을 반환하는 함수 
            if self.is_empty():
                return 0
            else:
                self.size-=1
                return self.items.pop()

        def peek(self): # 스택의 마지막 item을 반환하는 함수 
            if self.is_empty():
                return 0
            else:
                return self.items(self.size)

    # 필요하면 추가로 함수를 만들어도 됩니다.


    # 1. 중위 표기법을 후위 표기법으로 바꾸는 함수입니다. 
    def infix_to_postfix(string): 
            stack = Stack() 
        return 


    # 2. 후위 표기법을 사칙연산으로 계산값을 return하는 함수입니다. 
    def eval_postfix(string):
            stack = Stack() 

        return 


    # ======== CODES FOR TEST =======================================
    # 밑의 부분 부터는 건드리지 않으셔도 됩니다 =======================
    def expr_test(infix):
        postfix = infix_to_postfix(infix)
        result = eval_postfix(postfix)
        print("'%s' => '%s' = %.2f" % (infix, postfix, result))

    def expr_test2(postfix): 
        result = eval_postfix(postfix)
        print("'%s' = %.2f" % (postfix, result))

    # 숫자는 여러 자리 숫자가 올 수도 있어요. 대신 연산자와 피 연산자는 공백문자로 나누어집니다.
    # 괄호는 '(' 또는 ')'만 주어진다고 가정하며 숫자/연산자 및 괄호 이외의 문자는 주어지지 않습니다.
    if __name__ == '__main__':
        
        test_type = input("테스트 방식: A / B => ")
        if test_type == "A":  # A 방식: 중위식 -> 후위식 -> 계산까지 모든 함수를 작성한 경우
            expr_test("14 + 3 - 2")
            expr_test("4 + 23 - 4 / 2")
            expr_test("1 + 2 * 43 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
            expr_test("( 1 + 2 ) * 10 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
            expr_test("( 150 + 60 / 2 * 2 + ( ( 78 - 20 ) + ( 60 / 3 ) ) + 15 )")
        else: # B 방식: 후위식 -> 계산 까지의 함수만 작성한 경우 
            # 밑의 문자열들은 중위표현식을 후위표현식으로 바꾼 후의 상태 입니다. 
            input_string = """14 3 + 2 -\n4 23 + 4 2 / -\n1 2 43 * + 4 2 4 5 2 + - / * -\n1 2 + 10 * 4 2 4 5 2 + - / * -\n150 60 2 / 2 * + 78 20 - 60 3 / + + 15 +"""
            for cases in input_string.split("\n"): expr_test2(cases) 
        