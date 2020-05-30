

from math import log
import operator

import treePlotter
import importlib
import time



def BestSplit(dataSet):
    featuresCount = len(dataSet[0])-1
    entropy = calcShanEnt(dataSet)
    bestGainRate = 0
    chooesFeature = -1
    for i in range(featuresCount):
        featList = [rowdata[i] for rowdata in dataSet]
        unique = set(featList)
        newEnt = 0
        for value in unique:
            subData = dataSplit(dataSet, i, value)
            prob = len(subData) / float(len(dataSet))
            newEnt += prob * calcShanEnt(subData)
            # print(newEnt)
        info = entropy - newEnt
        splitonfo = calcShanEnt(subData)
        if splitonfo == 0:
            continue
        newGainRate = info / splitonfo  #calculate the a new GainRate
        if (newGainRate > bestGainRate):
            # print(newGainRate, bestGainRate)
            bestGainRate = newGainRate
            chooesFeature = i

    return chooesFeature



def majorityCnt(classList):
    c_count = {}
    for i in classList:
        if i not in c_count.keys():
            # print(c_count[i])
            c_count[i] = 0
        c_count[i] += 1
    ClassCount = sorted(c_count.items(), key=operator.itemgetter(1), reverse=True)
    return ClassCount[0][0]


# create the tree for user
def createTree(data, labels):
    classList = [rowdata[-1] for rowdata in data]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(data[0]) == 1:
        return majorityCnt(classList)
    bestFeat = BestSplit(data)
    bestLab = labels[bestFeat]
    myTree = {bestLab: {}}
    # print(myTree)

    del (labels[bestFeat])
    featValues = [rowdata[bestFeat] for rowdata in data]
    unique = set(featValues)
    for value in unique:
        subLabels = labels[:]
        myTree[bestLab][value] = createTree(dataSplit(data, bestFeat, value), subLabels)
    return myTree



#entropy
def calcShanEnt(data):
    length = len(data)
    label = {}
    for featVec in data:
        current = featVec[-1]
        if current not in label.keys():
            label[current] = 0
        label[current] += 1
    entropy = 0
    for key in label:
        probability = float(label[key]) / length
        entropy -= probability * log(probability, 2)
    return entropy


def dataSplit(data, i, value):
    dataSplit = []
    for featVec in data:
        if featVec[i] == value:
            # print(featVec[i])

            calcFeatVec = featVec[:i]
            calcFeatVec.extend(featVec[i + 1:])
            dataSplit.append(calcFeatVec)
    return dataSplit

if __name__ == '__main__':

    file = open('modified4.0monthDcTempRhRain.txt')
    data = [inst.strip().split('\t') for inst in file.readlines()]
    # feature = ['location','month','FFMC', 'DC', 'ISI']
    feature = ['month', 'DC', 'temp', 'RH','rain']
    # feature = ['temp', 'RH', 'wind', 'rain']

    t1 = time.clock()
    Tree = createTree(data, feature)
    t2 = time.clock()

    print(Tree)
    print('Execute for ', t2 - t1)

    importlib.reload(treePlotter)
    treePlotter.createPlot(Tree)


