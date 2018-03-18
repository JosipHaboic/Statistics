from pymymath.statistics.data_container import DataTable
# from pymymath.statistics.frequency_table import FrequencyTable
from pprint import pprint

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

DT = DataTable(DATA[1:], DATA[0])

for column in DT.columns_with_labels:
    pprint(column)
    pprint(column[1].summary)
    print()

for ft in DT.frequency_table:
    print(ft)