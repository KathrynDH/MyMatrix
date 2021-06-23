class MatrixMath():
    """ Class for performing matix operations

    Attributes:
	   matrix (2d list of float, int, or complex) representing a matrix
       rows (int) number of rows
       columns (int) number of columns
	"""
    def __init__(self, matrix):

        self.rows = len(matrix)
        self.columns = len(matrix[0])

        #Check if list is a matrix
        if not all(isinstance(i, (float, int, complex)) for r in matrix for i in r):
            raise TypeError('Elements must be numbers')
        if not all(len(r) == self.columns for r in matrix):
            raise ValueError('All rows must be of the same length')
        self.matrix=matrix

    def print_matrix(self, percision = 4):
        """
        Function to print rows of a matrix

		Args:
            percision (int): number of places to round to

		Returns:
			nothing
        """

        for r in self.matrix:
            row = []
            for i in r:
                if isinstance(i, float):
                    row.append(round(i,percision))
                elif isinstance(i,complex):
                    if abs(i.imag) < 0.000001:
                        row.append(round(i.real,percision))
                    else:
                        x = round(i.real,percision)+round(i.imag,percision)*1j
                        row.append(x)
                else:
                    row.append(i)
            print(row)
        print('{} x {}'.format(self.rows, self.columns))

    def add(self, other):
        """
        Function to add two matrices

		Args:
			other (MatrixMath): Matrix

		Returns:
			MatrixMath: Matrix

		"""
        if not (self.columns == other.columns and self.rows == other.rows):
            raise RuntimeError('Matrices must be of the same size')
        result = []
        for r in range(self.rows):
            result.append([x + y for x, y in zip(self.matrix[r],other.matrix[r])])

        return MatrixMath(result)

    def subtract(self, other):
        """
        Function to subtract two matrices

		Args:
			other (MatrixMath): Matrix

		Returns:
			MatrixMath: Matrix

		"""
        if not (self.columns == other.columns and self.rows == other.rows):
            raise RuntimeError('Matrices must be of the same size')
        result = []
        for r in range(self.rows):
            result.append([x - y for x, y in zip(self.matrix[r],other.matrix[r])])

        return MatrixMath(result)

    def multiply_scalar(self, a):
        """
        Function to multiply a matrix and a number

		Args:
			other (MatrixMath): Matrix

		Returns:
			MatrixMath: Matrix

		"""

        if not isinstance(a, (float, int, complex)):
            raise TypeError('Scalar must be a number')

        result = []
        for r in range(self.rows):
            result.append([x * a for x in self.matrix[r]])
        return MatrixMath(result)

    def multiply(self, other):
        """
        Function to multiply two matrices

		Args:
			other (MatrixMath): Matrix

		Returns:
			MatrixMath: Matrix

		"""
        if not (self.columns == other.rows):
            raise RuntimeError('Matrices are not of the correct shape')
        result = []
        for j in range(self.rows):
            row = []
            for i in range(other.columns):
                l = [other.matrix[k][i] for k in range(other.rows)]
                row.append(sum(x * y for x, y in zip(self.matrix[j],l)))
            result.append(row)
        return MatrixMath(result)

    def transpose(self):
        """
        Function to transpose a matrix

		Args:
			none

		Returns:
			MatrixMath: Matrix

		"""

        result = []
        for c in range(self.columns):
            result.append([self.matrix[r][c]for r in range(self.rows)])
        return MatrixMath(result)

    def determinant(self):
        """
        Function to find the determinant of a matrix

		Args:
			none

		Returns:
			int, float, complex: determinant of the square matrix

		"""

        if not (self.columns == self.rows):
            raise RuntimeError('Matrix must be square')

        if self.rows == 1:
            return self.matrix[0][0]

        if self.rows == 2:
            a = self.matrix[0][0]*self.matrix[1][1]
            b = self.matrix[0][1]*self.matrix[1][0]
            return a - b

        #if matrix has 3 or more rows, expand along the first row
        result = 0
        for i in range(self.columns):
            c = self.cofactor(1,i+1)
            result += self.matrix[0][i] * c
        return result

    def cofactor(self, i, j):
        """
        Function to find the cofactor of a matrix element

		Args:
			i (int): row of element
            j (int): column of element
            *Note: method uses traditional matrix 1-based indexing
             The first element in the first row would be i=1, j=1

		Returns:
			int, float, complex: cofactor of the matrix element

		"""

        result = []
        #append rows before ith row excluding column j
        for x in range(0,i-1):
            a = self.matrix[x][0:j-1] + self.matrix[x][j:self.columns]
            result.append(a)

        #append rows after ith row excluding column j
        for x in range(i,self.rows):
            b = self.matrix[x][0:j-1] + self.matrix[x][j:self.columns]
            result.append(b)

        #calculate and return the cofactor
        return (-1)**(i+j) * MatrixMath(result).determinant()

    def adjoin(self):
        """
        Function to find the adjoin of a matrix

		Args:
            None
		Returns:
			MatrixMath: adjoin the matrix

		"""

        t = self.transpose()
        result = []
        for i in range(1,t.columns+1):
            result.append([t.cofactor(i,j) for j in range(1,t.rows+1)])

        return MatrixMath(result)

    def inverse(self):
        """
        Function to find the inverse of an invertable matrix

		Args:
            None
		Returns:
			MatrixMath: inverse the matrix

		"""
        det = self.determinant()
        if det == 0:
            raise RuntimeError('Matrix is not invertable')

        return (1/det) * self.adjoin()

    @staticmethod
    def id(rows):
        """
        Function to create identity matrix

		Args:
            rows (int): size of identity matrix
		Returns:
			MatrixMath: identity matrix

		"""
        result = []
        for m in range(rows):
            row = []
            for n in range(rows):
                if m == n:
                    row.append(1)
                else:
                    row.append(0)
            result.append(row)
        return MatrixMath(result)

    def exp(self, n):
        """
        Function to find the power of a square matrix

		Args:
            n (int): exponent
		Returns:
			MatrixMath: power of the matrix

		"""
        if not (self.columns == self.rows):
            raise RuntimeError('Matrix must be square')
        if not isinstance(n, int):
            raise TypeError('Exponent must be an integer')

        if n == 0:
            return MatrixMath.id(self.rows)
        elif n > 0:
            m = self
        else:
            m = self.inverse()

        result = m

        for x in range(1,abs(n)):
            result *= m

        return result

    def __add__(self, other):
        """
        Function to add two matrices using +

		Args:
			other (MatrixMath): Matrix

		Returns:
			MatrixMath: Matrix

		"""
        return self.add(other)

    def __sub__(self, other):
        """
        Function to subtract two matrices using -

		Args:
			other (MatrixMath): Matrix

		Returns:
			MatrixMath: Matrix

		"""
        return self.subtract(other)

    def __mul__(self, other):
        """
        Function to multiply two matrices using * or to multiply a matrix by
        a scalar using *

		Args:
			other (MatrixMath, int, float, or complex): Matrix or scalar

		Returns:
			MatrixMath: Matrix

		"""
        if isinstance(other, (float, int, complex)):
            return self.multiply_scalar(other)
        elif isinstance(other, MatrixMath):
            return self.multiply(other)
        else:
            raise TypeError('Scalar must be a number')

    def __rmul__(self, other):
        """
        Function to multiply a scalar by a matrix using *

		Args:
			other (int, or float, or complex): scalar

		Returns:
			MatrixMath: Matrix

		"""
        if isinstance(other, (float, int, complex)):
            return self.multiply_scalar(other)
        else:
            raise TypeError('Scalar must be a number')

    def __pow__(self, n):
        """
        Function for matrix powers using **

		Args:
			n (int): exponent

		Returns:
			MatrixMath: Matrix

		"""
        return self.exp(n)

    def __getitem__(self, key):
        """
        Function to get matrix items by index

		Args:
			key (int or slice object): Key

		Returns:
			item or list: Items in matrix

		"""
        return self.matrix[key]

    def __setitem__(self, key, item):
        """
        Function to set matrix items by index

		Args:
			key (int or slice object): Key

		Returns:
			nothing

		"""
        m = self.matrix
        m[key] = item
        self = MatrixMath(m)
