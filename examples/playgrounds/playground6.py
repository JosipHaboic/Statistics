import os
import json
from pymymath.statistics.quantitative_population import QuantitativePopulation
from pymymath.statistics.quantitative_sample import QuantitativeSample
from pymymath.util import split_month_to_weeks
from pprint import pprint

os.chdir(os.path.dirname(os.path.abspath(__file__)))

DATA = None
with open('../data/GENERATED_DATASET.json', 'r') as fp:
    DATA = json.loads(fp.read())


QP = QuantitativePopulation(DATA['max_temperatures_summer_month_31_days'])
print('Maximum temperatures for random summer month')
print(QP)
print()
print('Statistics for that month:')
pprint(QP.summary)

print()
WEEKS = [week for week in split_month_to_weeks(QP)]
print('Weeks of month')
pprint(WEEKS)

print('Statistics for weeks:')
for week_number, week in enumerate(WEEKS, 1):
    print('Week: {}'.format(week_number))
    pprint(week.summary)

