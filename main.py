import numpy as np
import pandas as pd 
from Person import *
from Group import *

girls = ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"]
boys = ["m1","m2","m3","m4","m5","m6","m7","m8","m9","m10"]

def create_group(girls,boys):
    people = []

    for a in girls:
        people.append(Person("f",a))

    for a in boys:
        people.append(Person("m",a))
    
    return people

group = Group(create_group(girls,boys))
group.tostring()




    
    