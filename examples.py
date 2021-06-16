from matrix_math import MatrixMath

def demonstrate(a):
    """
    Function to demonstrate some of the MatrixMath methods

	Args:
		a (MatrixMath): Matrix

	Returns:
		nothing
    """

    print('Matrix:')
    a.print_matrix()

    try:
        print('\nDeterminant: {}'.format(a.determinant()))
    except:
        print('\nMatrix does not have a determinant')

    print('\nMatrix transpose:')
    a.transpose().print_matrix()

    try:
        print('\nMatrix inverse:')
        a.inverse().print_matrix()
    except:
        print('Matrix does not have an inverse')
    print('\n')


# Create some matrices as MatrixMath objects
a = MatrixMath([[1,0, 0],[0, 1, 0],[0,0,1]])
b = MatrixMath([[1,2, 3],[4,5, 6]])
c = MatrixMath([[5,2, 3, 10],[4,5, 6, 11],[7,8,9, 12],[13,14,15,20]])
d = MatrixMath([[1,2],[3,4]])
f = MatrixMath([[1+2j,2+5j],[3,4-2j]])

matrices = {'A':a, 'B':b, 'C':c, 'D':d, 'F':f}

for n, m in matrices.items():
    print('Matrix {}'.format(n))
    demonstrate(m)

print('d + f')
(d + f).print_matrix()

print('\nd - f')
(d - f).print_matrix()

print('\nd * f')
(d * f).print_matrix()

print('\n3 * d')
(3 * d).print_matrix()

print('\n1-2j * f')
((1-2j) * f).print_matrix()

print('\nf * f inverse')
(f * f**-1).print_matrix()
