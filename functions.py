def continous_uniform_distribution(min, max):
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


