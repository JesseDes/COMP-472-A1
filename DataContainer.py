import pandas
import enum

class DataContainer:
  def __init__(self, name ,trainingSource, testSource,  validationSource = None , symbols = None ):
    self.parsed_training = self.parseData(pandas.read_csv(trainingSource, header=None))
    self.parsed_test =  self.parseData(pandas.read_csv(testSource, header=None))
    if validationSource:
      self.parsed_validation = self.parseData(pandas.read_csv(validationSource, header=None))

    if symbols:
      self.symbols = pandas.read_csv(symbols)['symbol'].tolist()

    self.name = name


  def parseData(self, dataframe):
    training_result = dataframe[dataframe.shape[1] - 1].tolist()
    training_input = []
    for index ,rows in dataframe.iterrows():
      training_input.append(rows.tolist()[:-1])
    return [training_input, training_result]
    
class DataContainerTypes(enum.Enum):
  Input = 0
  Results = 1
