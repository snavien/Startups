from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkConf, SparkContext
from numpy.random import randint

#sc = SparkContext("local", "SVM App", pyFiles=['dataLibSVM.txt'])
conf = (SparkConf()
        .setMaster("local")
        .setAppName("SVM App")
        .set("spark.executor.memory", "500m"))
sc = SparkContext(conf=conf)
# Load and parse the data
def parsePoint(line):
    values = [float(x) for x in line.split(',')]
    # print(values[0])
    return LabeledPoint(values[0], values[2:])


data = sc.textFile("numData.csv")
parsedData = data.map(parsePoint)


def run_iterations(parsedData, iter, seed):
    trainingData, testingData = parsedData.randomSplit([70, 30], seed)
    print("For " + str(iter) + " iterations:")
    # Build the model
    model = SVMWithSGD.train(trainingData, iterations=100)

    # Evaluating the model on training data
    labelsAndPreds = trainingData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(trainingData.count())
    print("Training Error = " + str(trainErr))

    labelsAndPreds = testingData.map(lambda p: (p.label, model.predict(p.features)))
    testErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(testingData.count())

    print("Testing Error = " + str(testErr))

for iter in [100, 1000, 10000]:
    run_iterations(parsedData, iter, randint(1, 9999))