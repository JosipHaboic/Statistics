import os
import json
from pprint import pprint
from pymymath.statistics.quantitative_sample import QuantitativeSample
from pymymath.statistics.algorithms.binning.unsupervised import UnsupervisedBinning


os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('../data/GENERATED_DATASET.json', 'r') as fp:
    DATA = QuantitativeSample(json.loads(fp.read())['max_temperatures_summer_month_31_days'])

pprint('Data:\n {}'.format(DATA))
print('Data size: {}'.format(len(DATA)))

BINNED_DATA = [binned_sample for binned_sample in UnsupervisedBinning.equal_width_binning(DATA, 4)]
pprint('Binned data:')
for i in BINNED_DATA:
    print('Binned size: {}'.format(len(i)))
    print(i)
    print()