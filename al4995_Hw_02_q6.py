def two_sum(srt_lst, target):
    lst = []
    tup = ()
    length = len(srt_lst)
    x = 1
    for i in range(length):
       # y+= 1
        if srt_lst[i] + srt_lst[length - x] == target:
            tup = (i, length-x)
            return tup
        elif srt_lst[i-x] + srt_lst[length - x] < target:
            x += 1
        elif srt_lst[i] + srt_lst[length - x] > target:
            x -= 1
        else:
            return None
