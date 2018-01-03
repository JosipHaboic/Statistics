import json
from random import randint, random

with open('GENERATED_DATASET.json', 'w') as fp:
    fp.write(json.dumps({
        'positives' : [randint(1,100) for x in range(100)],
        'negatives' : [randint(-100,-1) for x in range(100)],
        'mixed' : [randint(-100,100) for x in range(100)]
    }))

