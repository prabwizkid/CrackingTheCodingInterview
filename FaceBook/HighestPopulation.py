# Given a list of people with their birth year and death year,
# Find the year with the highest population
# Only for the years in the given years

# brute Force way
# O(p*y) + O(m) + O(r) => O(py+m+r)
def highestPopulation1(personList):
    yearDict = {}
    for person in personList:
        for year in range(person['birthyear'], person['deathyear']):
            if year in yearDict.keys():
                yearDict[year] += 1
            else:
                yearDict[year] = 1

    maxPopulation = max(yearDict.values())
    years = []
    for k, v in yearDict.items():
        if v == maxPopulation:
            years.append(k)
    return years

# Another way - Check how many are alive each year
# O(p) + O(y.p) + O(m) + O(r) => O(yp+p+m+r)
def highestPopulation2(personList):
    years = []
    for person in personList:
        years.append(person['birthyear'])
        years.append(person['deathyear'])

    leastYear = min(years)
    highestYear = max(years)
    yearDict = {}
    for year in range(leastYear, highestYear + 1):
        for person in personList:
            if year >= person['birthyear'] and year < person['deathyear']:
                if year in yearDict.keys():
                    yearDict[year] += 1
                else:
                    yearDict[year] = 1

    maxPopulation = max(yearDict.values())
    years = []
    for k, v in yearDict.items():
        if v == maxPopulation:
            years.append(k)
    return years

# Number line way
def highestPopulation3(personList):
    birth = []
    death = []
    for person in personList:
        birth.append(person['birthyear'])
        death.append(person['deathyear'])

    yearDict = {}
    for year in birth:
        if year in yearDict.keys():
            yearDict[year] += 1
        else:
            yearDict[year] = 1
        if year in death:
            yearDict[year] -= 1

    maxPopulation = max(yearDict.values())
    years = []
    for k, v in yearDict.items():
        if v == maxPopulation:
            years.append(k)
    return years

# Test data
peopleList = []
peopleList.append({'name': 'paris', 'birthyear': 1967, 'deathyear': 2045})
peopleList.append({'name': 'bob', 'birthyear': 1954, 'deathyear': 2020})
peopleList.append({'name': 'bitter', 'birthyear': 2011, 'deathyear': 2034})
peopleList.append({'name': 'sam', 'birthyear': 2000, 'deathyear': 2067})
peopleList.append({'name': 'asper', 'birthyear': 1999, 'deathyear': 2030})
peopleList.append({'name': 'rand', 'birthyear': 2020, 'deathyear': 2030})
peopleList.append({'name': 'pet', 'birthyear': 1947, 'deathyear': 2009})
peopleList.append({'name': 'kelly', 'birthyear': 1990, 'deathyear': 2045})
peopleList.append({'name': 'ceri', 'birthyear': 1954, 'deathyear': 2020})
peopleList.append({'name': 'hari', 'birthyear': 1984, 'deathyear': 2024})
peopleList.append({'name': 'ram', 'birthyear': 1977, 'deathyear': 2020})

print(highestPopulation1(peopleList))
print(highestPopulation2(peopleList))
print(highestPopulation3(peopleList))

