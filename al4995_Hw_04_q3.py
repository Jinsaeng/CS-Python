def print_triangle(n):
    res = ""
    if n == 0:
        return ""
    else:
        res =res + print_triangle(n-1) + (n* "*") + "\n"
        return res

def print_opposite_triangles(n):
    res = ""
    if n == 0:
        res = "" + "\n"
        return res
    else:
        res = "\n" + (n)*"*" + print_opposite_triangles(n-1) + ((n)* "*") + "\n"
        return res
    
def print_ruler(n):
    res = ""
    if n == 0:
        return ""
    else:
        res = res + ((n-1)*"-") + print_ruler(n-1) + (n*"-") + "\n"
        return res
