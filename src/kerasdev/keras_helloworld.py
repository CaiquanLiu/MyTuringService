# coding:utf-8
'''
Created on Jun 30, 2017

@author: eddy
参考：https://github.com/fastforwardlabs/keras-hello-world/blob/master/kerashelloworld.ipynb
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV

from keras.layers.core import Dense,Activation
from keras.models import Sequential
from keras.utils import np_utils
from sklearn.decomposition.tests.test_nmf import random_state
from statsmodels.tsa.tests import test_x13
from nltk.chunk.util import accuracy

class KerasHelloWorld(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def one_hot_encode_object_array(self,arr):
        uniques,ids=np.unique(arr, return_inverse=True)
        return np_utils.to_categorical(ids, len(uniques))
    
        
    def test(self):
        iris=sns.load_dataset("iris")
        X=iris.values[:,:4]
        y=iris.values[:,4]
        
        train_X, test_X, train_y, test_y=train_test_split(X, y, train_size=0.5, random_state=0)
        
        # lr=LogisticRegressionCV()
        # lr.fit(train_X, train_y)
        # 
        # print("Accuracy= {:.2f}".format(lr.score(test_X, test_y)))
        
        train_y_ohe=self.one_hot_encode_object_array(train_y)
        test_y_ohe=self.one_hot_encode_object_array(test_y)
        
        model=Sequential()
        
        model.add(Dense(16, input_shape=(4,)))
        model.add(Activation('sigmoid'))
        
        model.add(Dense(3))
        model.add(Activation('softmax'))
        
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])
        
        model.fit(train_X, train_y_ohe, nb_epoch=100, batch_size=1, verbose=0)
        
        loss, accuracy=model.evaluate(test_X, test_y_ohe, verbose=0)
        
        print("Accuracy= {:.2f}".format(accuracy))