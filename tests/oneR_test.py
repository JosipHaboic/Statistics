# Test based on: http://www.saedsayad.com/oner.htm
from pprint import pprint
from pymymath.statistics.algorithms.classification.oneR import prepare, oneR
from pymymath.statistics.algorithms.classification.frequency_table import FrequencyTable
from pymymath.statistics.algorithms.classification.confusion_matrix import ConfusionMatrix

DATA = [
    ['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play Golf'],
    ['Rainy', 'Hot', 'High', False, 'No'],
    ['Rainy', 'Hot', 'High', True, 'No'],
    ['Overcast', 'Hot', 'High', False, 'Yes'],
    ['Sunny', 'Mild', 'High', False, 'Yes'],
    ['Sunny', 'Cool', 'Normal', False, 'Yes'],
    ['Sunny', 'Cool', 'Normal', True, 'No'],
    ['Overcast', 'Cool', 'Normal', True, 'Yes'],
    ['Rainy', 'Mild', 'High', False, 'No'],
    ['Rainy', 'Cool', 'Normal', False, 'Yes'],
    ['Sunny', 'Mild', 'Normal', False, 'Yes'],
    ['Rainy', 'Mild', 'Normal', True, 'Yes'],
    ['Overcast', 'Mild', 'High', True, 'Yes'],
    ['Overcast', 'Hot', 'Normal', False, 'Yes'],
    ['Sunny', 'Mild', 'High', True, 'No']
]

LABELS, PREDICTORS = prepare(DATA)
PREDICTIONS = oneR(PREDICTORS)

FREQUENCY_TABLES = [FrequencyTable(*prediction) for prediction in PREDICTIONS.items()]
CONFUSION_MATRICES = [ConfusionMatrix.from_frequency_table(frequency_table) for frequency_table in FREQUENCY_TABLES]
for cf in CONFUSION_MATRICES:
    pprint(cf.summary)
# OUTLOOK_CM = ConfusionMatrix(FREQUENCY_TABLE.name, FREQUENCY_TABLE.lables, FREQUENCY_TABLE.frequncy_table)
# OUTLOOK_CM = ConfusionMatrix.from_frequency_table(FREQUENCY_TABLE)


# print('oneR generated predictors:')
# pprint(PREDICTIONS)
# print('\nfrequnecy table')
# print(FREQUENCY_TABLE.labels)
# for table in FREQUENCY_TABLE.frequncy_table:
#     pprint(table)

# pprint(OUTLOOK_CM.summary)
# # for cm in CONFUSION_MATRICES:
# #     print('Confusion matrix:')
# #     pprint(cm.summary)
# #     print()