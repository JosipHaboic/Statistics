from math import ceil
from . statistics.quantitative_sample import QuantitativeSample

def split_month_to_weeks(month_data):
    NUMBER_OF_WEEKS = ceil(len(month_data) / 7)
    current_week = 1
    weeks = []
    while current_week <= NUMBER_OF_WEEKS:
        yield QuantitativeSample(month_data[(current_week - 1) * 7:current_week * 7])
        current_week += 1
        