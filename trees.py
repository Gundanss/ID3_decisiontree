from math import log
import operator

    
def chooseBestFeatureToSplit(dataSet):
    featuresCount = len(dataSet[0]) - 1      #used the last column to be the labels
    entropy = calcShanEnt(dataSet)
    bestInfoGain = 0.0
    chooesFeature = -1
    # print(featuresCount)
    for i in range(featuresCount):
        featList = [instant[i] for instant in dataSet]  #contain lots of data
        # print(featList)
        unique = set(featList)
        newEnt = 0
        for value in unique:
            subDataSet = splitData(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEnt += prob * calcShanEnt(subDataSet)
        informationGain = entropy - newEnt     # formula
        if (informationGain > bestInfoGain):
            bestInfoGain = informationGain         # choose the bigger one
            chooesFeature = i
    return chooesFeature

def majorityCnt(classList):
    classNum={}
    for i in classList:
        if i not in classNum.keys(): classNum[i] = 0
        classNum[i] += 1
    sortedClassNum = sorted(classNum.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassNum[0][0]

def createTree(dataSet,labels):

    classList = [instant[-1] for instant in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]  #when all classes are equal, stop split

    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    chooesFeature = chooseBestFeatureToSplit(dataSet)
    bestLabel = labels[chooesFeature]
    tree = {bestLabel:{}}

    del(labels[chooesFeature])
    featValues = [instant[chooesFeature] for instant in dataSet]
    unique = set(featValues)
    for value in unique:
        subLabels = labels[:]       #copy all labels
        tree[bestLabel][value] = createTree(splitData(dataSet, chooesFeature, value), subLabels)
    return tree


def calcShanEnt(dataSet):
    length = len(dataSet)
    label = {}
    for featVec in dataSet:  # the the number of unique elements and their occurance
        current = featVec[-1]
        if current not in label.keys():
            label[current] = 0
        label[current] += 1
    shanEnt = 0.0
    for key in label:
        prob = float(label[key]) / length
        shanEnt -= prob * log(prob, 2)  # log base 2
    return shanEnt


def splitData(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            calcFeatVec = featVec[:axis]  # chop out axis used for splitting
            calcFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(calcFeatVec)
    return retDataSet

