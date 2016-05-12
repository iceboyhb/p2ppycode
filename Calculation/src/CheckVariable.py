''' 
Created on 2016 5/11
@author: BingHou
'''

class CheckVariable(object): 
    def __init__(self, inputVariable):
        self.inputVariable = inputVariable
        
        
    def GetType(self):                 
        if isinstance(self.inputVariable, str):
            return 'string'
        elif isinstance(self.inputVariable, int):
            return 'integer'
        elif isinstance(self.inputVariable, float):
            return 'float'