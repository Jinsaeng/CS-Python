def permutations(lst, low, high):
    newls= []
    val = []
    if low == high:
        return lst[low]
    else:
        val = [permutation(lst,low+1,high)]
        newls.append(val)
        return newls
