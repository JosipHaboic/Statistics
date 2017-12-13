class Population(list):
    def __init__(self, data=[]):
        list.__init__(self, data)


class ExistingPopulation(Population):
    '''Are well–defined sets of data containing
       elements that could be identified explicitly.
       Examples:
       1. CD4 counts of every American diagnosed with AIDS as of January 1, 1996.
       2. Amount of active drug in all 20–mg Prozac capsules manufactured in June 1996.
       3. Presence or absence of prior myocardial infarction in all American males between 45 and 64
          years of age.'''
    
    def __init__(self, data):
        Population.__init__(self, data)


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

    def __init__(self, data):
        Population.__init__(self, data)
