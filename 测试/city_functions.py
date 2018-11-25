def cityCountryPopulation(city ,country, population=""):
    if population:
        return city + "," + country + "-人口" + population
    else:
        return city + "," + country
