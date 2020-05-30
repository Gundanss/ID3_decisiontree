import trees
import time
import treePlotter
import importlib


# file = open('gender.txt')
file = open('modified4.0monthDcTempRhRain.txt')
data = [inst.strip().split('\t') for inst in file.readlines()]

# feature = ['height','voice','weight']
# feature = ['FFMC','DMC','DC','ISI','rain']
# feature = ['FFMC','DMC','DC','ISI','temp','RH','wind','rain']
feature = ['month','DC','temp','RH','rain']
# feature = ['location','month','ffmc','dc','isi','rain']

print(data)

t1 = time.clock()
Tree = trees.createTree(data, feature)
Tree
t2 = time.clock()
print(Tree)
print('execute for ', t2-t1)


importlib.reload(treePlotter)
treePlotter.createPlot(Tree)
