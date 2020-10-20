import enum

class ExpParams:
  def __init__(self, **kwargs):
      totalTest = 1
      currentParamValue = {}
      for member in kwargs.items():
          currentParamValue[member[0]] = 0
          if len(member[1]) > 0:
              totalTest *= len(member[1])
      self.__paramList = kwargs
      self.__totalTest = totalTest
      self.__currentTest = 0
      self.__currentParamValues = currentParamValue

  def getCurrentTestInstanceParams(self):
      currenInstanceParam = {}
      param_count = self.getParamCount()
      i = param_count - 1
      increment_next_param = True #lowest order paramter always increments
      while i >= 0:
          param = self.getParamByOrder(i)
          i -= 1
          param_list = self.getParamByName(param)
          param_index = self.__currentParamValues[param]
          currenInstanceParam[param] = param_list[param_index]
          if increment_next_param:
              if self.__currentParamValues[param]  > (len(param_list) - 2):
                  self.__currentParamValues[param] = 0
              else:
                  self.__currentParamValues[param] += 1

              increment_next_param = self.__currentParamValues[param] == 0

      self.__currentTest += 1
      return currenInstanceParam
  
  def getParamByOrder(self, order):
      return list(self.__paramList)[order]

  def getParamCount(self):
      return len(list(self.__paramList))

  def getParamByName(self, name):
      return self.__paramList[name]

  def isTestsComplete(self):
      return self.__currentTest >= self.__totalTest

  
  

class DTExpParams(enum.Enum):
  CRITERION = 'criterion'
  MAX_DEPTH = 'max_depth'
  MIN_SAMPLE_SPLIT = 'min_samples_split'
  MIN_IMPURITY_DEC = 'min_impurity_decrease'
  CLASS_WEIGHT = 'class_weight'

class MLPExpParams(enum.Enum):
    ACTIVATION = "activation"
    HIDDEN_LAYER_SIZES = 'hidden_layer_sizes'
    SOLVER = 'solver'