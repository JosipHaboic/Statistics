import json
import os
from pprint import pprint
from matplotlib import pyplot
from pymymath.statistics.quantitative_population import QuantitativePopulation
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DATA = None
with open('../data/GENERATED_DATASET.json', 'r') as fp:
    DATA = json.loads(fp.read())


QS = QuantitativePopulation(DATA['positives'])
pprint(QS.summary)

# pyplot.grid()
# pyplot.plot(DATA['positives'], 'k-')
# pyplot.show()
# qp = QuantitativePopulation()
# pprint(qp.summary)