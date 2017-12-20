from operator import itemgetter
from csv import reader
from sys import exit


__all__ = ['KNN']

class KNN:

    @staticmethod
    def normalize(data):
        magnitude = sum(list(map(lambda x: x**2))) ** 0.5
        if magnitude == 0:
            return data
        for index, value in enumerate(data):
            data[index] = value / magnitude

    @staticmethod
    def convert_to_float(dataset: list, mode: str) -> list:
        new_set = []
        try:
            if mode == 'training':
                for data in dataset:
                    new_set.append([ float(x) for x in data[:len(data) - 1]] + [data[len(data) -1]])
            elif mode == 'test':
                for data in dataset:
                    new_set.append([ float(x) for x in data ])
            else:
                print('Invalid mode, program will exit')
                exit()
            
            return new_set

        except ValueError as value_error:
            print(value_error)
            exit()

    @staticmethod
    def get_classes(training_set: list) -> list:
        extracted = tuple(c[-1] for c in training_set)
        return extracted

    @staticmethod
    def find_neighbours(distances: list, k: int) -> list:
        return distances[0:k]

    @staticmethod
    def find_response(neighbours: list, classes: list) -> int:
        votes = [0] * len(classes)

        for instance in neighbours:
            for ctr, c in enumerate(classes):
                if instance[-2] == c:
                    votes[ctr] += 1
        return max(enumerate(votes), key=itemgetter(1))

    @staticmethod
    def knn(training_set: list, test_set: list, k: int) -> list:
        distances = []
        d = 0
        limit = len(training_set) - 1

        classes = KNN.get_classes(training_set)
        predictions = []

        try:
            for test_instance in test_set:
                for row in training_set:
                    for x, y in zip(row[:limit], test_instance):
                        d += (x - y) * (x - y)
                    distances.append(row + [d ** 0.5])
                    d = 0
                distances.sort(key=itemgetter(len(distances[0]) - 1))

                neighbours = KNN.find_neighbours(distances, k)

                index, value = KNN.find_response(neighbours, classes)
                
                predictions.append({
                    'test instance' : test_instance,
                    'classes' : classes[index],
                    'votes' : {'value' : value, 'k' : k}
                })
                distances.clear()
        except Exception as e:
            print('Error occured: {}'.format(e))

        return predictions

    @staticmethod
    def load_csv_dataset(filename) -> list:
        try:
            with open(filename, newline='') as data:
                return list(reader(data,delimiter=','))
        except FileNotFoundError as e:
            print(e)