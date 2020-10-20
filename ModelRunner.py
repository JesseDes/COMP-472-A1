from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import  confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from DataContainer import DataContainer, DataContainerTypes
from MLPTestParams import MLPExperimentVars
from TreeTestParams import treeParams
from sklearn.model_selection import GridSearchCV
import pandas
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def runTest(clf, dataSet:DataContainer , fuseData = False ):
    if fuseData:
        training_data_input = dataSet.parsed_training[DataContainerTypes.Input.value] + dataSet.parsed_validation[DataContainerTypes.Input.value]
        training_data_results = dataSet.parsed_training[DataContainerTypes.Results.value] + dataSet.parsed_validation[DataContainerTypes.Results.value]
        training_data = [training_data_input , training_data_results]
    else:
        training_data = dataSet.parsed_training

    test_data = dataSet.parsed_test

    y_pred = clf.fit(training_data[DataContainerTypes.Input.value], training_data[DataContainerTypes.Results.value]).predict(test_data[DataContainerTypes.Input.value])
    outPutTestData(y_pred, test_data[DataContainerTypes.Results.value], dataSet.name , list(range(0,len(dataSet.symbols))))

def outPutTestData(y_pred, validation_result, dataSetName, labels):
    print(validation_result.count(1))
    precision = precision_score(validation_result , y_pred, average=None)
    f1 = f1_score(validation_result,y_pred, average=None)
    recall = recall_score(validation_result,y_pred, average=None)
    accuracy = accuracy_score(validation_result,y_pred)
    macro_f1 = f1_score(validation_result,y_pred, average='macro')
    weighted_f1 = f1_score(validation_result,y_pred,average="weighted")

    prediction_frame = pandas.DataFrame({'prediction': y_pred})
    prediction_frame.to_csv(dataSetName+ ".csv", index=True)

    class_performance_frame =  pandas.DataFrame({ 'percision': precision,'recall': recall, 'F-meausre': f1})
    macro_performance_frame = pandas.DataFrame({ 'accuracy': accuracy,'macro f1':macro_f1, 'weighted f1': weighted_f1}, index=[0])
    performance_frame = pandas.concat([class_performance_frame, macro_performance_frame], axis=1) 
    performance_frame.to_csv(dataSetName + "-performance.csv", index=True)
   
    sns.heatmap(confusion_matrix(validation_result, y_pred), annot=True, fmt='d')
    plt.savefig(dataSetName + "-confusion-matrix.png", dpi=400)
    plt.clf()

def runModelOp(operation, dataSet):
    dataSetName = dataSet.name
    modelList = []
    if operation == 1 or operation == 7 or operation == 8:
        modelList.append([GaussianNB(),False])
    if  operation == 2 or operation == 7 or operation == 8:
        modelList.append([tree.DecisionTreeClassifier(criterion='entropy'),False])
    if operation == 3 or operation == 8:
        clf = tree.DecisionTreeClassifier()
        test_DT = GridSearchCV(clf, treeParams, n_jobs=-1)
        modelList.append([test_DT,True])
    if operation == 4 or operation == 7 or operation == 8:
        modelList.append([Perceptron(),False])
    if operation == 5 or operation == 7 or operation == 8:
        modelList.append([MLPClassifier(solver='sgd' , hidden_layer_sizes = (100,) , activation='logistic'),False])
    if operation == 6 or operation == 8:
        clf = MLPClassifier(max_iter=1000)
        test_MLP = GridSearchCV(clf,MLPExperimentVars,n_jobs=-1)
        modelList.append([test_MLP,True])

    for test in modelList:
        if(test[1]):
            testName = "Best-" + test[0].estimator.__class__.__name__
        else:
            testName = test[0].__class__.__name__

        dataSet.name = "outputs/" + testName + " - " + dataSetName
        print("Testing " , testName , " on " , dataSetName)
        runTest(test[0], dataSet, test[1])
            
    dataSet.name = dataSetName
    