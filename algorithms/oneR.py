'''
File: oneR.py
Project: algorithms
File Created: Saturday, 23rd December 2017 7:27:15 pm
Author: Josip Haboic (josiphaboic@gmail.com)
-----
Last Modified: Saturday, 23rd December 2017 7:46:15 pm
Modified By: Josip Haboic (josiphaboic@gmail.com>)
'''


def prepare(data):
    labels = data[0]
    del data[0]

    predictors = {}

    for index, label in enumerate(labels[:-1]):
        predictors[label] = list(zip([row[index] for row in data], [row[-1] for row in data]))

    return labels, predictors


def oneR(predictors):
    counted_predictors = {}

    for predictor in predictors.items():
        counted_predictors[predictor[0]] = {}
        for pair in predictor[1]:
            if pair[0] not in counted_predictors[predictor[0]].keys():
                counted_predictors[predictor[0]][pair[0]] = {}
            if pair[1] not in counted_predictors[predictor[0]][pair[0]].keys():
                counted_predictors[predictor[0]][pair[0]][pair[1]] = 1
            else:
                counted_predictors[predictor[0]][pair[0]][pair[1]] += 1
    return counted_predictors