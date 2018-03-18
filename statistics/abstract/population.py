from abc import ABCMeta ,abstractproperty

class Population(list):

    __metaclass__  = ABCMeta

    def __init__(self, data=[], name=None):
        self.name = name
        list.__init__(self, data)


class ExistingPopulation(Population):
    '''Are well–defined sets of data containing
       elements that could be identified explicitly.
       Examples:
       1. CD4 counts of every American diagnosed with AIDS as of January 1, 1996.
       2. Amount of active drug in all 20–mg Prozac capsules manufactured in June 1996.
       3. Presence or absence of prior myocardial infarction in all American males between 45 and 64
          years of age.'''
    
    __metaclass__ = ABCMeta

    def __init__(self, data, name=None):
        Population.__init__(self, data, name)


class ConceptualPopulation(Population):
    '''Conceptual populations are non–existing, yet visualized, or imaginable, sets of measurements. This
       could be thought of characteristics of all people with a disease, now or in the near future, for
       instance. It could also be thought of as the outcomes if some treatment were given to a large group
       of subjects. In this last setting, we do not give the treatment to all subjects, but we are interested
       in the outcomes if it had been given to all of them.
       Examples:
       1. Bioavailabilities of a drug’s oral dose (relative to i. v. dose) in all healthy subjects under
          identical conditions.
       2. Presence or absence of myocardial infarction in all current and future high blood pressure
          patients who receive short–acting calcium channel blockers.
       3. Positive or negative result of all pregnant women who would ever use a particular brand of
          home pregnancy test.'''
    
    __metaclass__ = ABCMeta

    def __init__(self, data, name=None):
        Population.__init__(self, data, name)


class AbstractQuantitativePopulation(Population):

    __metaclass__ = ABCMeta

    @abstractproperty
    def n(self):pass

    @abstractproperty
    def mean(self):pass

    @abstractproperty
    def geometric_mean(self):pass

    @abstractproperty
    def harmonic_mean(self):pass

    @abstractproperty
    def median(self):pass

    @abstractproperty
    def midrange(self):pass

    @abstractproperty
    def mean_test(self):pass

    @abstractproperty
    def mean_deviation(self):pass

    @abstractproperty
    def variance(self):pass

    @abstractproperty
    def standard_deviation(self):pass

    @abstractproperty
    def range(self):pass

    @abstractproperty
    def mode(self):pass

    @abstractproperty
    def skewness(self):pass

    @abstractproperty
    def kurtosis(self):pass

    @abstractproperty
    def coefficient_of_variation(self):pass

    @abstractproperty
    def min(self):pass

    @abstractproperty
    def max(self):pass

    @abstractproperty
    def sum(self):pass

    @abstractproperty
    def squared_sum(self):pass

    @abstractproperty
    def sum_of_squares(self):pass

    @abstractproperty
    def standard_error(self):pass

    @abstractproperty
    def negative_values(self):pass

    @abstractproperty
    def positive_values(self):pass

    @abstractproperty
    def unique(self):pass

    @abstractproperty
    def summary(self):pass



class AbstractQualitativePopulation(Population):

    __metaclass__ = ABCMeta

    @abstractproperty
    def frequencies(self):pass

    @abstractproperty
    def relative_frequencies(self):pass

    @abstractproperty
    def quantitatized_frequencies(self):pass

    @abstractproperty
    def summary(self):pass

