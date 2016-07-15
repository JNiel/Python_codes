# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def hello():
    a, b, c= 1, 2, "OK!"
    greetings = "Hello Python World!"
    print greetings
    print a
    print b
    print c
    print greetings[6:]    
    
    del a, b, c
    
    list_test = ["okidoki", [1, 2,3,4], 123213]
    
    print list_test
    
    
def dictionary():
    dict = {}
    dict['one'] = "This is one."
    dict[2] = "This is two."
    
    tinydict = {"name": "Jon", "age": 28, "occupation": "Data scientist"}
    
    print dict
    print dict['one']
    print dict[2]
    
    print tinydict
    print tinydict.keys()
    print tinydict.values()
    
    print tinydict["name"]
    
    
def nextWork():
    import time;
    import calendar;
    
    localtime = time.asctime(time.localtime(time.time()))
    cal = calendar.month(2016, 03)
    
    print "Local current time is: ", localtime
    print cal
    
    
def printme(str):
    print str
    return
    
    
class Employee:
    
    empCount=0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount():
        print empCount
        
    def displayEmployee(self):
        print "Name:", self.name, ", salary: ", self.salary, "."