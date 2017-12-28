from random import randint
from pprint import pprint
from matplotlib import pyplot
from pymymath.statistics.quantitative_population import QuantitativePopulation


def loto(min=1, max=49, combination_length=7):
    loto_numbers = set()
    while len(loto_numbers) < combination_length:
        loto_numbers.add(randint(min, max))

    return sorted(list(loto_numbers))

LOTO_NUMBERS = loto(1,49,7)
MY_GUESS = [8, 12, 20, 24, 29, 34, 42]

QP = QuantitativePopulation(LOTO_NUMBERS)
MY_QP = QuantitativePopulation(MY_GUESS)

print('Your numbers: {}'.format(MY_GUESS))
print('Your numbers summmary:')
pprint(MY_QP.summary)

print('Loto numbers: {}'.format(LOTO_NUMBERS))
print('Loto numbers summary:')
pprint(QP.summary)

COVAR = QuantitativePopulation.covariance(QP,MY_QP)
TTEST = QuantitativePopulation.t_test(QP,MY_QP)
DOF = QuantitativePopulation.degrees_of_freedom(QP,MY_QP)
LC = QuantitativePopulation.linear_correlation(QP,MY_QP)
print('''
Covariance:         {}
T-test:             {}
Degrees of freedom: {}
Linear covariance:  {}
'''.format(COVAR, TTEST, DOF, LC))

GUESSED = set(LOTO_NUMBERS).intersection(set(MY_GUESS))
print('Guessed numbers:{}'.format(GUESSED))
print(help(QuantitativePopulation.linear_correlation))

pyplot.plot(LOTO_NUMBERS, 'r+', MY_GUESS, 'g+')
pyplot.grid()
pyplot.show()