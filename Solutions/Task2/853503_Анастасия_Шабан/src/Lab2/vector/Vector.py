from collections.abc import Iterable


class DiffSize(Exception):
    def __init__(self):
        super(Exception, self).__init__('dimension mismatch')


class Vector:
    def __init__(self, arg):
        if isinstance(arg, Iterable):
            self.vector_type = type(arg[0])
            for item in arg:
                if not isinstance(item, self.vector_type):
                    raise TypeError('Different data types')
            self.elements = list(arg)
            self.vector_size = len(self.elements)
        elif isinstance(arg, int):
            if arg < 0:
                raise ValueError('Negative size')
            self.elements = []
            self.vector_size = arg
            self.vector_type = int
        else:
            raise TypeError('Data type error')

    def __setitem__(self, index, value):
        if isinstance(value, self.vector_type):
            self.elements[index] = value
        else:
            raise TypeError("Different data types")

    def __getitem__(self, index):
        return self.elements[index]

    def __iter__(self):
        return self.elements.__iter__()

    @property
    def size(self):
        return self.vector_size

    def __len__(self):
        return self.vector_size

    @property
    def dtype(self):
        return self.vector_type

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return 'Vector {}'.format(str(self))

    def __add__(self, second_element):
        if not isinstance(second_element, Vector):
            raise TypeError('Different type')
        if self.size != second_element.size:
            raise DiffSize()
        return Vector([i + j for i, j in zip(self, second_element)])

    def __sub__(self, second_element):
        if not isinstance(second_element, Vector):
            raise TypeError('Different type')
        if self.size != second_element.size:
            raise DiffSize()
        return Vector([i - j for i, j in zip(self, second_element)])

    def __mul__(self, multiplier):
        return Vector([elem * multiplier for elem in self])

    def __eq__(self, second_vector):
        if self.size == len(second_vector) and all([i == j for i, j in zip(self, second_vector)]):
            return True
        else:
            return False


if __name__ == "__main__":
    a = Vector([8, 1, 2, 5, 2])
    b = Vector([1, 2, 3, 15, 7])

    print('a = ', a)
    print('b = ', b)
    print('Сумма: ', a + b)
    print('Разность: ', a - b)
    print('Умножение на число ', a * 5)
    print('Сравнить: ', a == b)
