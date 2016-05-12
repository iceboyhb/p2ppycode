'''
Created on 2016 5/11
@author: BingHou
'''
import math
from CheckVariable import CheckVariable
from ConvertToNumber import ConvertToNumber


class Calculator(object):
    def __init__(self, number, digit_num):
        self.number = number
        self.digit_num = digit_num 
    
    def RoundUp(self):
        return (math.ceil(self.number))
    
    def RoundDown(self):
        return (int(self.number))
    
    def Round(self):
        if(CheckVariable(self.digit_num).GetType()=='string'):
            digit_num = ConvertToNumber(self.digit_num).ToIntNumber()
            return(round(self.number, digit_num))
        else: 
            return (round(self.number, self.digit_num))
        
    def RoundDigit(self):
        if(CheckVariable(self.digit_num).GetType()=='string'):
            digit_num = ConvertToNumber(self.digit_num).ToIntNumber()
            return(self.number - self.number % digit_num)
        else:
            return(self.number - self.number % self.digit_num)
    
    