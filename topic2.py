# What is dataframe?
# A pandas dataframe is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as pd

# A DataFrame in Pandas is usually created using:
'''
1. dictionary
2. list of list
3. tuple of tuple
4. list of dictionaries
5. NumPy arrays
6. list of tuple
7. and more
'''

# Dictionary
a = {
    "color": ["red", "green", "black", "orange"],
    "fruit": ["apple", "kiwi", "fig", "mango"]
}

dictdataframe = pd.DataFrame(a)
print("Datafrane using dictionary: \n", dictdataframe)

# list of list
b = [
    ["red", "apple"],
    ["green", "kiwi"],
    ["black", "fig"],
    ["orange", "mango"]
]
listdataframe = pd.DataFrame(b)
print("Dataframe using list: \n", listdataframe)

# tuple of tuple
c = (
    ("red", "apple"),
    ("green", "kiwi"),
    ("black", "fig"),
    ("orange", "mango")
)
tupleoftupledf = pd.DataFrame(c)
print("Dataframe using tuple: \n", tupleoftupledf)

# List of dictionary
d = [
    {"color": "red", "fruit": "apple"},
    {"color": "green", "fruit": "kiwi"},
    {"color": "black", "fruit": "fig"},
    {"color": "orange", "fruit": "mango"}
]
listofdictdf = pd.DataFrame(d)
print("Dataframe using list of dictionary: \n", listofdictdf)

# numpy arrays
import numpy as np

arr = np.array(
    [
        ["red", "apple"],
        ["green", "kiwi"],
        ["black", "fig"],
        ["orange", "mango"]
    ]
)
arrayofdf = pd.DataFrame(arr)
print("Dataframe using array: \n", arrayofdf)

#list of tuple
e = [
    ("red", "apple"),
    ("green", "kiwi"),
    ("black", "fig"),
    ("orange", "mango")
]
listoftupledf = pd.DataFrame(e)
print("Dataframe using list of tuple: \n", listoftupledf)


# when to use which input type to create pandas dataframe
'''
1. Dictionary
   - Use When: You have data in columns (labeled).

2. List of Lists
   - Use When: You have only values (no column names).

3. Tuple of Tuples
   - Use When: You want fixed row values (like list of lists but can't change).

4. List of Dictionaries
   - Use When: Each row is a record (like from JSON or API).

5. NumPy Array
   - Use When: You already have data in NumPy (especially numeric data).

6. List of Tuples
   - Use When: You have row-wise data (like CSV or database rows).
'''

# columns: Custom column names
f = [
    ["red", "apple"],
    ["green", "kiwi"],
    ["black", "fig"],
    ["orange", "mango"]
]
listdataframecolumn = pd.DataFrame(b, columns=["color", "fruit"])
print("Dataframe using list with columns: \n", listdataframecolumn)

# dtype = Force a specific data type (e.g., str, int, float)
g = [
    [101, "Alice"],
    [102, "Bob"],
    [103, "Charlie"]
]
dtypedf = pd.DataFrame(g, dtype=str, columns=["color", "fruit"])
print("Dataframe using list with dtype: \n", dtypedf)
