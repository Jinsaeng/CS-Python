express = input("Enter a mathematical expression:");

for i in range(len(express)):
    if express.find("+") > 0:
        op = "+"
    elif express.find("-") > 0:
        op = "-"
    elif express.find("*") > 0:
        op = "*"
    elif express.find("/") > 0:
        op = "/"
    pos = express.index(op)
operand1 = int(express[0:pos])
operand2 = int(express[pos+1:])
if op == "+":
    total = operand1 + operand2
elif op == "-":
    total = operand1 - operand2
elif op == "*":
    total = operand1 * operand2
elif op == "/":
    total = operand1 / operand2

print(operand1, op, operand2, "=", total)

