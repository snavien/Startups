import csv
import Helpers
import numpy as np
import pandas as pd
from random import shuffle
from sklearn.naive_bayes import GaussianNB

def getData():
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

    return X, Y, testX, testY

X, Y, testX, testY = getData()

clf = GaussianNB()
clf.fit(X, Y)

compare = []
predictedOutput = []
total = 0.0;

for i in range(len(testX)):
    #print([testX[1]])
    #input()
    predictedOutput.append(clf.predict([testX[i]]))
    if predictedOutput[i] == testY[i]:
        compare.append(1)
        total = total + 1.0
    else:
        compare.append(0)

dfCompare = pd.DataFrame(compare)
dfPredictedOutput = pd.DataFrame(predictedOutput)

print("Output from Naive Bayes:")
print(dfPredictedOutput)

print('\n')
print("Comparing output to actual data: 0 = wrong prediction, 1 = correct prediction")
print(dfCompare)

print("percentage of accuracy: # correct / total")
print(total / len(testX))