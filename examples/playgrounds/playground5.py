import os
import json
from pymymath.statistics.quantitative_population import QuantitativePopulation
from pymymath.statistics.algorithms.binning.unsupervised import UnsupervisedBinning

from pprint import pprint

os.chdir(os.path.dirname(os.path.abspath(__file__)))

DATA = None
with open('../data/GENERATED_DATASET.json', 'r') as fp:
    DATA = json.loads(fp.read())

QP = QuantitativePopulation(sorted(DATA['positives']))

print()
print(QP)
pprint(QP.summary)
print()

BINNED = [binned for  binned in UnsupervisedBinning.equal_width_binning(QP, 8)]
pprint(BINNED)

AVERAGES = [binned.mean for binned in BINNED]
print(AVERAGES)