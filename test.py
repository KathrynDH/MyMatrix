from matrix_math import MatrixMath

c = MatrixMath([[1+2j,2+5j],[3,4-2j]])
b = MatrixMath([[1,2],[3,4]])

b.print_matrix()
(b**5).print_matrix()

(b * b * b * b*b).print_matrix()

#(b.inverse() * b.inverse() * b.inverse()).print_matrix()
