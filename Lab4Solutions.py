# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:08:16 2019

@author: AFajemisin

Lab 4 Solutions
"""
import numpy as np
# Exception Handling

myFile = "C:\\Users\\afajemisin\\Desktop\\Modules\\Database and Analytics Programming H9DAP\\Lectures\\Week 4\\myText.txt"
myFH = open(myFile, "w")
myFH.readlines()


# 3)	Note the type of Error that has been raised.
# UnsupportedOperation: not readable File IO error

# 4)	Modify your code to
try:
    myFH = open("myText.txt", "w")
    myFH.readlines()
except:
    print("Oh No!!!!! FILE IO ERROR!!")
finally:
    myFH.close()

#5)	Investigate how you would create your own Exception class. Then create your own Exception class and use it in your code from the previous exercise.
class MyIOError(Exception):
    pass # some real stuff will go in here. For now, we use 'pass' function

try:
    try:
        myFH = open("myText.txt", "w")
        myFH.readlines()
    except (IOError):
        raise MyIOError 

except (MyIOError):
    print("Oh No!!!!! FILE IO ERROR!!")
finally:
    myFH.close()

################  NumPy Exercise 1  ################
    
b = np.arange(24).reshape(2,3,4)
    
# Choose the first set of 3 rows and 4 columns of data
b[0] # or
b[0, :, :] # or
b[0,...]

# Choose the second row of data from the second set of 3 rows of data
b[1,1]

# Choose all the data from the second column for both the first and second sets of rows and columns of data
b[...,1]

# 2)	Use the ravel function to flatten the data
np.ravel(b)

# What’s the difference between ravel and flatten?

b.shape = (6,4)
b

# 4)	Get the transpose of the new data structure.
b = b.transpose()
b
# Restack the rows of the transposed data structure in reverse order (hint: look at the row_stack function).


#6)	Split the resulting data structure horizontally (hint: look at the hsplit function).


################  NumPy Exercise 2  ################
appleData = "C:\\Users\\afajemisin\\Desktop\\Modules\\Database and Analytics Programming H9DAP\\Lectures\\Week 4\\AAPL.csv"
close, volume = np.loadtxt(appleData, delimiter=',', usecols=(4,6), unpack=True, skiprows=1)
#unpack=True => column is transposed into vector

# https://www.wikihow.com/Calculate-Weighted-Average
vwap = np.average(close, weights=volume) 

np.median(close)
np.var(close)
h, l = np.loadtxt(appleData, delimiter=',', usecols=(2,3), unpack=True, skiprows=1)
np.max(h)
np.min(l)
# 7)	Load data from column 5 of AAPL.csv. Also, load data from column 5 of MSFT.csv.
cAAPL = np.loadtxt(appleData, delimiter=',', usecols=(4,), unpack=True, skiprows=1)

msftData = "C:\\Users\\afajemisin\\Desktop\\Modules\\Database and Analytics Programming H9DAP\\Lectures\\Week 4\\MSFT.csv"

cMSFT = np.loadtxt(msftData, delimiter=',', usecols=(4,), unpack=True, skiprows=1)

covariance = np.cov(cAAPL, cMSFT)

covariance.diagonal()

np.corrcoef(cAAPL, cMSFT)




################  Regular Expression Exercise  ################
# Use the following as an example
pat = r"(https?://)?[0-9a-zA-Z]+\.[-_0-9a-zA-Z]+\.[0-9a-zA-Z]+"
    
    
    
    
    
    
    
    
    
    