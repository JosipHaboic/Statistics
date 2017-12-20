from quantitative_population import QuantitativePopulation
from pprint import pprint

def normalize(data: list) -> list:
    magnitude = sum(map(lambda x: x**2, data)) ** 0.5
    if magnitude == 0:
        magnitude = 1
    for index, value in enumerate(data):
        data[index] = value / magnitude
    return data

DATA = [10, 2, 38, 23, 38, 23, 21]
QS = QuantitativePopulation(DATA)


STANDARD_DEVIATION = round(13.284434142115, 12)
VARIANCE = round(176.47619047619, 12)
N = 7
MEAN = round(22.142857142857, 12)
STANDARD_ERROR_OF_MEAN = round(5.0210441497503, 12)


def test():
    assert round(QS.standard_deviation, 12) == STANDARD_DEVIATION
    assert round(QS.variance, 12) == VARIANCE
    assert QS.n == N
    assert round(QS.mean, 12) == MEAN
    assert round(QS.standard_error, 12) ==  STANDARD_ERROR_OF_MEAN
    print('TESTS PASSESD')

test()

def test2():
    from random import randint
    DATA = [randint(-100,100) for x in range(100)]
    QS = QuantitativePopulation(DATA)
    pprint(QS.result)

test2()