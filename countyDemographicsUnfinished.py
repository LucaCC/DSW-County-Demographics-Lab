import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(high_income_counties(counties))
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(lowest_median_income(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def high_income_counties(counties):
    """Return a LIST of the counties with a median household income over $90,000."""
    high_med_inc = []
    for data in counties:
        if data["Income"]["Median Household Income"] > 90000:
            high_med_inc.append(data["County"])
    return high_med_inc


def lowest_median_income(counties):
    """Return a name of a county with the lowest median household income"""
    lowest_name = counties[0]["County"]
    lowest_income = counties[0]["Income"]["Median Household Income"]
    for data in counties:
        if(data["Income"]["Median Household Income"] < lowest_income):
            lowest_name = data["County"]
            lowest_income = data["Income"]["Median Household Income"]
    return lowest_name


def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    #Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True
    first_name = counties[0]["County"]
    for data in counties:
        if data["County"] < first_name:
            first_name = data["County"]
    return first_name

def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    pct_most_under_18 = counties[0]["Age"]["Percent Under 18 Years"]
    for data in counties:
        if data["Age"]["Percent Under 18 Years"] > pct_most_under_18:
            pct_most_under_18 = data["Age"]["Percent Under 18 Years"]
    return pct_most_under_18


def county_most_under_18(counties):
    """Return the name a county with the highest percent of under 18 year olds."""
    pct_most_under_18 = counties[0]["Age"]["Percent Under 18 Years"]
    pct_most_under_name = counties[0]["County"]
    for data in counties:
        if data["Age"]["Percent Under 18 Years"] > pct_most_under_18:
            pct_most_under_18 = data["Age"]["Percent Under 18 Years"]
            pct_most_under_name = data["County"]
    return pct_most_under_name

def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #1. Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    state = {}

    #2. Find the state in the dictionary with the most counties
    state_with_most_counties = ""
    for data in counties:
        if data["State"] in state:
            state[data["State"]] += 1
        else:
            state[data["State"]] = 1
    state_with_most_counties  = data["State"]

    #3. Return the state with the most counties
    for data in state:
        if state[data] > state[state_with_most_counties]:
            state_with_most_counties = data
    return state_with_most_counties


def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    state = {}
    state_with_best_education = ""
    for data in counties:
        if data["State"] in state:
            state[data["State"]]["Bach"] += data["Education"]["Bachelor's Degree or Higher"]
            state[data["State"]]["High"] += data["Education"]["High School or Higher"]
            state[data["State"]]["Count"] += 1
        else:
            state[data["State"]] = {}
            state[data["State"]]["Bach"] = data["Education"]["Bachelor's Degree or Higher"]
            state[data["State"]]["High"] = data["Education"]["High School or Higher"]
            state[data["State"]]["Count"] = 1
        state_with_best_education = data["State"]

    for data in state:
        state[data]["Bach"] = (state[data]["Bach"]/state[data]["Count"])*2 # Weighted because higher degree
        state[data]["High"] = (state[data]["High"]/state[data]["Count"])
        state[data]["Edu"] = state[data]["Bach"] + state[data]["High"]

    for data in state:
        if state[data]["Edu"] > state[state_with_best_education]["Edu"]:
            state_with_best_education = data

    return state_with_best_education



if __name__ == '__main__':
    main()
