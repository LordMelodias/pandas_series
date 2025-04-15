# What is a Series?
# A pandas series is like a column in a table. It is one-dimensional array holding data of any type.

import pandas as pd

# In pandas a Series can be created using lists, tuples, arrays, and even dictionaries.

# Using list to create a series
a = [9, 5, 4]
listseries = pd.Series(a)
print("Series using list:\n ", listseries)

# Using tuple to create a series
b = (9, 5, 4)
tupleseries = pd.Series(b)
print("Series using tuple:\n ", tupleseries)

# Using dictionary to create a series
c = {"a": 9, "b": 5, "c": 4}
dictionaryseries = pd.Series(c)
print("Series using Dictionary:\n ", dictionaryseries)

# Using array to create a dictionary
import numpy as np
d = np.array([9, 5, 4])
arrayseries = pd.Series(d)
print("Series using array:\n ", arrayseries)


#  when to use which input type to create a pandas Series
'''
Type	Ordered	 Mutable    Custom Index	    When to Use
list	✅	   ✅	      ❌ (default)	   Simple series without labels
tuple	✅	   ❌	      ❌ (default)	   Immutable data
array	✅	   ✅	      ❌ (default)	   Numerical/scientific workflows
dict	✅	   ✅	      ✅                When you need custom labels/index
'''

# Labels
# Label means the name of a row (or column) ,default it have numerical value like 0,1,2,3.....,n .
# Used index argument to name own labels

e = [9, 5, 4]
labelseries = pd.Series(e, index=['x', 'y', 'z'])
print("Series using list with Labels:\n ", labelseries)
print("Individual access: ", labelseries['y'])

