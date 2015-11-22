import csv
import Helpers
import numpy as np
from random import shuffle

def main():
    # initialize parallel arrays
    name = []
    market = []
    funding_amount = []
    status =[]
    country =[]
    bay_area = []
    funding_rounds = []
    founded_at = []
    first_funding_at =[]
    last_funding_at =[]

    # read and manipulate data
    with open('FinalData.csv', newline='', encoding='utf8') as file:
        reader = csv.reader(file, delimiter=',')
        first = True
        for row in reader:
            if first == True:
                first = False
                continue
            name.append(row[Helpers.NAME_IDX])
            market.append(hash(row[Helpers.MARKET_IDX]))
            funding_amount.append(int(row[Helpers.FUNDING_IDX]))
            status.append(Helpers.processStatus(row[Helpers.STATUS_IDX]))
            country.append(row[Helpers.COUNTRY_IDX])
            bay_area.append(Helpers.processRegion(row[Helpers.BAYAREA_IDX]))
            funding_rounds.append(int(row[Helpers.ROUNDS_IDX]))
            founded_at.append(int(row[Helpers.FOUNDED_IDX]))
            first_funding_at.append(int(row[Helpers.FIRST_IDX]))
            last_funding_at.append(int(row[Helpers.LAST_IDX]))

    for idx,countryStr in enumerate(country):
        country[idx] = Helpers.processCountry(countryStr)

    # select indexes for testing and training sets
    dividingIdxs = list(range(0, len(name)))
    shuffle(dividingIdxs)

    # create training set
    Y = []
    X = []
    dataIdx = 0
    while dataIdx < len(name) * .75:
        elementIdx = dividingIdxs[dataIdx]
        element = []
        element.append(market[elementIdx])
        element.append(funding_amount[elementIdx])
        element.append(country[elementIdx])
        element.append(bay_area[elementIdx])
        element.append(funding_rounds[elementIdx])
        element.append(founded_at[elementIdx])
        element.append(first_funding_at[elementIdx])
        element.append(last_funding_at[elementIdx])
        X.append(element)
        Y.append(status[elementIdx])
        dataIdx = dataIdx + 1

    X = np.array(X)
    Y = np.array(Y)

    # create training set
    testX = []
    testY = []
    while dataIdx < len(name):
        elementIdx = dividingIdxs[dataIdx]
        element = []
        element.append(market[elementIdx])
        element.append(funding_amount[elementIdx])
        element.append(country[elementIdx])
        element.append(bay_area[elementIdx])
        element.append(funding_rounds[elementIdx])
        element.append(founded_at[elementIdx])
        element.append(first_funding_at[elementIdx])
        element.append(last_funding_at[elementIdx])
        testX.append(element)
        testY.append(status[elementIdx])
        dataIdx = dataIdx + 1

main()