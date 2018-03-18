from pymymath.statistics.algorithms.classification.knn import KNN


# lets see how well KNN will predict RGB values, with k=1, k=4

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

def test_KNN(data, test_data, k=1):
    predictions = KNN.knn(data, test_data, k)
    for i in predictions:
        print(i)

test_KNN(DATA, TEST_DATA, k=1)
print()
test_KNN(DATA, TEST_DATA, k=4)
