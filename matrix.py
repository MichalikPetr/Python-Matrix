def dot_product(vector1, vector2):
    """Returns the dot product of two vectors of same length."""
    result = 0

    for num1, num2 in zip(vector1, vector2):
        result += num1 * num2
    
    return result


class Matrix():
    def __init__(self):
        self.data = []
    
    def get_data(self):
        """Returns data."""
        return self.data
    
    def _check_data(self, data):
        """Checks if input data is of correct format."""
        if not isinstance(data, list):
            raise ValueError(f'Matrix data is of wrong type: {type(data)}')
        
        row_len = len(data[0])
        for row in data:
            if len(row) != row_len:
                raise ValueError(f'Inputted data is not matrix, row {row} is of different length.')

    def set_data(self, data):
        """Sets data of matrix."""
        self._check_data(data)
        self.data = data[:]
        return self

    def get_colums(self):
        """Returns columns of matrix."""
        columns = []

        for column in zip(*self.get_data()):
            columns.append(list(column))

        return columns

    def __str__(self):
        """Returns matrix as string where row items are separated by comma
        and rows are separated by newline character."""        
        return '\n'.join(', '.join(str(item) for item in row) for row in self.get_data())
    
    def __add__(self, matrix):
        """Returns matrix of two added matrices."""
        if not isinstance(matrix, Matrix):
            raise TypeError(f'Input item {matrix} is not a matrix')
        
        if len(self.get_data()) != len(matrix.get_data()):
            raise ValueError(f'Matrices {len(self.get_data())} and {len(matrix.get_data())} are of different height.')
        
        if len(self.get_data()[0]) != len(matrix.get_data()[0]):
            raise ValueError(f'Matrices {len(self.get_data()[0])} and {len(matrix.get_data()[0])} are of different width.')
        
        new_matrix = []

        for i, row in enumerate(self.get_data()):
            new_row = []

            for j, number in enumerate(self.get_data()[i]):
                new_row.append(number + matrix.get_data()[i][j])
        
            new_matrix.append(new_row)
        
        return Matrix().set_data(new_matrix)

    def __mul__(self, by):
        """Returns matrix of multiplied matrix by scalar or other matrix."""
        if isinstance(by, Matrix):
            if len(self.get_data()[0]) != len(by.get_colums()[0]):
                raise ValueError('Matrices can\'t be multiplied.')

            new_matrix = []

            for row in self.get_data():
                new_row = []

                for column in by.get_colums():
                    new_row.append(dot_product(row, column))

                new_matrix.append(new_row)

            return Matrix().set_data(new_matrix)

        if isinstance(by, (float, int)):
            new_matrix = []
          
            for row in self.get_data():
                new_row = []

                for item in row:
                    new_row.append(item * by)

                new_matrix.append(new_row)

            return Matrix().set_data(new_matrix)
        
        return NotImplemented


#test
"""
m1 = Matrix().set_data(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

m2 = Matrix().set_data(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

mx = Matrix().set_data(
    [
        [1, 2],
        [4, 5],
        [7, 8],
    ])

m3 = m1 + m2
print(m3)
print()
m4 = m1 * 4
print(m4)
print()
m5 = m1 * m2
print(m5)
print()
m6 = m1 * mx
print(m6)
input()
"""
