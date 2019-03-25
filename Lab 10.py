#1
##def write_name(filename, first_name, last_name):
##    file = open("write_name_test.txt", "w")
##    print(first_name, last_name, file= file);
##    file.close()
##def main():
##    filename = "write_name_test.txt"
##    first_name = "Charles"
##    last_name = "Darwin"
##    write_name(filename, first_name, last_name)
##main()
##

###2
##import random
##def write_randint(filename, n):
##    file = open("print_rand_int.txt", "w")
##    for i in range(n):
##        print(random.randint(1,100), file = file)
##    file.close()
##def main():
##    filename = "print_rand_int"
##    n = 10
##    write_randint(filename, n)
##main()

#3
def sum_column(filename):
    file  = open("print_rand_int.txt", "r")
    file2 = open("Sum_of_rand_int.txt", "w")
    total = 0
    for line in file:
        total += int(line)
    print(total, file= file2)
    file.close()
    file2.close()

def main():
    filename = "print_rand_int"
    sum_column(filename)
main()

#4
##def html_table_generator(ls, file_to_write_to):
##    file = open("file_to_write_to.html", "w")
##    print("<html>", file = file)
##    print("<table>", file=file)
##    for i in range(len(ls)):
##        print("<tr>", file=file)
##        if i == 0:
##            for j in range(len(ls[i])):
##                print("<th>",ls[i][j],"</th>", file=file)
##        else:
##            for j in range(len(ls[i])):
##                print("<td>",ls[i][j],"</td>", file=file)
##        print("</tr>", file=file)
##    print("</table>", file=file)
##    print("</html>", file=file)
##    file.close()
##def main():
##    file_to_write_to = "file_to_write_to"
##    ls = [["Header1", "Header2", "Header3", "Header4"], ["R1C1", "R1C2", "R1C3","R1C4"], ["R2C1", "R2C2", "R2C3", "R2C4"], ["R3C1", "R3C2", "R3C3", "R3C4"]]
##    html_table_generator(ls,file_to_write_to)
##main()
##
