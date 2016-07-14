# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:06:35 2016

@author: jon.nielsen
"""

import numpy as np
import scipy as sp
import pandas
import pylab
import matplotlib.pyplot as plt
import os

trainFile = "C:\Users\jon.nielsen\Desktop/actuals.csv"

df = pandas.read_csv(trainFile)

#Show what data types are in the frame.
df.dtypes