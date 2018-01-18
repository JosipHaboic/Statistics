from types import FunctionType
from functools import reduce
from operator import mul
from math import ceil, floor
from collections import Counter

def average(elements: list) -> float:
    return sum(elements) / len(elements)

def weighted_averge(elements: list, weights: list) -> float:
    weights_sum = sum(weights)
    ziped_values = zip(elements, weights)
    return sum(map(lambda x: x[0] * x[1], ziped_values)) / weights_sum

def arithmetic_mean(elements: list) -> float:
    return average(elements)

def geometric_mean(elements: list) -> float:
    return reduce(mul, elements) ** (1 / len(elements))

def harmonic_mean(elements: list) -> float:
    if all(elements):
        return len(elements) / (sum(map(lambda x: 1 / x, elements)))
    else:
        print('''Error: One or more zeros encountered in data, can't divide by zero.''')
        return float('nan')

def harmonic_mean_of_two_numbers(a: float, b: float) -> float:
    return (2* a * b) / (a + b)

def median(elements: list) -> float:
        d = sorted(elements)
        n = len(elements)
        if n % 2 == 0:
            i = (n + 1) / 2
            left = floor(i)
            right = ceil(i)
            return (d[left - 1] + d[right - 1]) / 2
        else:
            i = int((n + 1) / 2)
            return d[i - 1]

def midrange(elements: list):
        return (max(elements) + min(elements)) / 2

def range(elements: list):
    return max(elements) - min(elements)

def mode(elements: list):
    return Counter(elements).most_common()

def percentage_change(final_value: float, initial_value: float) -> float:
    return ((final_value - initial_value) / initial_value) * 100

def total_percentage_change(final_value: float, initial_value: float) -> float:
    return (a + b + ((a * b) / 100))

def interest(principal: float, rate: float, time: float) -> float:
    return (principal * rate * time) / 100

def compound_interest(principal: float, rate: float, time: float) -> float:
    return principal * (1 + ((rate / 100)) ** time) - principal

def interest_ammount(principal: float, interest: float) -> float:
    return principal + interest

def population_formula(population: int, rate_of_annual_change_percent, after_n_years: int) -> float:
    return population * ((1 + (annual_change_percent / 100)) ** after_n_years)

def depreciation_formula(original_value: float, final_value: float, rate_of_annual_depreciation: float, after_n_years: int) -> float:
    return original_value * ((1 - (rate_of_annual_depreciation / 100)) ** after_n_years)

def absolute_growth(final_value: float, initial_value: float) -> float:
    return final_value - initial_value

def factorial(k: int) -> float:
    if k == 0: return 1
    return reduce(mul, range(1, k + 1))

def binominal_coefficient(n: int, x: int) -> float:
    return factorial(n) / (factorial(x) * factorial(n - x))

def binominal_probability_formula(number_of_trials: int, success_probability: float, x: float) -> float:
    return binominal_coefficient(number_of_trials, x) * (success_probability ** x) * ((1 - success_probability) ** (n - x))

def mean_of_binominal_random_variable(number_of_trials: int, success_probability: float) -> float:
    return number_of_trials * success_probability

def standard_deviation_of_binominal_random_variable(number_of_trials: int, success_probability: float) -> float:
    return (number_of_trials * success_probability * (1 - success_probability)) ** 0.5

def probability_for_equally_likely_outcomes(number_of_ways_event_can_occur: int, total_number_of_possible_outcomes: int) -> float:
    return number_of_ways_event_can_occur / total_number_of_possible_outcomes

def continous_uniform_distribution(min, max) -> FunctionType:
    def f(x):
        if min <= x <= max:
            return 1 / (max - min)
        else:
            return 0
    return f

def continous_uniform_distribution_mean(min, max) -> float:
    return (max + min) / 2

def continous_uniform_distribution_variance(min, max) -> float:
    return ((max - min) ** 2) / 12

def convert_to_ones_and_zeroes(dataset: list) -> list:
    return [ (1 if x > 0 else 0) for x in dataset ]

def bernoulli(x: int, p: float = 0.1) -> float:
    if x == 1:
        return p
    elif x == 0:
        return 1 - p

def bernoulli_mean(p: float) -> float:
    return p

def bernoulli_variance(p: float) -> float:
    return p * (1 - p)

def unit_step(x) -> int:
    if x < 0:
        return 0
    else:
        return 1

def sigmoid(beta) -> FunctionType:
    from math import exp
    def f(x):
        return 1 / (1 + exp(-beta*x))
    return f

def piecewise_linear(a, b, min_x, max_x) -> FunctionType:
    def f(x):
        if x <= min_x:
            return 0
        elif max_x > x > min_x:
            return a*x + b
        else:
            return 1
    return f

