class Empty(Exception):
    pass

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
    
numbers = ArrayStack()
operators = ArrayStack()
alpha = ArrayStack()
symbols = "+-*/"
expression = ""
while (expression != "done()"):
    expression_list = input("-->")
    expression_list = expression_list.split()
    count = 0
    for item in expression_list:
        if item.isdigit():
            numbers.push(int(item))
        elif item in symbols:
            operators.push(item)
        elif item.isalpha():
            alpha.push(item)
        elif item == "=":
            count = 1
    for x in range(int(len(numbers))//2):
        if not alpha.is_empty():
            char = alpha.pop()
            if count == 1:
                value = char
        elif alpha.is_empty():
            lhs = numbers.pop()
            rhs = numbers.pop()
            operation = operators.pop()
            if operation == "+":
                 value = lhs + rhs
            elif operation == "-":
                value = rhs - lhs
            elif operation == "*":
                 value = lhs * rhs
            elif operation == "/":
                 value = lhs / rhs
    if len(numbers)//2 == 0 and not numbers.is_empty():
        value = numbers.pop()
    print(value)
    
