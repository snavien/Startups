from pyspark.mllib.classification import SVMWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkConf, SparkContext
from random import randint
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

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
    MSE = labelsAndPreds.map(lambda(v,p): (v-p)**2).reduce(lambda x, y: x + y)/labelsAndPreds.count()
    print("Training Error = " + str(trainErr))
    print("MSE = " + str(MSE))

    labelsAndPreds = testingData.map(lambda p: (p.label, model.predict(p.features)))
    testErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(testingData.count())
    MSE = labelsAndPreds.map(lambda(v,p): (v-p)**2).reduce(lambda x, y: x + y)/labelsAndPreds.count()
    print("Testing Error = " + str(testErr))
    print("MSE = " + str(MSE))



    info = labelsAndPreds.collect()
    actual = [i[0] for i in info]
    predictions = [i[1] for i in info]

    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)

    plt.title('Receiver Operating Characteristic')
    plt.plot(false_positive_rate, true_positive_rate, 'b',
    label='AUC = %0.2f'% roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([-0.1,1.2])
    plt.ylim([-0.1,1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()


for iter in [10000]:
    run_iterations(parsedData, iter, randint(1, 9999))

