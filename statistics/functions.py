from types import FunctionType

__all__ = [
    'continous_uniform_distribution',
    'continous_uniform_distribution_mean',
    'continous_uniform_distribution_variance',
    'convert_to_ones_and_zeroes',
    'bernoulli',
    'bernoulli_mean',
    'bernoulli_variance',
    'unit_step',
    'sigmoid',
    'piecewise_linear'
]

def continous_uniform_distribution(min, max) -> FunctionType:
    def f(x):
        if min <= x <= max:
            return 1 / (max - min)
        else:
            return 0
    return f

def continous_uniform_distribution_mean(min, max):
    return (max + min) / 2

def continous_uniform_distribution_variance(min, max):
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

        