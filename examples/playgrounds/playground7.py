import os
import json
import random
from pprint import pprint
from pymymath.statistics.quantitative_population import QuantitativePopulation
from pymymath.statistics.quantitative_sample import QuantitativeSample
from pymymath.statistics.function_collection import (
    weighted_averge
)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

DATA = None
with open('../data/GENERATED_DATASET.json', 'r') as fp:
    DATA = json.loads(fp.read())

DATA = QuantitativePopulation(DATA['positives'])
WEIGHTS = [random.random() for x in range(0, DATA.n + 1)]

print('Mean: {}'.format(DATA.mean))
print('Weighted mean: {}'.format(weighted_averge(DATA, WEIGHTS)))

