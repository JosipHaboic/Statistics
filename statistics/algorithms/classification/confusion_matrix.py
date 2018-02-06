'''
File: confusion_matrix.py
Project: classification
File Created: Sunday, 24th December 2017 7:30:48 pm
Author: Josip Haboic (josiphaboic@gmail.com)
-----
Last Modified: Tue Feb 06 2018
Modified By: Josip Haboic
'''

from .frequency_table import FrequencyTable
class ConfusionMatrix:pass

class ConfusionMatrix:
    ''' In the field of machine learning and specifically the problem of statistical classification,
        a confusion matrix, also known as an error matrix, is a specific table layout that allows
        visualization of the performance of an algorithm, typically a supervised learning one 
        (in unsupervised learning it is usually called a matching matrix). 
        Each row of the matrix represents the instances in a predicted class while each column represents
        the instances in an actual class (or vice versa).The name stems from the fact that it makes
        it easy to see if the system is confusing two classes (i.e. commonly mislabelling one as another).
        It is a special kind of contingency table, with two dimensions ("actual" and "predicted"),
        and identical sets of "classes" in both dimensions (each combination of dimension and class
        is a variable in the contingency table). '''
    def __init__(self, name, labels, table):
        self.name = name
        self.labels = labels
        self._table = table

    @property
    def table(self):
        return self._table

    @property
    def a(self):return self._table[0][0]
    @property
    def b(self):return self._table[0][1]
    @property
    def c(self):return self._table[1][0]
    @property
    def d(self):return self._table[1][1]

    @property
    def sesitivity(self):
        return self.a / (self.a + self.c)

    @property
    def specificity(self):
        return self.d / (self.b + self.d)

    @property
    def accuracy(self):
        return (self.a + self.d) / (self.a + self.b + self.c + self.d)

    @property
    def positive_predictive_value(self):
        return self.a / (self.a + self.b)

    @property
    def negative_predictive_value(self):
        return self.d / (self.c + self.d)

    @property
    def confusion_matrix(self):
        result = {}
        for label in self.labels:
            result[label] = 0
        for row in self.table:
            if row[0] >= row[1]:
                result[self.labels[0]] += row[0]
            else:
                result[self.labels[1]] += row[1]
        return result

    @property
    def summary(self):
        return {
            'table' :  {
            'a' : self.a,
            'b' : self.b,
            'c' : self.c,
            'd' : self.d
            },
            'sensitivity' : self.sesitivity,
            'specificity' : self.specificity,
            'accuracy' : self.accuracy,
            'positive_predictive_value' : self.positive_predictive_value,
            'negative_predictive_value' : self.negative_predictive_value
        }

    @staticmethod
    def from_frequency_table(frequncy_table: FrequencyTable) -> ConfusionMatrix:
        return ConfusionMatrix(frequncy_table.name, frequncy_table.labels, frequncy_table.frequncy_table)