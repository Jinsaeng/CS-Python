def flat_list(nested_list, low, high):
    newls = []
    if low==high:
        return nested_lst[low]
    else:
        for x in nested_list:
            if isinstance(x, int):
                newls.append(x)
                return newls
            elif isinstance(x, list):
                flat_list(nested_list,low+1,high)
    return newls
