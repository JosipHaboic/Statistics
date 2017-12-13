__all__ = ['DataCleaner']

class DataCleaner:

    def __init__(self, data=[], clean_list=[]):
        self.data = data
        self.clean_list = clean_list

    @property
    def cleaned(self):
        return list(
            filter(self.clean, self.data)
        )

    def clean(self, item):
        if item in self.clean_list:
            return False
        return True

"""
dc = DataCleaner([1,2,3,None], [None])
print(dc.cleaned == [1,2,3])
"""