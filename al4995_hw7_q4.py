#4
def create_prefix_lists(ls):
    ls2 = []
    for i in range(len(ls)+1):
        lsTemp = ls[:i]
        ls2 += [lsTemp]
    return ls2

def main():
    ls = [2, 4, 6, 8, 10]
    print(create_prefix_lists(ls))
    
main()

