x = (input('x?\n'))
y = (input('y?\n'))
z = (input('z?\n'))


def is_between(x, y, z):
    return x <= y <= z

a = is_between(x, y, z)
if a:
    print ('y is between x and z!')
else:
    print ('y is not between x and z!')
