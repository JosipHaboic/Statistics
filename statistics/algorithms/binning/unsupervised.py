from ... qualitative_population import QuantitativePopulation
from ... quantitative_sample import QuantitativeSample

class UnsupervisedBinning:

    @staticmethod
    def equal_width_binning(dataset: list, k: int):
        from math import ceil
        ''' The algorithm divides the data into k intervals of equal size. '''
        N = len(dataset)
        BIN_WIDTH = ceil(N / k)
        NUMBER_OF_BINS = ceil(N / BIN_WIDTH)

        current_bin = 0

        while current_bin < NUMBER_OF_BINS:
            slice_start = current_bin * BIN_WIDTH 
            slice_end = (current_bin + 1) * BIN_WIDTH

            yield QuantitativeSample(
                dataset[slice_start:slice_end]
                )

            current_bin += 1