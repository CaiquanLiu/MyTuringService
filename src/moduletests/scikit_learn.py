'''
Created on 2017年3月17日

@author: liucaiquan
'''

if __name__ == '__main__':
    from machine_learning.scikit_learn import ScikitUtils
    scikit = ScikitUtils()
    
    scikit.data_load()
    
    scikit.feature_selection()
    
    scikit.logistic_regression()
