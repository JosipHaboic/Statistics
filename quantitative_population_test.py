import numpy
from quantitative_sample import QuantitativeSample
from quantitative_population import QuantitativePopulation
from pprint import pprint
from matplotlib import pyplot

def normalize(data: list) -> list:
    magnitude = sum(map(lambda x: x**2, data)) ** 0.5
    if magnitude == 0:
        magnitude = 1
    for index, value in enumerate(data):
        data[index] = value / magnitude
    return data

def test1():
    DATA = [10, 2, 38, 23, 38, 23, 21]
    QS = QuantitativeSample(DATA)
    STANDARD_DEVIATION = round(13.284434142115, 12)
    VARIANCE = round(176.47619047619, 12)
    N = 7
    MEAN = round(22.142857142857, 12)
    STANDARD_ERROR_OF_MEAN = round(5.0210441497503, 12)

    assert round(QS.standard_deviation, 12) == STANDARD_DEVIATION
    assert round(QS.variance, 12) == VARIANCE
    assert QS.n == N
    assert round(QS.mean, 12) == MEAN
    assert round(QS.standard_error, 12) ==  STANDARD_ERROR_OF_MEAN
    print('TEST 1 PASSESD')

test1()

def test2():
    TEMPEARATURE = QuantitativePopulation([83,64,72,81,70,68,65,75,71,85,80,72,69,75])
    HUMIDITY = QuantitativePopulation([86,65,90,75,96,80,70,80,91,85,90,95,70,70])

    assert round(QuantitativePopulation.covariance(TEMPEARATURE, HUMIDITY), 2) == 19.78
    assert round(QuantitativePopulation.linear_correlation(TEMPEARATURE, HUMIDITY), 2) == 0.32
    print('TEST 2 PASSESD')

test2()