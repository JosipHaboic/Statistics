import json
from os import chdir
from os.path import dirname, abspath
chdir(dirname(abspath(__file__)))
from pprint import pprint
from matplotlib import pyplot
from pymymath.statistics.quantitative_sample import QuantitativeSample


with open('ME_PS2.json', 'r') as fp:
    DATA = json.loads(fp.read())


CLEAN_DATA = list(filter(lambda x: x != None, DATA['dataset']['value']))
QP = QuantitativeSample(CLEAN_DATA)
print('Index potrosackih cjena')
pprint(QP.summary)

pyplot.plot(QP, 'ko')
pyplot.grid()
pyplot.show()

# dimension
# label
# source
# status
# updated
# value