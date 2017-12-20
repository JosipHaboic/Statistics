import random
import math
import json
from quantitative_population import QuantitativePopulation
from qualitative_population import QualitativePopulation
from pprint import pprint
from matplotlib import pyplot
import csv



DATA = []
with open('./Loto7od39_2017.csv', 'r', newline='') as file:
    for row in csv.reader(file, delimiter=' ', quotechar='|'):
        DATA.append(row)

def filter_loto_data(data):
    del data[:2]
    data = list(filter(lambda x: x != [], data))
    data = list(map(lambda x: x[0].split(','), data))
    return data

def map_loto_data(data):
    loto_map = {}
    for record in data:
        loto_map[record[1]] = {}
        loto_map[record[1]]['jackpot'] = float(record[0])
        loto_map[record[1]]['date'] = record[1]
        loto_map[record[1]]['numbers'] = [int(float(x)) for x in record[2:9]]
        loto_map[record[1]]['jackpot_won'] = True if record[9] == 'DA' else False
    return loto_map

def map_samples_to_dates(data: dict):
    samples = {}
    for value in data.values():
        samples[value['date']] = QuantitativePopulation(value['numbers'])
    return samples

CLEANED_DATA = map_loto_data(filter_loto_data(DATA))
MAPPED_SAMPLES = map_samples_to_dates(CLEANED_DATA)
# pprint(MAPPED_SAMPLES)

## show variance for each record
# for k,v in MAPPED_SAMPLES.items():
#     print('''
#         DATE: {}
#         variance: {}
#         numbers: {}
#         '''.format(k, v.summary['variance'], v))

ALL_YEAR_NUMBERS = QuantitativePopulation([])
for sample in MAPPED_SAMPLES.values():
    ALL_YEAR_NUMBERS.extend(sample)

# print(ALL_YEAR_NUMBERS.summary)
QP = QualitativePopulation(ALL_YEAR_NUMBERS)
pprint(QP.summary)