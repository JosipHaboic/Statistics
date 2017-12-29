from pymymath.statistics.quantitative_sample import QuantitativeSample
from pprint import pprint

QS1 = QuantitativeSample([1,2,3,4,5,6,7,8,9,10])
QS2 = QuantitativeSample([10,9,8,7,6,5,4,3,2,1])


pprint(QS1.summary)
pprint(QS2.summary)