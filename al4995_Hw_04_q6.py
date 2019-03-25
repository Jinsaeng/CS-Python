def appearances(s,low,high):
    start = 1
    keys = {}
    if low == high:
        return s[low]
    else:
        appearances(s,low+1,high)
        if s[low] not in keys:
            keys = {s[low] : start}
        else:
            keys[s[low]: start+1]
        return keys
        
