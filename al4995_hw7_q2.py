#2
def find_all(ls, val):
    index = [];
    for i in range(len(ls)):
        if ls[i] == val:
            index.append(i)
    return index
def main():
    ls = ["a", 'b', '10', 'bab', 'a']
    val = "a"
    print(find_all(ls,val))
main()
