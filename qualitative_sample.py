from collections import Counter
from abstract.sample import Sample

__all__ = ['QuantitativeSample']

class QuantitativeSample(Sample):

    def __init__(self, data):
        Sample.__init__(self, data)

    @property
    def counted(self):
        return Counter(self).most_common()

