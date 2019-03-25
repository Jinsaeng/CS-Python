#3
def same_length(ls1, ls2):
    if len(ls1) == len(ls2):
        size = True;
    else:
        size = False;
    return size
        
def add_list(ls1, ls2):
    size = same_length(ls1,ls2)
    newsum = []
    newsumstr = ""
    if size:
        for i in range(len(ls1)):
            newsum.append(ls1[i] + ls2[i])
        for i in range(len(newsum)):
            newsumstr += str(newsum[i]) + "\n"
    else:
        newsumstr = "Lists are different length"
    return newsumstr

def main():
    ls1 = []
    ls2 = []
    num =0
    num2 = 0
    print("Enter numbers for list 1 and list 2")
    while num != "done":
        num = input()
        if num != "done":
            num = int(num)
            ls1.append(num)
    while num2 != "done":
        num2 = input()
        if num2 != "done":
            num2 = int(num2)
            ls2.append(num2)
    print("Resulting List... ")
    print(add_list(ls1,ls2))
    
main()
