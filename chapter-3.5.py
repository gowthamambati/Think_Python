def do_twice(f,r,c):
    f(r,c)
    f(r,c)
    
def print_twice(row, column):
    print(row)
    print(column)
    print(column)
    print(column)
    print(column)
    
def do_four(f,r,c):
    do_twice(f,r,c)
    do_twice(f,r,c)

do_four(print_twice, '+----+----+', '|    |    |')
print('+----+----+')
