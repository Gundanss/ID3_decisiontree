from sklearn.datasets import load_iris
from sklearn import tree
import pandas as pd
import numpy as np
import math

# pip install -U scikit-learn
#
# 引入数据
iris=load_iris()
X = iris.data
y = iris.target
print(X)
print(y)

# data = pd.read_csv("modifiedID3.csv")
data = pd.read_csv("modifiedC4.5.csv")
# data = data.drop('ID',axis=1)
data = data.drop('X',axis=1)
data = data.drop('Y',axis=1)
data = data.drop('month',axis=1)
data = data.drop('day',axis=1)
data = data.drop('temp',axis=1)
data = data.drop('RH',axis=1)
data = data.drop('wind',axis=1)
data = data.drop('rain',axis=1)
data = data.drop('FFMC',axis=1) #不能算
data = data.drop('DMC',axis=1) #不能算
data = data.drop('ISI',axis=1) #能算 但最后是area
data = data.drop('DC',axis=1) #能算，但最后是area

target_values = data['area'].values
print("y:", target_values)
target_names = data['area'].unique()
print("target_names:", target_names)

data = data.drop('area',axis=1)
feature_names = list(data.columns)
dataSet = data.values
print("X:", dataSet)
print("feature_names:", feature_names)

#训练数据和模型,采用ID3或C4.5训练
clf=tree.DecisionTreeClassifier(criterion='entropy')
# clf=clf.fit(X, y) #change
clf=clf.fit(dataSet, target_values) #change
print(clf)

print(iris.feature_names)
print(iris.target_names)

#引入graphviz模块用来导出图,结果图如下所示
# pip install graphviz
import graphviz
# dot_data=tree.export_graphviz(clf,out_file=None,feature_names=
#          iris.feature_names,class_names=iris.target_names,filled=
#          True,rounded=True,special_characters=True) #change
dot_data=tree.export_graphviz(clf,out_file=None,feature_names=
         feature_names,class_names=target_names,filled=
         True,rounded=True,special_characters=True) #change
graph=graphviz.Source(dot_data)
graph.view()