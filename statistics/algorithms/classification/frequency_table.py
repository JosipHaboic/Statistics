from pprint import pprint, pformat
from collections import Counter
from types import GeneratorType


__all__ = ('FrequencyTable',)

class FrequencyTable:

    def __init__(self, name: str, data=None):
        self.name = name
        self.data = data

    def get_row_with_label(self, n) -> list:
        return [self.class_labels[n], *self.get_row(n)]

    def get_row(self, n: int) -> list:
        return self.frequency_table[n]

    def get_rows(self) -> list:
        return [row for row in self.frequency_table]

    def get_column(self, n: int) -> list:
        return [i[n] for i in self.frequency_table]

    def get_column_with_label(self, n: int) -> list:
        return [self.labels[n]] + [i[n] for i in self.frequency_table]

    @property
    def frequency_table(self) -> list:
        return [tuple(x.values()) for x in self.values]

    @property
    def labels(self) -> list:
        return list(self.values[0].keys())

    @property
    def values(self) -> list:
        return list(self.data.values())

    @property
    def class_labels(self) -> list:
        return list(self.data.keys())

    @property
    def number_of_rows(self) -> int:
        return len(self.frequency_table)

    @property
    def number_of_columns(self) -> int:
        return len(self.frequency_table[0])

    def __repr__(self):
        return '''\n{:<32}\n{:<32}\n{:<32}\n{:<32}\n{:<32}\n
        '''.format(
            32 * '-',
            self.name,
            32 * '-',
            '\t'.join(self.labels),
            '\n'.join([str(list(x.values())) for x in self.values])
        )