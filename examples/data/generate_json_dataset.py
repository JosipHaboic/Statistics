import json
from random import randint, random

with open('GENERATED_DATASET.json', 'w') as fp:
    fp.write(json.dumps({
        'positives' : [randint(1,100) for x in range(100)],
        'negatives' : [randint(-100,-1) for x in range(100)],
        'mixed' : [randint(-100,100) for x in range(100)],
        'person_heights' : [randint(160, 210) for x in range(100)],
        'max_temperatures_summer_month_30_days' : [randint(25, 38) for x in range(1, 31)],
        'max_temperatures_summer_month_31_days' : [randint(25, 38) for x in range(1, 32)],
        'max_temperatures_winter_month_30_days' : [randint(-15, 10) for x in range(1, 31)],
        'max_temperatures_winter_month_31_days' : [randint(-15, 10) for x in range(1, 32)],
    }))

