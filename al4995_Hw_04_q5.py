def count_lowercase(s,low,high):
    counter = 0
    if low == high:
        return s[low]
    else:
        res = count_lowercase(s,low+1,high)
        if res.islower():
            counter += 1
        return res,counter
def is_number_of_lowercase_even(s,low,high):
    counter = 0
    if low == high:
        return s[low]
    else:
        res = count_lowercase(s,low+1,high)
        if res.islower():
            counter += 1
    if counter%2 == 0:
        return True
    else:
        return False
