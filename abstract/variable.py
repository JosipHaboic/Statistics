'''
This module exists only for informational purposes.
'''

class Variable:
    ''' The measurements to be made are referred to as variables.'''
    pass

class  QuantitativeVariable(Variable):
    ''' Classified as quantitative (numeric). '''
    pass

class QualitativeVariable(Variable):
    ''' Classified as qualitative (categorical)
        Categorical variables also are commonly described in one of two ways: 
        nominal and ordinal. 
        Nominal variables have distinct levels that have no inherent ordering. 
        Hair color and sex are examples of variables that would be described as nominal. 
        On the other hand, ordinal variables have levels that do follow a distinct ordering.
        Examples in the medical field typically relate to degrees of change in patients 
        after some treatment (such as: vast improvement, moderate improvement,
        no change, moderate degradation, vast degradation/death).
    '''
    pass

class Continuous(Variable):
    ''' Continuous variables are values that can fall 
        anywhere corresponding to points on a line segment. Some
        examples are weight and diastolic blood pressure. '''
    pass

class Discrete(Variable):
    ''' Discrete variables are variables that can take on
        only a finite (or countably infinite) number of outcomes. Number of previous myocardial 
        infarctions and parity are examples of discrete variables.
        It should be noted that many continuous variables are reported as if 
        they were discrete, and many discrete variables are analyzed as if they were continuous.'''
    pass