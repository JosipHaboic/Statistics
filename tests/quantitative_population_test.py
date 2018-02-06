import numpy
from pymymath.statistics.quantitative_sample import QuantitativeSample
from pymymath.statistics.quantitative_population import QuantitativePopulation
from pprint import pprint
from matplotlib import pyplot


def normalize(data: list) -> list:
    MAGNITUDE = sum(map(lambda x: x**2, data)) ** 0.5
    if MAGNITUDE == 0:
        MAGNITUDE = 1
    for index, value in enumerate(data):
        data[index] = value / MAGNITUDE
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
    assert round(QS.standard_error, 12) == STANDARD_ERROR_OF_MEAN
    print('TEST 1 PASSESD')
    print('TEST 2 RESULTS:')
    pprint(QS.summary)
    print()




def test2():
    TEMPEARATURE = QuantitativePopulation(
        [83, 64, 72, 81, 70, 68, 65, 75, 71, 85, 80, 72, 69, 75])
    HUMIDITY = QuantitativePopulation(
        [86, 65, 90, 75, 96, 80, 70, 80, 91, 85, 90, 95, 70, 70])

    assert round(QuantitativePopulation.covariance(
        TEMPEARATURE, HUMIDITY), 2) == 19.78
    assert round(QuantitativePopulation.linear_correlation(
        TEMPEARATURE, HUMIDITY), 2) == 0.32
    print('TEST 2 PASSESD')
    print('TEST 2 RESULTS:')
    pprint(TEMPEARATURE.summary)
    print(32 * '-')
    pprint(HUMIDITY.summary)
    print()




def test3():
    FAILED_ORING_TEMPERATURES = QuantitativeSample([53, 56, 57, 70, 70, 70, 75])
    INTACT_ORING_TEMPERATURES = QuantitativeSample([63, 66, 67, 67, 67,
                                 68, 69, 70, 72, 73, 75, 76, 76, 78, 79, 80, 81])

    T_TEST = QuantitativeSample.t_test(FAILED_ORING_TEMPERATURES, INTACT_ORING_TEMPERATURES)
    assert round(T_TEST, 2) == -2.62
    print('TEST 3 PASSED')
    print('t test = {}'.format(T_TEST))

test1()
test2()
test3()