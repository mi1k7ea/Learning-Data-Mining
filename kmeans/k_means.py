#!/usr/bin/python
#coding=utf-8
from numpy import *
import matplotlib.pyplot as plt

#计算欧氏距离
def euclDistance(v1,v2):
	#
	return sqrt(sum(power(v2 - v1, 2)))

#使用随机样本初始化质心
def initCentroids(dataSet,k):

	numSamples, dim = dataSet.shape
	centroids = zeros((k, dim))

	for i in range(k):
		index = int(random.uniform(0, numSamples))
		centroids[i, :] = dataSet[index, :]

	return centroids

#k-均值聚类
def kmeans(dataSet,k):
	numSamples = dataSet.shape[0]
	clusterAssment = mat(zeros((numSamples, 2)))
	clusterChanged = True

	#初始化质心
	centroids = initCentroids(dataSet, k)

	while clusterChanged: 
		clusterChanged = False
		#遍历样本数据
		for i in xrange(numSamples):
			minDist  = 100000.0
			minIndex = 0
			#遍历质心
			#找出跟质心最近的数据点
			for j in range(k):
				distance = euclDistance(centroids[j, :], dataSet[i, :])
				if distance < minDist:
					minDist  = distance
					minIndex = j

			#更新簇
			if clusterAssment[i, 0] != minIndex:
				clusterChanged = True
				clusterAssment[i, :] = minIndex, minDist**2

		#更新质心
		for j in range(k):
			pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
			centroids[j, :] = mean(pointsInCluster, axis = 0)

	print '[+]聚类完成！'
	return centroids, clusterAssment

#只显示二维数据的簇
def showCluster(dataSet,k,centroids,clusterAssment):
	numSamples, dim = dataSet.shape
	if dim != 2:
		print "[!]错误：输入的数据不是二维的！"
		return 1

	mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
	if k > len(mark):
		print "[!]输入的k值太大！"
		return 1

	#描绘所有的样本数据
	for i in xrange(numSamples):
		markIndex = int(clusterAssment[i, 0])
		plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

	mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
	#描绘质心
	for i in range(k):
		plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)

	plt.show()