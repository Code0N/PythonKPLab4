import numpy
from functools import reduce
from operator import mul


def matrix_mul(A, B):
    A_m = numpy.matrix(A)
    B_m = numpy.matrix(B)
    return (A_m*B_m).tolist()


def _1():
    A = numpy.random.randint(0, 100, (3, 5))
    B = numpy.random.randint(0, 100, (5, 2))
    print('A = {}\nB = {}\nA * B = {}'.format(A, B, matrix_mul(A, B)))


def _2():
    A = numpy.random.randint(0, 100, (5, 3))
    B = numpy.random.randint(0, 100, (3, 1))
    print('A = {}\nB = {}\nA * B = {}'.format(A, B, matrix_mul(A, B)))


def _3():
    n = numpy.random.randint(0, 100)
    A = numpy.random.randint(0, 100, (n, n))
    B = numpy.random.randint(0, 100, (n))
    X = numpy.linalg.solve(A, B)
    print('A = {}\n A * X = {}\nX = {}'.format(A, B, X))


def _4():
    n = numpy.random.randint(1, 100)
    A = numpy.matrix(numpy.random.randint(0, 100, (n, n)))
    print('A = {}\ndet(A) = {}'.format(A, numpy.linalg.det(A)))


def _5():
    n = numpy.random.randint(3, 4)
    A = numpy.matrix(numpy.random.randint(0, 100, (n, n)))
    print('A = {}\nA^-1 = {}\nA^T = {}'.format(A,
                                               numpy.linalg.inv(A),
                                               numpy.transpose(A)))


def _addition():
    not_equal_counter = 0
    iter_count = 1000
    for i in range(iter_count):
        A = numpy.matrix(numpy.random.randint(0, 100, (5, 5)))
        det = numpy.round(numpy.linalg.det(A))
        eigvals = numpy.round(reduce(mul, numpy.linalg.eigvals(A)))
        if not numpy.equal(det,
                           eigvals):
            print('Not equal with det = {} and eigvals = {}'
                  .format(det, eigvals))
            not_equal_counter += 1
    print('Wasn\'t equal {} of {} times'.format(not_equal_counter,
                                                iter_count))

if __name__ == '__main__':
    _addition()
