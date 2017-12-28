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
    ''' Split data to labels and dataset.
        Assume that lables are at data[0] '''
    labels = data[0]
    del data[0]

    predictors = {}

    for index, label in enumerate(labels[:-1]):
        predictors[label] = list(zip([row[index] for row in data], [row[-1] for row in data]))

    return labels, predictors


def oneR(predictors):
    ''' OneR, short for "One Rule", is a simple, yet accurate, 
        classification algorithm that generates one rule for each predictor in the data,
        then selects the rule with the smallest total error as its "one rule".
        To create a rule for a predictor, we construct a frequency table for each predictor against the target.'''
    counted_predictors = {}

    for predictor in predictors.items():
        counted_predictors[predictor[0]] = {}
        values_names = []
        for pair in predictor[1]:
            if pair[0] not in counted_predictors[predictor[0]].keys():
                counted_predictors[predictor[0]][pair[0]] = {}
            if pair[1] not in values_names:
                values_names.append(pair[1])
            if pair[1] not in counted_predictors[predictor[0]][pair[0]].keys():
                counted_predictors[predictor[0]][pair[0]][pair[1]] = 1
            else:
                counted_predictors[predictor[0]][pair[0]][pair[1]] += 1

            for value_name in values_names:
                if value_name not in counted_predictors[predictor[0]][pair[0]].keys():
                    counted_predictors[predictor[0]][pair[0]][value_name] = 0
                    
    return counted_predictors