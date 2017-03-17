# coding:utf-8
'''
Created on 2017年3月17日
参考：http://www.cnblogs.com/CheeseZH/p/5250997.html
@author: liucaiquan
'''

class ScikitUtils(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    # 加载数据
    def data_load(self):
        import numpy as np
        import urllib2
        # url with dataset
        url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
        # download the file
        raw_data = urllib2.urlopen(url)
        # load the CSV file as a numpy matrix
        dataset = np.loadtxt(raw_data, delimiter=",")
        # separate the data from the target attributes
        self.X = dataset[:, 0:7]
        self.y = dataset[:, 8] 
        
    # 数据归一化
    def data_normalization(self):
        from sklearn import preprocessing
        # scale the data attributes
        scaled_X = preprocessing.scale(self.X)
        
        # normalize the data attributes
        normalized_X = preprocessing.normalize(self.X)
        
        # standardize the data attributes
        standardized_X = preprocessing.scale(self.X) 
        
    #特征选择
    def feature_selection(self):
        from sklearn import metrics
        from sklearn.ensemble import ExtraTreesClassifier
        model = ExtraTreesClassifier()
        model.fit(self.X, self.y)
        # display the relative importance of each attribute
        print(model.feature_importances_)   
    
    #逻辑回归  
    def logistic_regression(self):  
        from sklearn import metrics
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()
        model.fit(self.X, self.y)
        print('MODEL')
        print(model)
        # make predictions
        expected = self.y
        predicted = model.predict(self.X)
        # summarize the fit of the model
        print('RESULT')
        print(metrics.classification_report(expected, predicted))
        print('CONFUSION MATRIX')
        print(metrics.confusion_matrix(expected, predicted))  
    
    #朴素贝叶斯
    def  naive_bayesian(self):   
        from sklearn import metrics
        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
        model.fit(self.X, self.y)
        print('MODEL')
        print(model)
        # make predictions
        expected = self.y
        predicted = model.predict(self.X)
        # summarize the fit of the model
        print('RESULT')
        print(metrics.classification_report(expected, predicted))
        print('CONFUSION MATRIX')
        print(metrics.confusion_matrix(expected, predicted))
    
    #K近邻  
    def knn(self):
        from sklearn import metrics
        from sklearn.neighbors import KNeighborsClassifier
        # fit a k-nearest neighbor model to the data
        model = KNeighborsClassifier()
        model.fit(self.X, self.y)
        print(model)
        # make predictions
        expected = self.y
        predicted = model.predict(self.X)
        # summarize the fit of the model
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))   
    
    #决策树    
    def cart(self):
        from sklearn import metrics
        from sklearn.tree import DecisionTreeClassifier
        # fit a CART model to the data
        model = DecisionTreeClassifier()
        model.fit(self.X, self.y)
        print(model)
        # make predictions
        expected = self.y
        predicted = model.predict(self.X)
        # summarize the fit of the model
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))   
    
    #支持向量机   
    def svm(self):
        from sklearn import metrics
        from sklearn.svm import SVC
        # fit a SVM model to the data
        model = SVC()
        model.fit(self.X, self.y)
        print(model)
        # make predictions
        expected = self.y
        predicted = model.predict(self.X)
        # summarize the fit of the model
        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))   
        
    # 优化算法参数   
        
        
