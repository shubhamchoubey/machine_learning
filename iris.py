#!/usr/bin/python3
from sklearn.datasets import load_iris 
from sklearn import tree
import numpy as np

#calling load_iris() function
fl_iris=load_iris()

#extracting data for training
features=fl_iris.data

test_indices=[49,99,149]

#removing testing data
training_data=np.delete(features,test_indices,axis=0)

#taking data for testing
testing_data=fl_iris.data[test_indices]

#setting target data
target=fl_iris.target
target_data=np.delete(target,test_indices,axis=0)

#calling decision tree classifier
algo=tree.DecisionTreeClassifier()

training=algo.fit(training_data,target_data)

resoutput=training.predict([testing_data[2]])

if resoutput==[0]:
   output='Setosa'
elif resoutput==[1]:
   output='versicolor'
else:
   output='verginia'
print(output)




