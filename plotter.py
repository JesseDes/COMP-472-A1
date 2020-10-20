import matplotlib.pyplot as plt
from DataContainer import DataContainer, DataContainerTypes

def PlotDataContainer(dataSet):
  validationResultsCount =  [0] * len(dataSet.symbols)
  testingResultsCount =  [0] * len(dataSet.symbols)
  trainingResultsCount = [0] * len(dataSet.symbols)

  for result in dataSet.parsed_training[DataContainerTypes.Results.value]:
    trainingResultsCount[result] += 1

  for result in dataSet.parsed_validation[DataContainerTypes.Results.value]:
    validationResultsCount[result] += 1

  for result in dataSet.parsed_test[DataContainerTypes.Results.value]:
    testingResultsCount[result] += 1

  plotCategoryInstances(dataSet.symbols,[trainingResultsCount,validationResultsCount, testingResultsCount],['Training Data', "Validation Data", "Testing Data"], dataSet.name)

def plotCategoryInstances (categories, dataList, labels, title):
    dataLength = len(dataList)
    width = 6 * dataLength
    spacer = '1' + str(dataLength) + '1'
    plt.figure(figsize=(width, 6))
    spacer = int(spacer)
    count = 0
    for data in dataList:
      plt.subplot(spacer)
      spacer += 1
      plt.bar(categories, data)
      plt.title(labels[count])
      count += 1
    plt.suptitle(title)
    plt.show()