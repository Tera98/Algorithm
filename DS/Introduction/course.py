
class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def a_course(n):
    if n is not None:
        print(f'{n.name} ->', end=' ')
        a_course(n.left)
        a_course(n.right)


def b_course(n):
    if n is not None:
        a_course(n.left)
        print(f'{n.name} ->', end=' ')
        a_course(n.right)


def c_course(n):
    if n is not None:
        a_course(n.left)
        a_course(n.right)
        print(f'{n.name} ->', end=' ')


def mapping():
    n1 = Node('H')
    n2 = Node('F')
    n3 = Node('S')
    n4 = Node('U')
    n5 = Node('E')
    n6 = Node('Z')
    n7 = Node('K')
    n8 = Node('N')
    n9 = Node('A')
    n10 = Node('Y')
    n11 = Node('T')

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n5.left = n9
    n7.right = n10
    n9.right = n11

    return n1


# course
start_map = mapping()
print('a-course:\t', end=' ')
a_course(start_map)
print('\nb-course:\t', end=' ')
b_course(start_map)
print('\nc-course:\t', end=' ')
c_course(start_map)