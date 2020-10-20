from DataContainer import DataContainer
from plotter import PlotDataContainer
from ModelRunner import runModelOp

def getValidSelection(min,max, prompt):
    selection_valid = False
    while not selection_valid:
        selection = input(prompt)
        if selection.isdigit() and int(selection) >= min and int(selection) <= max: 
            selection_valid = True
        else:
            print("Please enter a valid selection, try again")
    
    return int(selection)

end_test = False

while not end_test:
    selection_valid = False
    dataChoice =  getValidSelection(1,2,"Which data set would you like to use? \n [1] Data set 1 (A-Z) \n [2] Data set 2 (Greek symbols) \n :")
    if dataChoice == 1:
        if not 'd1' in locals():
            d1 = DataContainer("data-set-1", './Assig1-Dataset/train_1.csv','./Assig1-Dataset/test_with_label_1.csv','./Assig1-Dataset/val_1.csv', './Assig1-Dataset/info_1.csv')
        dataSet = d1
    else:
        if not 'd2' in locals():
            d2 = DataContainer("data-set-2", './Assig1-Dataset/train_2.csv','./Assig1-Dataset/test_with_label_2.csv','./Assig1-Dataset/val_2.csv', './Assig1-Dataset/info_2.csv')
        dataSet = d2
    opType = getValidSelection(1,9,"Which test would you like to do? \n [1] GNB \n [2] BASE-DT \n [3] BEST-DT (Configure test params in TreeTestParams.py) \n [4] PER \n [5] BASE-MLP \n [6] BEST-MLP (configure test params in MLPTestParams.py \n [7] All base tests (GNB, BASE-DT , PER, BASE-MLP) \n [8] ALL tests \n [9] Plot data \n:")
    if opType == 9:
        PlotDataContainer(dataSet)
    else:
        runModelOp(opType,dataSet)

    end_test = getValidSelection(1,2,"Would you like to do something else? \n [1] Yes \n [2] No \n:") == 2

