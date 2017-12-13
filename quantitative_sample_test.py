from quantitative_sample import QuantitativeSample

def normalize(data: list) -> list:
    magnitude = sum(list(map(lambda x: x**2, data))) ** 0.5
    if magnitude == 0:
        magnitude = 1
    for index, value in enumerate(data):
        data[index] = data[index] / magnitude
    return data

DATA = [10, 2, 38, 23, 38, 23, 21]
QS = QuantitativeSample(DATA)



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




print(QS.result['coefficient of variation'] == 59.99421870632576)
print(QS.result)

# with data normalized
QS = QuantitativeSample(normalize(DATA))
print(QS.result['coefficient of variation'] == 59.99421870632576)
print(QS.result)