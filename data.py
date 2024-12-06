'''example:

data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO')'''


class CountyDemographics:
    # Initialize a new CountyDemographics object.
    # input: the county's age demographics data as a dictionary
    # input: the county's name as a string
    # input: the county's education demographics data as a dictionary
    # input: the county's ethnicities demographics data as a dictionary
    # input: the county's income demographics data as a dictionary
    # input: the county's population demographics data as a dictionary
    # input: the county's state as a string
    def __init__(self,
                  age: dict[str,float],
                  county: str,
                  education: dict[str,float],
                  ethnicities: dict[str,float],
                  income: dict[str,float],
                  population: dict[str,float],
                  state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state


    # Provide a developer-friendly string representation of the object.
    # input: CountyDemographics for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return 'CountyDemographics({}, {}, {}, {}, {}, {}, {})'.format(
                self.age,
                self.county,
                self.education,
                self.ethnicities,
                self.income,
                self.population,
                self.state
            )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__