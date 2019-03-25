class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

    
def tag_gen(text):
    while text != "":
        text = file.readline()
        n = len(text)
        for char in range(n):
            if text[char] == "<":
                start = char
            elif text[char] == ">":
                end = char
                
                yield text[start:end+1]
                
file = open("html_file.html", "r")



def is_matched(expr):
    left = "<"
    right = "/"
    count = 0
    s = ArrayStack()
    if right in expr[0:1]:
        if s.is_empty():
            return False
        if s.top() == expr:
            s.pop()
            count -= 1
    else:
        s.push(expr)
        count += 1
    if s.is_empty():
        return True
    else:
        return False

for expr in tag_gen(file):
    if (is_matched(expr)):
        count = 1
    else:
        count = 0
if count == 1:
    print("The file is correct")
else:
    print("The file is incorrect")

def eval_postfix_boolean_exp(boolean_exp_str):
    numbers = ArrayStack()
    operators = ArrayStack()
    symbols = "<>&|"
    expression_list = string_input.split()
    count = 0
    for ​item in ​expression_list:
        if ​item.isdigit():
            numbers.push(int(item))
        elif ​item in ​symbols:
            operators.push(item)
        elif ​item == ")"​:
            # evaluate
            rhs = numbers.pop()
            lhs = numbers.pop()
            operation = operators.pop()
        if ​operation == ">"​:
            if lhs > rhs:
                count += 1
            else:
                count -= 1
        elif ​operation == "<"​:
            if lhs < rhs:
                count += 1
            else:
                count -= 1
        elif ​operation == "&"​:
            if lhs and rhs:
                count += 1
            else:
                count -= 1
        elif ​operation == "|"​:
            if lhs or rhs:
                count += 1
            else:
                count -= 1
    if count >= 1:
        return True
    else:
        return False
def convert_infix_exp_to_postfix(infix_exp_str):
    operation = ArrayStack()
    postfix = []
    for token in token(infix_exp_str):
        if token.isdigit():
            postfix.append(token)
        elif token = "(":
            operation.push(token)
        elif token in "+-/*":
            operation.push(token)
        else:
            operator = operation.pop()
            operation.pop()
            postfix.append(operator)
    return " ".join(postfix)
