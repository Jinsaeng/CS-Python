def print_shifted_triangle(n,m,symbol):
    matrix = "";
    for i in range(2*n):
        if i % 2 == 0:
            j = 0
        else:
            j = i
        line = (" " * m) + ((2* n-i) * " ")+ (j * symbol) + "\n"
        matrix +=line
    return matrix
def print_pine_tree(n, symbol):
    pine = "";
    for i in range(1, n+1):
        result = print_shifted_triangle(i+1, n-i, symbol) + "\n"
        pine += result
    return pine
def main():
    n = int(input("Enter the number of triangles: "))
    symbol = input("Enter the symbol you want to use: ")
    print(print_pine_tree(n, symbol))
