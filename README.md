# gdp-analysis
def get_highest_gdp(data, year):
        maximum = float(data[0][year])
        for row in data:
            value = float(data["2020"])
            if value > maximum:
                maximum = value
        return maximum
        

    def get_lowest_gdp(data, year):
        minimum = float(data[0][year])
        for row in data:
            value = float(row["2020"])
            if value < minimum:
                minimum = value
        return minimum