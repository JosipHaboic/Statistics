from collections import Counter

__all__ = ('FrequencyTable',)

class FrequencyTable(list):

    def __init__(self, *data: list, name=None):
        self.name = name
        list.__init__(self, data)

    @property
    def frequency_table(self):
        return Counter(self).most_common()

    


