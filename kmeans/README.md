## 0x00 废话

n年前的东西，搬到一起。

旧博客原文：[数据挖掘之k-means算法的Python实现](https://blog.csdn.net/SKI_12/article/details/78298719)

## 0x01 简介

K-means算法是很典型的基于距离的聚类算法，采用距离作为相似性的评价指标，即认为两个对象的距离越近，其相似度就越大。该算法认为簇是由距离靠近的对象组成的，因此把得到紧凑且独立的簇作为最终目标。

## 0x02 基本原理

k均值算法原理：

1. 从n个数据对象任意选择k个对象作为初始聚类中心。
2. 根据每个聚类对象的均值，计算每个对象与这些中心对象的距离，并根据最小距离重新对相应对象进行划分。

3. 重新计算每个聚类的均值。

4. 循环2.3步骤，知道每个聚类不再发生变化为止。

