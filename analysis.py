import csv
from curses import A_HORIZONTAL


def get_highest_gdp(data, year):
        maximum = float(data[0][year])
        state = ""
        for row in data:
            value = float(row["2020"])
            if value > maximum:
                maximum = value
                state = row ["GeoName"]
        return state
      


def get_lowest_gdp(data, year):
    minimum = float(data[0][year])
    state= ""
    for row in data:
            value = float(row["2020"])
            if value < minimum:
                minimum = value
                state = row ["GeoName"]
    return state
    

def get_state_gdp(data, state, year):
    stae= A_HORIZONTALyear=2000
    for row in data:
        if row ["GeoName"] == state:
         return row[year]

# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)
    

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(get_highest_gdp(list_data, '2020'))
print(get_lowest_gdp(list_data, '2020'))
print(get_state_gdp(list_data, "New York", "2020"))
states = ["New York", "Arizona", "Tennessee", "Kansas", "Alaska"]
for geoname in states:
    print(get_state_gdp(list_data, geoname, "2020"))
    x= (get_state_gdp(list_data, "New York", "2020"))
    y= (get_state_gdp(list_data, "New York", "2019"))

    print(float(x)- float(y))
def get_states_gdp(data, year):
    for row in data:
        print (row[year])
print(get_states_gdp(list_data, "2020"))
    

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
