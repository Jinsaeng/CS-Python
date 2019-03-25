#6
def reverse_to_new_list(ls):
    ls2 = ls[len(ls)::-1]
    return ls2
#creates a new list with the reverse elements

def reverse_in_place(ls):
    ls = ls[len(ls)::-1]
    return ls
#reverses the elements of the same list

def main():
    ls = [1,2,3,4,5,6]
    print(reverse_to_new_list(ls))
    print(reverse_in_place(ls))
    
main()


