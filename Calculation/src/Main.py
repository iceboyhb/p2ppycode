'''
Created on 2016,5,10

@author: BingHou
'''  
from Calculate import Calculator 

       
numTest = Calculator(5.4938,3)      
print ('round up= ', numTest.RoundUp()) 
print ('round down= ', numTest.RoundDown()) 

print ('round 3 digits= ', numTest.Round()) 

numTest = Calculator(5.4938,'two')
print ('round two digits= ', numTest.Round()) 
 

numTest2 = Calculator(345, 10)
print ('round Keep 10 = ',numTest2.RoundDigit())

numTest3 = Calculator(345, 100)
print ('round Keep 100 = ', numTest3.RoundDigit())
  

numTest2 = Calculator(345, 'ten')
print ('round Keep ten = ',numTest2.RoundDigit())

numTest3 = Calculator(345599678, 'ten thousand')
print ('round Keep ten thousand = ', numTest3.RoundDigit())