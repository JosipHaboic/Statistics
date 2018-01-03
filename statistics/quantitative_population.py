'''
Relationship of the Mean, Median, and Mode
The relationship of the mean, median, and mode to each other can provide some information
about the relative shape of the data distribution. If the mean, median, and mode are
approximately equal to each other, the distribution can be assumed to be approximately
symmetrical. If the mean > median > mode, the distribution will be skewed to the left or
positively skewed. If the mean < median < mode, the distribution will be skewed to the
right or negatively skewed.

There is an ordering to these means if all values in data set are positive.
min <= harmonic mean <= geometric mean <= arithmetic mean <= max.
'''

from collections import Counter
from functools import reduce
from operator import mul
import math
from . abstract.population import Population

__all__ = ['QuantitativePopulation']


class QuantitativePopulation:
    pass


class QuantitativePopulation(Population):
    '''Quantitative data is a numerical measurement expressed not by means of a natural
       language description, but rather in terms of numbers. However, not all numbers are
       continuous and measurable. For example, the social security number is a number, but not
       something that one can add or subtract.
       Quantitative data always are associated with a scale measure.
    '''

    def __init__(self, data=[], assumed_mean=0):
        Population.__init__(self, data)
        self.assumed_mean = assumed_mean

    def normalize(self):
        '''Normalize values in dataset so they are in range 0-1'''
        m = self.mean
        if m == 0:
            return
        for index, value in enumerate(self):
            self[index] = self[index] / m

    @property
    def n(self) -> float:
        '''Number of items in dataset'''
        return len(self)

    @property
    def mean(self) -> float:
        ''' Arithmetic mean of data set.
            The arithmetic mean is relevant any time several quantities add together to produce a total.
            The arithmetic mean answers the question, "if all the quantities had the same value, what
            would that value have to be in order to achieve the same total?" '''
        try:
            return sum(self) / self.n
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

    @property
    def geometric_mean(self) -> float:
        ''' The geometric mean is a type of average, usually used for growth rates, like population growth or interest rates. 
            While the arithmetic mean adds items, the geometric mean multiplies items. 
            Also, you can only get the geometric mean for positive numbers.
            the geometric mean is relevant any time several quantities multiply together to produce a product.
            The geometric mean answers the question, "if all the quantities had the same value, 
            what would that value have to be in order to achieve the same product?"'''
        try:
            return reduce(mul, self) ** (1 / len(self))
        except (OverflowError, ZeroDivisionError) as e:
            print(e)
            return float('nan')

    @property
    def harmonic_mean(self):
        ''' In mathematics, the harmonic mean (sometimes called the subcontrary mean) is one of several kinds of average,
            and in particular one of the Pythagorean means. 
            Typically, it is appropriate for situations when the average of rates is desired.
            The harmonic mean can be expressed as the reciprocal of the arithmetic mean of the reciprocals of the given set of observations.
            The harmonic mean is one of the three Pythagorean means.
            For all positive data sets containing at least one pair of nonequal values, 
            the harmonic mean is always the least of the three means,
            [1] while the arithmetic mean is always the greatest of the three and the geometric mean is always in between.
            (If all values in a nonempty dataset are equal, the three means are always equal to one another; 
            e.g., the harmonic, geometric, and arithmetic means of {2, 2, 2} are all 2.) '''
        n = self.n
        try:
            harmonics = sum([1 / x for x in self])
        except ZeroDivisionError as e:
            print(e)
            return float('nan')
        return n / harmonics

    @property
    def median(self) -> float:
        ''' The median is the "middle value" in a set. That is, the median is the number in the center
            of a data set that has been ordered sequentially.'''
        d = sorted(self)
        if self.n % 2 == 0:
            i = (self.n + 1) / 2
            left = math.floor(i)
            right = math.ceil(i)
            return (d[left - 1] + d[right - 1]) / 2
        else:
            i = int((self.n + 1) / 2)
            return d[i - 1]

    @property
    def midrange(self):
        ''' The midrange is the arithmetic mean strictly between the minimum and the maximum
            value in a data set. '''
        return (self.max + self.min) / 2

    @property
    def mean_test(self) -> dict:
        ''' Test if the means are aligned. '''
        result = None
        try:
            result = True if (self.min <= self.harmonic_mean <= self.geometric_mean <= self.mean <= self.max) else False
        except TypeError as e:
            result = e

        return {
            'passed': result,
            'test': '{:+.2f} <= {:+.2f} <= {:+.2f} <= {:+.2f} <= {:+.2f}'.format(self.min, self.harmonic_mean, self.geometric_mean, self.mean, self.max)
        }

    @property
    def mean_deviation(self) -> float:
        ''' Average of absolute differences (differences expressed without plus or minus sign)
            between each value in a set of values, and the average of all values of that set. '''
        m = self.mean
        try:
            return sum(map(lambda x: abs(x - m), self)) / self.n
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

    @property
    def variance(self) -> float:
        ''' A measure of data dispersion. '''
        mean = self.mean
        try:
            return sum(map(lambda x: (x - mean)**2, self)) / (self.n)
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

    @property
    def standard_deviation(self) -> float:
        ''' The square root of variance. '''
        return self.variance ** 0.5

    @property
    def range(self) -> float:
        ''' The difference between maximum and minimum. '''
        return max(self) - min(self)

    @property
    def mode(self) -> tuple:
        ''' The mode is the most common or "most frequent" value in a data set. '''
        return Counter(self).most_common(1)

    @property
    def skewness(self):
        ''' A measure of symmetry or asymmetry in the distribution of data. '''
        mean = self.mean
        std = self.standard_deviation
        n = self.n
        try:
            return (n / ((n - 1) * (n - 2))) * sum(map(lambda x: ((x - mean) / std) ** 3, self))
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

    @property
    def kurtosis(self):
        ''' A measure of whether the data are peaked or flat relative to a normal distribution. '''
        mean = self.mean
        std = self.standard_deviation
        n = self.n
        try:
            return sum(map(lambda x: (x - mean) ** 4, self)) / ((n - 1) * std ** 4)
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

    @property
    def coefficient_of_variation(self) -> float:
        ''' A measure of data dispersion divided by mean in percents. '''
        try:
            return (self.standard_deviation / self.mean) * 100
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

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
        ''' The standard error (SE) of a parameter is the standard deviation 
            of its sampling distribution or an estimate of the standard deviation.
            If the parameter or the statistic is the mean, it is called the standard error of the mean (SEM)'''
        try:
            return self.standard_deviation / (self.n ** 0.5)
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

    @property
    def standard_normal_distribution(self):
        mean = self.mean
        std = self.standard_deviation
        try:
            return QuantitativePopulation([(x - mean) / std for x in self])
        except ZeroDivisionError as e:
            print(e)
            return float('nan')

    def most_common(self, n=None):
        if n and n > self.n:
            n = self.n
        return Counter(self).most_common(n)

    @property
    def negative_values(self):
        return QuantitativePopulation(list(filter(lambda x: x < 0, self)))

    @property
    def positive_values(self):
        return QuantitativePopulation(list(filter(lambda x: x > 0, self)))

    @property
    def unique(self):
        return QuantitativePopulation(set(self))

    @property
    def summary(self) -> dict:
        return {
            'n': self.n,
            'sum': self.sum,
            'squared_sum': self.squared_sum,
            'sum_of_squares': self.sum_of_squares,
            'min': self.min,
            'max': self.max,
            'range': self.range,
            'midrange': self.midrange,
            'mode': self.mode,
            'skewness': self.skewness,
            'mean': self.mean,
            'mean_deviation': self.mean_deviation,
            'geometric_mean': self.geometric_mean,
            'harmonic_mean': self.harmonic_mean,
            'median': self.median,
            'variance': self.variance,
            'standard_deviation': self.standard_deviation,
            'kurtosis': self.kurtosis,
            'standard_error': self.standard_error,
            'coefficient_of_variation': self.coefficient_of_variation,
            'mean_test': self.mean_test,
            'number_of_positive_values': self.positive_values.n,
            'number_of_negative_values': self.negative_values.n,
            'sum_of_positive_values': self.positive_values.sum,
            'sum_of_negative_values': self.negative_values.sum
        }

    @staticmethod
    def t_test(population_a: QuantitativePopulation, population_b: QuantitativePopulation) -> float:
        ''' The t-test can be used, for example, 
            to determine if two sets of data are significantly different from each other. '''
        n_a = population_a.n
        n_b = population_b.n
        mean_a = population_a.mean
        mean_b = population_b.mean
        std_a = population_a.standard_deviation
        std_b = population_b.standard_deviation
        return (mean_a - mean_b) / ((((std_a ** 2) / n_a) + ((std_b ** 2) / n_b)) ** 0.5)

    @staticmethod
    def degrees_of_freedom(population_a: QuantitativePopulation, population_b: QuantitativePopulation) -> float:
        ''' the number of degrees of freedom is the number of values in 
            the final calculation of a statistic that are free to vary. '''
        return (population_a.n - 1) + (population_b.n - 1)

    @staticmethod
    def covariance(population_a: QuantitativePopulation, population_b: QuantitativePopulation) -> float:
        ''' In probability theory and statistics, covariance is a measure of the joint 
            variability of two random variables.If the greater values of one variable mainly 
            correspond with the greater values of the other variable,
            and the same holds for the lesser values, i.e., the variables tend
            to show similar behavior, the covariance is positive.
            In the opposite case, when the greater values of one variable mainly correspond to
            the lesser values of the other, i.e., the variables tend to show opposite behavior, the covariance is negative. 
            The sign of the covariance therefore shows the tendency in the linear relationship between the variables.
            The magnitude of the covariance is not easy to interpret because it is not normalized
            and hence depends on the magnitudes of the variables. '''
        if population_a.n != population_b.n:
            raise Exception('Populations not the same size.')
        else:
            n = population_a.n
            mean_a = population_a.mean
            mean_b = population_b.mean
            return sum([(population_a[i] - mean_a) * (population_b[i] - mean_b) for i in range(n)]) / n
        return float('nan')

    @staticmethod
    def linear_correlation(population_a: QuantitativePopulation, population_b: QuantitativePopulation) -> float:
        ''' Linear correlation refers to straight-line relationships between two variables.
            A correlation can range between -1 (perfect negative relationship) and +1 (perfect positive relationship),
            with 0 indicating no straight-line relationship '''
        return QuantitativePopulation.covariance(population_a, population_b) / (population_a.standard_deviation * population_b.standard_deviation)

    @staticmethod
    def correlation_coefficient(population_a: QuantitativePopulation, population_b: QuantitativePopulation):
        ''' Alias for linear_correlation.
            Correlation coefficient refers to straight-line relationships between two variables.
            A correlation can range between -1 (perfect negative relationship) and +1 (perfect positive relationship),
            with 0 indicating no straight-line relationship '''
        return QuantitativePopulation.linear_correlation(population_a, population_b)
