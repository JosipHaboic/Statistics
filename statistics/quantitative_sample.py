from . abstract.population import AbstractQuantitativePopulation
from . quantitative_population import QuantitativePopulation


class QuantitativeSample(QuantitativePopulation):

    def __init__(self, data=[], name=None):
        QuantitativePopulation.__init__(self, data, name)

    @property
    def variance(self) -> float:
        MEAN = self.mean # cache var in constant
        return sum(map(lambda y: (y - MEAN)**2, self)) / (self.n - 1)

    @staticmethod
    def linear_correlation(population_a: AbstractQuantitativePopulation, population_b: AbstractQuantitativePopulation) -> QuantitativePopulation:
        ''' Linear correlation refers to straight-line relationships between two variables.
            A correlation can range between -1 (perfect negative relationship) and +1 (perfect positive relationship),
            with 0 indicating no straight-line relationship '''
        return QuantitativePopulation.covariance(population_a, population_b) / ((population_a.variance * population_b.variance) ** 0.5)
