'''
Relationship of the Mean, Median, and Mode
The relationship of the mean, median, and mode to each other can provide some information
about the relative shape of the data distribution. If the mean, median, and mode are
approximately equal to each other, the distribution can be assumed to be approximately
symmetrical. If the mean > median > mode, the distribution will be skewed to the left or
positively skewed. If the mean < median < mode, the distribution will be skewed to the
right or negatively skewed.
'''

from collections import Counter
from functools import reduce
from operator import mul
import math
from abstract.sample import Sample

__all__ = ['QuantitativeSample']

class QuantitativeSample(Sample):

    def __init__(self, data=[], assumed_mean = 0):
        Sample.__init__(self, data)
        self.assumed_mean = assumed_mean

    def normalize(self):
        m = self.mean
        if m == 0:
            return
        for index, value in enumerate(self):
            self[index] = self[index] / m

    @property
    def n(self) -> float:
        return len(self)
        
    @property
    def mean(self) -> float:
        return sum(self) / self.n

    @property
    def geometric_mean(self) -> float:
        return reduce(mul, self) ** (1 / self.n)

    @property
    def median(self) -> float:
        d = sorted(self)
        if self.n % 2 == 0:
            i = (self.n + 1) / 2
            left = math.floor(i)
            right = math.ceil(i)
            return (d[left-1] + d[right-1]) / 2
        else:
            i = int((self.n + 1) / 2)
            return d[i-1]

    @property
    def midrange(self):
        return (self.max + self.min) / 2

    @property
    def variance(self) -> float:
        mean = self.mean
        return sum(map(lambda y: (y - mean)**2, self)) / (self.n - 1)

    @property
    def standard_deviation(self) -> float:
        v = self.variance
        return v ** 0.5

    @property
    def range(self) -> float:
        return max(self) - min(self)

    @property
    def mode(self) -> tuple:
        return Counter(self).most_common(1)
    
    @property
    def coefficient_of_variation(self) -> float:
        return (self.standard_deviation / self.mean) * 100

    @property
    def min(self) -> float:
        return min(self)

    @property
    def max(self) -> float:
        return max(self)

    @property
    def sum(self):
        return sum(self)

    @property
    def squared_sum(self) -> float:
        return sum(self) ** 2

    @property
    def sum_of_squares(self) -> float:
        return sum(
            list(
                map(lambda x: x**2, self)
                )
            )

    @property
    def standard_error(self) -> float:
        return self.standard_deviation / (self.n ** 0.5)
    
    @property
    def selfTtest(self) -> float:
        return (self.mean - self.assumed_mean) / (self.standard_deviation / (self.n ** 0.5))
        
    @property
    def result(self) -> dict:
        return {
            'data' : self,
            'n' : self.n,
            'sum' : self.sum,
            'squared_sum' : self.squared_sum,
            'sum_of_squares' : self.sum_of_squares,
            'min' : self.min,
            'max' : self.max,
            'range' : self.range,
            'mode' : self.mode,
            'mean' : self.mean,
            'geometric_mean' : self.geometric_mean,
            'median' : self.median,
            'variance' : self.variance,
            'standard_deviation' : self.standard_deviation,
            'standard_error' : self.standard_error,
            'coefficient_of_variation' : self.coefficient_of_variation,
            't_test' : self.selfTtest
        }
