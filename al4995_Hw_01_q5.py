#5
def fibs(n):
    curr = 1
    curr2 = 1
    yield curr
    yield curr2
    for x in range(n-2):
        num = curr + curr2
        yield num
        curr = curr2
        curr2 = num
        
