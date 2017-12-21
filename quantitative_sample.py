from quantitative_population import QuantitativePopulation


class QuantitativeSample(QuantitativePopulation):

    def __init__(self, data=[]):
        QuantitativePopulation.__init__(self, data)

    @property
    def variance(self) -> float:
        mean = self.mean
        return sum(map(lambda y: (y - mean)**2, self)) / (self.n - 1)
    