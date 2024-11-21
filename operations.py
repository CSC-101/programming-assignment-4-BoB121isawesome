from data import CountyDemographics


def population_total(counties:list[CountyDemographics])->int:
    population = 0
    for county in counties:
        population += county.population["2014 Population"]
    return population

def percent(counties:list[CountyDemographics], current_field:str, subfield:str) -> float:
    population = 0
    total_pop=0
    for county in counties:
        field_arg = getattr(county, current_field)
        if field_arg and subfield in field_arg:
            population = population + county.population["2014 Population"] * (field_arg[subfield]/100)
            total_pop += county.population["2014 Population"]
    result= (population/total_pop)*100
    return result

def filter_gt(counties:list[CountyDemographics],current_field:str, subfield:str, threshold:float)->list[CountyDemographics]:
    county_list = []
    for county in counties:
        field_arg = getattr(county, current_field)
        if field_arg and subfield in field_arg:
            threshold = float(threshold)
            if field_arg[subfield] > threshold:
                county_list.append(county)
    return county_list

def filter_lt(counties:list[CountyDemographics],current_field:str, subfield:str, threshold:float)->list[CountyDemographics]:
    county_list = []
    for county in counties:
        field_arg = getattr(county, current_field)
        if field_arg and subfield in field_arg:
            threshold=float(threshold)
            if field_arg[subfield] < threshold:
                county_list.append(county)
    return county_list

def population(counties:list[CountyDemographics], current_field:str, subfield:str):
    population = 0
    for county in counties:
        field_arg = getattr(county, current_field)
        if field_arg and subfield in field_arg:
            population = population + county.population["2014 Population"] * (field_arg[subfield] / 100)
    return population

def filter_state(demographics:list[CountyDemographics], state:str)->list[CountyDemographics]:
    county_list=[]
    for county in demographics:
        if county.state == state:
            county_list.append(county)
    return county_list

def display(counties:list[CountyDemographics]):
    formatted_output = ""
    for county in counties:
        formatted_output += f"{county.county}, {county.state}\n"
        formatted_output += f"\tPopulation: {county.population.get('2014 Population', 'N/A')}\n"
        formatted_output += "\tAge:\n"
        formatted_output += f"\t\t< 5: {county.age.get('Percent Under 5 Years', 'N/A')}%\n"
        formatted_output += f"\t\t< 18: {county.age.get('Percent Under 18 Years', 'N/A')}%\n"
        formatted_output += f"\t\t> 65: {county.age.get('Percent 65 and Older', 'N/A')}%\n"
        formatted_output += "\tEducation\n"
        formatted_output += f"\t\t>= High School: {county.education.get('High School or Higher', 'N/A')}%\n"
        formatted_output += f"\t\t>= Bachelor's: {county.education.get("Bachelor's Degree or Higher", 'N/A')}%\n"
        formatted_output += "\tEthnicity Percentages\n"

        for ethnicity, percent in county.ethnicities.items():
            formatted_output += f"\t\t{ethnicity}: {percent}%\n"

        # Income Section
        formatted_output += "\tIncome\n"
        formatted_output += f"\t\tMedian Household: {county.income.get('Median Household Income', 'N/A')}\n"
        formatted_output += f"\t\tPer Capita: {county.income.get('Per Capita Income', 'N/A')}\n"
        formatted_output += f"\t\tBelow Poverty Level: {county.income.get('Persons Below Poverty Level', 'N/A')}%\n\n"
    return formatted_output

operations_dict = {
    'display':display,
    'filter-state':filter_state,
    'filter-gt':filter_gt,
    'filter-lt':filter_lt,
    'population-total': population_total,
    'population':population,
    'percent':percent
}
