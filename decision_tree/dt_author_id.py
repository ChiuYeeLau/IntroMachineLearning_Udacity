#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""

import pdb
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier (min_samples_split = 40)
pred = dtc.fit(features_train, labels_train).predict(features_test)

from sklearn.metrics import accuracy_score

print accuracy_score (pred, labels_test)

print len(features_train[0])

pdb.set_trace ()


#########################################################
### your code goes here ###


#########################################################


