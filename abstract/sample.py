from . population import Population

class Sample(Population):
    '''Samples are observed sets of measurements that are subsets of a corresponding population.
       Samples are used to describe and make inferences concerning the populations from which they arise.
       Statistical methods are based on these samples having been taken at random from the population.
       However, in practice, this is rarely the case. We will always assume that the sample is representative
       of the population of interest.
       Examples:
       1. CD4 counts of 100 AIDS patients on January 1, 1996.
       2. Amount of active drug in 2000 20–mg Prozac capsules manufactured during June 1996.
       3. Prior myocardial infarction status (yes or no) among 150 males aged 45 to 64 years.
       4. Bioavailabilities of an oral dose (relative to i.v. dose) in 24 healthy volunteers.
       5. Presence or absence of myocardial infarction in a fixed period of time for 310 hypertension
          patients receiving calcium channel blockers.
       6. Test results (positive or negative) among 50 pregnant women taking a home pregnancy test.'''

    def __init__(self, data):
        Population.__init__(self, data)


