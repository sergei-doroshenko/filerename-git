

def test_1():
    print('test')

    # Way 1
    emptyTuple = ()

    # Way 2
    emptyTuple = tuple()

    # way 1
    z1 = (3, 7, 4, 2)
    print(z1[0])
    print(z1[-1])
    # first index is inclusive (before the :) and last (after the :) is not.
    print(z1[0:2])
    # everything up to but not including index 3
    print(z1[:3])

    # way 2 (tuples can also can be created without parenthesis)
    z2 = 3, 7, 4, 2

    # tuple with one value
    tup1 = ('Michael',)
    # tuple with one value
    tup2 = 'Michael',
    # This is a string, NOT a tuple.
    notTuple = ('Michael')


if __name__ == '__main__':
    test_1()