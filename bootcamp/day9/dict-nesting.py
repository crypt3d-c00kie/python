# exploring dict+lists
travel_log = []

def add_country(travel_log,name, countVisit, listCities):
    newCountry = {}
    newCountry["country"] = name
    newCountry["visits"] = countVisit
    newCountry["cities"] = listCities
    
    travel_log.append(newCountry)


def main():
    '''
    nesting list in dictionary
    travel_log = {
        "Andhra" : ["Hyderabad", "Warangal", "Vizag"],
        "Tamil Nadu" : ["Chennai", "Coimbatore", "Trichy"]
    }   
    #nesting dictionary in a list
    '''
    travel_log = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
    ]

    print('Before')
    print(travel_log, end = "\n")
    print('After')
    add_country(travel_log,"Italy", 3, ["Rome", "Naples", "Amalfi"])
    print(travel_log)

if __name__ == '__main__':
    main()