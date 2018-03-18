from types import GeneratorType
from .qualitative_population import QualitativePopulation


__all__ = ('DataTable',)



class DataTable(list):

    def __init__(self, data: list=[], labels: list=[]):
        self.labels = labels
        list.__init__(self, data)
    
    @property
    def nrows(self) -> int:
        return len(self)

    @property
    def ncols(self) -> int:
        if self.nrows > 0:
            return len(self[0])
        else:
            return 0

    @property
    def dimension(self) -> tuple:
        return (self.nrows, self.ncols,)

    @property
    def rows(self) -> GeneratorType:
        for row in self:
            yield row

    @property
    def columns(self) -> GeneratorType:
        for column_index in range(0, self.ncols):
            column = []
            for row in self:
                column.append(row[column_index])
            yield QualitativePopulation(column)
    
    @property
    def columns_with_labels(self) -> GeneratorType:
        for labeled_column in zip(self.labels, self.columns):
            yield labeled_column

    @property
    def frequency_table(self) -> GeneratorType:
        for column in self.columns_with_labels:
            yield column[0]
            yield column[1].summary