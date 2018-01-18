from ... qualitative_population import QuantitativePopulation
from ... quantitative_sample import QuantitativeSample

class UnsupervisedBinning:

    @staticmethod
    def equal_width_binning(dataset: QuantitativePopulation, k: int):
        ''' The algorithm divides the data into k intervals of equal size. '''
        W = (dataset.max - dataset.min) / k
        MIN = dataset.min
        NUMBER_OF_INTERVALS = int(dataset.n / W)

        current_interval = 0

        while current_interval < NUMBER_OF_INTERVALS:
            yield QuantitativeSample(
                dataset[int(MIN + current_interval * W):int(MIN + (current_interval + 1) * W)]
                )
            current_interval += 1