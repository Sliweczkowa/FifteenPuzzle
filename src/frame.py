from typing import List


class Frame:

    def __init__(self, r: int, c: int, vals: List[int]):
        self.row = r
        self.column = c
        self.values = vals

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, row):
        if type(row) is not int:
            raise Exception("row must be of type int")
        # TODO: add exception for minimal value
        self._row = row

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, col):
        if type(col) is not int:
            raise Exception("column must be of type int")
        # TODO: add exception for minimal value
        self._column = col

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        if len(values) is not self.row*self.column:
            raise Exception("values len must be the product of row and column")
        if not all(type(v) is int for v in values):
            raise Exception("all values items must be of type int")
        if not all( 0 < v < self.row*self.column for v in values):
            raise Exception("all values items must be of value <0, row*column)")
        if len(values) is not len(set(values)):
            raise Exception("values items must not repeat")
        self._values = values
