#1
def max_abs_value(ls):
    for i in range(len(ls)):
        ls[i] = abs(ls[i])
    return max(ls)

def main():
    ls =[-19, -3, 20, -1, 0, -25]
    print(max_abs_value(ls))
    
main()
