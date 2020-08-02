#!/usr/bin/python
#coding=utf-8
import itertools

#事务数据库，和课本上的数据一致
Data = {
	'T100':['I1','I2','I5'],
        	'T200':['I2','I4'],
        	'T300':['I2','I3'],
        	'T400':['I1','I2','I4'],
        	'T500':['I1','I3'],
        	'T600':['I2','I3'],
        	'T700':['I1','I3'],
        	'T800':['I1','I2','I3','I5'],
        	'T900':['I1','I2','I3']
}

#定义Apriori类
class Apriori:
	def __init__(self,min_sup=0.2,dataDic={}):
		#事务数据库data
		self.data = dataDic

		#获取事务的数量
		self.size = len(dataDic)

		#最小支持度阈值
		self.min_sup = min_sup
		self.min_sup_val = min_sup * self.size

	#找出频繁1项集的集合L1
	def find_frequent_1_itemsets(self):
		#这里的字典格式设置为: {itemset1:freq1,itemsets2:freq2}
		FreqDic = {}
		for event in self.data:
			for item in self.data[event]:
				if item in FreqDic:
					FreqDic[item] += 1
				else:
					FreqDic[item] = 1
		L1 = []
		for itemset in FreqDic:
			if itemset >= self.min_sup_val:
				L1.append([itemset])
		return L1

	#实现连接和剪枝
	def apriori_gen(self,L_last):
		k = len(L_last[0]) + 1
		Ck = []
		for itemset1 in L_last:
			for itemset2 in L_last:
				#连接步：产生候选
				flag = 0
				for i in range(k-2):
					if itemset1[i] != itemset2[i]:
						flag = 1
						break;
				if flag == 1:
					continue
				if itemset1[k-2] < itemset2[k-2]:
					c = itemset1 + [itemset2[k-2]]
				else:
					continue

				#剪枝步：删除非频繁的候选
				if self.has_infrequent_subset(c,L_last,k):
					continue
				else:
					Ck.append(c)
		return Ck

	#使用先验知识
	def has_infrequent_subset(self,c,L_last,k):
		#返回列表中元组的项
		subsets = list(itertools.combinations(c,k-1))
		for each in subsets:
			#将元组转换成列表
			each = list(each)
			if each not in L_last:
				return True
		return False

	#运行Apriori算法
	def run(self):
		L_last = self.find_frequent_1_itemsets()
		L = L_last
		i = 0
		j = 2
		while L_last != []:
			Ck = self.apriori_gen(L_last)
			FreqDic = {}
			for event in self.data:
				#获取所有支持的子集
				for c in Ck:
					#判断是否是子集
					if set(c) <= set(self.data[event]):
						if tuple(c) in FreqDic:
							FreqDic[tuple(c)]+=1
						else:
							FreqDic[tuple(c)]=1

			Lk = []
			num = []
			Lo = []
			for c in FreqDic:
				if FreqDic[c] > self.min_sup_val:
					Lk.append(list(c))
					num.append(FreqDic[c])

			L_last = Lk
			L += Lk

			if len(Lk) != 0:
				print "[*] 频繁%d项集L%d："%(j,j)
				for i in xrange(0,len(Lk)):
					print Lk[i],':',num[i]
				print
				j += 1
				
		return L

def main():
	print '''
	    _               _            _ 
	   / \   _ __  _ __(_) ___  _ __(_)
	  / _ \ | '_ \| '__| |/ _ \| '__| |
	 / ___ \| |_) | |  | | (_) | |  | |
	/_/   \_\ .__/|_|  |_|\___/|_|  |_|
	        |_|                        

	'''
	a = Apriori(dataDic=Data)
	result = a.run()
	print "[*] 所有的频繁项集："
	for r in result:
		print r

if __name__ == '__main__':
	main()