from collections import Counter
from . abstract.population import Population
from . quantitative_population import QuantitativePopulation

__all__ = ['QualitativePopulation']

class QualitativePopulation(Population):

    def __init__(self, data):
        Population.__init__(self, data)

    @property
    def n(self) -> int:
        return len(self)

    @property
    def frequencies(self) -> list:
        return Counter(self).most_common()

    @property
    def relative_frequencies(self) -> list:
        n = self.n
        relative_frequencies_list = []
        for element, frequency in self.frequencies:
            relative_frequency = frequency / n
            relative_frequencies_list.append((element, relative_frequency, relative_frequency * 100))
        return sorted(relative_frequencies_list,key=lambda x: x[1], reverse=True)

    @property
    def quantitatized_frequencies(self):
        return QuantitativePopulation([x[0] for x in self.frequencies])

    @property
    def summary(self) -> dict:
        return {
            'n' : self.n,
            'frequencies' : self.frequencies,
            'relative_frequencies' : self.relative_frequencies
        }
