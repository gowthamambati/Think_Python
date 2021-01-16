triangle = [int(input(x)) for x in ['a = ', 'b = ', 'c = ']]
triangle.sort()


def is_triangle():
    if triangle[0] + triangle[1] <= triangle[2]:
        print ('No')
    print ('Yes')
        
is_triangle()
