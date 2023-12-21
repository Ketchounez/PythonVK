"""Module for class CustomList"""
from operator import sub  # sub(x,y) = x - y.
from itertools import zip_longest


class CustomList(list):
    """CustomList class"""

    @staticmethod
    def operate(one, two, operation):
        """operation function"""
        res = None

        if operation == '+':
            res = CustomList(map(sum, zip_longest(one, two, fillvalue=0)))
        elif operation == '-':
            one, two = zip(*zip_longest(one, two, fillvalue=0))
            res = CustomList(map(sub, one, two))
        return res

    def __add__(self, other):
        return self.operate(self, other, '+')

    def __radd__(self, other):
        return self.operate(self, other, '+')

    def __sub__(self, other):
        return self.operate(self, other, '-')

    def __rsub__(self, other):
        return self.operate(other, self, '-')

    def __str__(self):
        return f'{str(list(self))}, summa = {str(sum(self))}'

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
