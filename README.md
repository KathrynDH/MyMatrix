# Matrix-math
MatrixMath is a light weight class for performing basic matrix operations.

No additional pacakages are required. It uses only builtin Python functions.

A MatrixMath object is constructed from an $m \times n$ 2-dimensional list


## Getting Started
Include:
<code> from matrix_math import MatrixMath </code>

Methods:

<code>   

    print_matrix(self, percision = 4)

    add(self, other)

    subtract(self, other)

    multiply_scalar(self, a)

    multiply(self, other)

    transpose(self)

    determinant(self)

    cofactor(self, i, j)

    adjoin(self)

    inverse(self)

    id(rows)

    exp(self, n)
</code>    

Magic methods:
  add, sub, mul, rmul, pow, getitem, setitem

## Examples
<code> a = MatrixMath([[1,2],[3,4]]) </code>

printing: <code> a.print_matrix() </code>

determinant: <code> a.determinant() </code>

transpose: <code> a.transpose() </code>

inverse: <code> a.inverse() </code> or <code> a**-1 </code>

</code>

Jupyter notebook:
[Notebook examples](https://github.com/KathrynDH/MyMatrix/blob/main/MatrixMathExamples.ipynb)

Also see examples.py in this repository.

## License
The contents of this repository are covered under the [MIT License](LICENSE).
