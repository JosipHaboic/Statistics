class FrequencyTable:
    ''' Frequency tables tell you how often something occurs in a set of data. '''
    def __init__(self, data):
        self.data = data
        self.labels, self.ft = FrequencyTable.frequency_table(self.data)

    @property
    def summary(self):
        return self.ft
    
    
    @staticmethod
    def frequency_table(dataset):
        ft = {}
        labels = None
        for k, v in dataset.items():
            ft[k] = []
            predictor_contribution = [0,0]
        
            for j in v.values():
                if not labels:
                    labels = list(j.keys())
                predictor_values = list(j.values())
                if predictor_values[0] >= predictor_values[1]:
                    predictor_contribution[0] += 1
                else:
                    predictor_contribution[1] += 1

                ft[k].append(predictor_values)
        
        return labels, ft