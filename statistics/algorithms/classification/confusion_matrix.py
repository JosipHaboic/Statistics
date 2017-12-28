'''
File: confusion_matrix.py
Project: classification
File Created: Sunday, 24th December 2017 7:30:48 pm
Author: Josip Haboic (josiphaboic@gmail.com)
-----
Last Modified: Sunday, 24th December 2017 7:30:55 pm
Modified By: Josip Haboic (josiphaboic@gmail.com>)
'''

class ConfusionMatrix:

    def __init__(self, table_data, labels):
        self.table_name = table_data[0]
        self._table = table_data[1:][0]
        self.labels = labels

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
            'negative_predictive_value' : self.negative_predictive_value,
        }
        

