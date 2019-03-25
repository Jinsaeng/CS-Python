def findchange(lst01):
    first = 0
    last = len(lst01)
    number = 1
    found = False
    while found == False and first <= last:
        midpoint = (first + last) //2
        if lst01[midpoint] == number:
            found = True
            return midpoint
        elif number in lst01[:midpoint]:
            last = midpoint
        elif number in lst01[midpoint:]:
            first = midpoint
