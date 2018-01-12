import os
from pprint import pprint
from pymymath.statistics.qualitative_population import QualitativePopulation
from pymymath.statistics.algorithms.classification.frequency_table import FrequencyTable
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
    with open('../data/contact_lenses.txt','r') as fp:
        for line in fp.readlines():yield list(map(lambda x: x.replace('\n',''),line.split('\t')))


DATA = [ITEM for ITEM in load_data()]
LABELS = DATA[0]

FT = FrequencyTable(DATA)

del DATA[0]


# CATEGORIES = {}
# for index, label in enumerate(LABELS):
#     CATEGORIES[label] = QualitativePopulation([])
#     for item in DATA:
#         CATEGORIES[label].append(item[index])

# for category_name, category_population in CATEGORIES.items():
#     print(category_name)
#     pprint(category_population.summary)

# pprint(FT.summary)