import os
from knn import KNN

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CSV_TRAINING_DATA = KNN.load_csv_dataset('./data/example_data.csv')
CSV_TEST_DATA = KNN.load_csv_dataset('./data/example_test_data.csv')

DATA = KNN.convert_to_float(CSV_TRAINING_DATA, 'training')
TEST_DATA = KNN.convert_to_float(CSV_TEST_DATA, 'test')


K = 2

KNN_DATA = KNN.knn(DATA, TEST_DATA, K)
for i in KNN_DATA:
    print(i)