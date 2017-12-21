import os
from knn import KNN

os.chdir(os.path.dirname(os.path.abspath(__file__)))

TRAINING_DATA = [
    [255, 255, 255, 'white'],
    [0, 0, 0, 'black'],
    [128, 128, 128, 'gray'],
    [255, 0, 0, 'red'],
    [0, 255, 0, 'green'],
    [0, 0, 255, 'blue']
]
TEST_DATA = [
    [0,255,0],
    [255,0,0],
    [0,0,255],
    [255,0,255],
    [100,0,50],
    [100,100,100],
    [50,50,50],
    [200,200,200],
    [10,20,30],
    [100,10,200],
    [32,0,255],
    [128,255,64]
]

DATA = KNN.convert_to_float(TRAINING_DATA, 'training')
TEST_DATA = KNN.convert_to_float(TEST_DATA, 'test')


K = 1

KNN_DATA = KNN.knn(DATA, TEST_DATA, K)
for i in KNN_DATA:
    print(i)
