#!/usr/bin/python
#coding=utf-8

from numpy import *
import matplotlib.pyplot as plt
import k_means
from optparse import OptionParser

def main():

	print "[*]加载数据..."
	dataSet = []
	fileIn = open('testSet.txt')
	for line in fileIn.readlines():
		lineArr = line.strip().split('\t')
		dataSet.append([float(lineArr[0]), float(lineArr[1])])

	print "[*]聚类..."
	dataSet = mat(dataSet)#用mat函数转换为矩阵之后可以才进行一些线性代数的操作
	k = options.k
	centroids, clusterAssment = k_means.kmeans(dataSet, k)

	print "[*]输出图形化结果"
	k_means.showCluster(dataSet, k, centroids, clusterAssment)

if __name__ == '__main__':

	parser = OptionParser('./test.py [-k <k值, 默认为2>]')
	parser.add_option('-k',dest='k',type='int',default=2,help='k值')
	(options,args) = parser.parse_args()

	print '	 _                                        '
	print '	| | __     _ __ ___   ___  __ _ _ __  ___ '
	print "	| |/ /____| '_ ` _ \ / _ \/ _` | '_ \/ __|"
	print "	|   <_____| | | | | |  __/ (_| | | | \__ \\"
	print '	|_|\_\    |_| |_| |_|\___|\__,_|_| |_|___/ k-均值'
	print
	main()