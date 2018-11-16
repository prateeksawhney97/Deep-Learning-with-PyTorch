import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expList = np.exp(L)
    sumList = sum(expList)
    
    result = []
    for i in expList:
        result.append(i/sumList)
    return result
    
        
