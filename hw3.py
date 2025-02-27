import data


def population_total(lst:list[data.CountyDemographics]) -> int:#this function return total population
    pop=0
    for a in lst:
        pop+=a.population['2014 Population']
    return pop

def filter_by_state(lst:list[data.CountyDemographics], s:str)->list[data.CountyDemographics]:#this function gives filters counties from particular state
    r_lst=[]
    for a in lst:
        if s==a.state:
            r_lst.append(a)
    return r_lst

def population_by_education(lst:list[data.CountyDemographics], s:str) -> float:#This function gives total population by education level
    tot=0
    for a in lst:
        try:
            percentage=a.education[s]
        except KeyError:
            percentage=0
        tot+=percentage*a.population['2014 Population']/100
    return tot

def population_by_ethnicity(lst:list[data.CountyDemographics], s:str) -> float:# This function gives population by ethnicity
    tot=0
    for a in lst:
        try:
            percentage=a.ethnicities[s]
        except KeyError:
            percentage=0
        tot+=percentage*a.population['2014 Population']/100
    return tot

def population_below_poverty_level(lst:list[data.CountyDemographics]) -> float:#this function gives population below poverty level
    tot=0
    for a in lst:
        percentage=a.income['Persons Below Poverty Level']
        tot+=percentage*a.population['2014 Population']/100
    return tot

#task 4
def percent_by_education(lst:list[data.CountyDemographics], s:str) -> float:# This functions give percentage by attributes such as education level, ethnicity and below poverty level
    total_population=population_total(lst)
    pop_edu=population_by_education(lst,s)
    return 100*pop_edu/total_population

def percent_by_ethnicity(lst:list[data.CountyDemographics], s:str) -> float:
    total_population=population_total(lst)
    pop_eth=population_by_ethnicity(lst,s)
    return 100*pop_eth/total_population

def percent_below_poverty_level(lst:list[data.CountyDemographics]) -> float:
    total_population=population_total(lst)
    pbp=population_below_poverty_level(lst)
    return 100*pbp/total_population

def education_greater_than(lst:list[data.CountyDemographics], s:str, threshold:float) -> list[data.CountyDemographics]: #These functions return list of counties greater and lesser than certain attributes.
    r_lst=[]
    for a in lst:
        if a.education[s]>threshold:
            r_lst.append(a)
    return r_lst

def education_lesser_than(lst:list[data.CountyDemographics], s:str, threshold:float) -> list[data.CountyDemographics]:
    r_lst=[]
    for a in lst:
        if a.education[s]<threshold:
            r_lst.append(a)
    return r_lst

def ethnicity_greater_than(lst:list[data.CountyDemographics], s:str, threshold:float) -> list[data.CountyDemographics]:
    r_lst=[]
    for a in lst:
        if a.ethnicities[s]>threshold:
            r_lst.append(a)
    return r_lst

def ethnicity_lesser_than(lst:list[data.CountyDemographics], s:str, threshold:float) -> list[data.CountyDemographics]:
    r_lst=[]
    for a in lst:
        if a.ethnicities[s]<threshold:
            r_lst.append(a)
    return r_lst

def below_poverty_level_greater_than(lst:list[data.CountyDemographics], threshold:float) -> list[data.CountyDemographics]:
    r_lst=[]
    for a in lst:
        if a.income['Persons Below Poverty Level']>threshold:
            r_lst.append(a)
    return r_lst

def below_poverty_level_lesser_than(lst:list[data.CountyDemographics], threshold:float) -> list[data.CountyDemographics]:
    r_lst=[]
    for a in lst:
        if a.income['Persons Below Poverty Level']<threshold:
            r_lst.append(a)
    return r_lst