def intersection_list(lst1, lst2):
    combined = []
    for i in lst1:
        if i in lst2:
            combined.append(i)
    return combined
