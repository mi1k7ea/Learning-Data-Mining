#!/usr/bin/python
#coding=utf-8
import operator
import math

#定义训练数据集
def createDataSet():

	#用书上图8.2的数据
	dataSet = [
			['youth', 'no', 'no', 'no'],
			['youth', 'yes', 'no', 'yes'],
			['youth', 'yes', 'yes', 'yes'],
			['middle_aged', 'no', 'no', 'no'],
			['middle_aged', 'no', 'yes', 'no'],
			['senior', 'no', 'excellent', 'yes'],
			['senior', 'no', 'fair', 'no']
	]

	labels = ['age', 'student', 'credit_rating']

	return dataSet, labels

#实现熵的计算
def calShannonEnt(dataSet):

	numEntries = len(dataSet)
	labelCounts = {}

	for featVect in dataSet:
		currentLabel = featVect[-1]
		if currentLabel not in labelCounts:
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1

	shannonEnt = 0.0

	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * math.log(prob, 2)

	return  shannonEnt

#分割训练数据集
def splitDataSet(dataSet, axis, value):

	retDataSet = []

	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)

	return retDataSet

#一个确定“最好地”划分数据元组为个体类的分裂准则的过程
def Attribute_selection_method(dataSet):

	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1

	for i in range(numFeatures):

		featList = [example[i] for example in dataSet]
		uniqueValue = set(featList)
		newEntropy = 0.0

		for value in uniqueValue:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / len(dataSet)
			newEntropy += prob * calShannonEnt(subDataSet)

		infoGain = baseEntropy - newEntropy

		if infoGain > bestInfoGain:
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature

#采用majorityvote策略，选择当前训练集中实例数最大的类
def majorityCnt(classList):

	classCount = {}

	for vote in classList:

		if vote not in classCount.keys():
			classCount[vote] = 0

		classCount[vote] += 1

	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

	return sortedClassCount[0][0]

#创建决策树
def Generate_decision_tree(dataSet, labels):
	classList = [example[-1] for example in dataSet]

	# 训练集所有实例属于同一类
	if classList.count(classList[0]) == len(classList):
		return classList[0]

	# 训练集的所有特征使用完毕，当前无特征可用
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)

	bestFeat = Attribute_selection_method(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel: {}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)

	for value in uniqueVals:
		 subLabels = labels[:]
		 myTree[bestFeatLabel][value] = Generate_decision_tree(splitDataSet(dataSet, bestFeat, value), subLabels)

	return myTree

def main():
	print '	 ____            _     _           _____              '
	print '	|  _ \  ___  ___(_)___(_) ___  _ _|_   _| __ ___  ___ '
	print '''	| | | |/ _ \/ __| / __| |/ _ \| '_ \| || '__/ _ \/ _ \\'''
	print '	| |_| |  __/ (__| \__ \ | (_) | | | | || | |  __/  __/'
	print '	|____/ \___|\___|_|___/_|\___/|_| |_|_||_|  \___|\___|决策树'
	print
	myDat, labels = createDataSet()
	myTree = Generate_decision_tree(myDat, labels)
	print '[*]生成的决策树：\n',myTree

if __name__ == '__main__':
	main()