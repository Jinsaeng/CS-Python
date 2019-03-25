
print("Please enter non-empty sequence of positive integers, each one in a separate line. End your sequence by typing 'done': ");
entered = input()
loop = 0
placement = 1
while( entered != "done"):
    placement *= int(entered)
    loop += 1
    entered = input()

mean = (placement ** (1/loop))
print(mean)

#basically unlimited inputs until specific "done" entered and then has to find the geometric mean of the n amount of inputs
