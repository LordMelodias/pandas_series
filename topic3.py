# What is .loc?
# .loc is used to access data by label (name) in DataFrames and Series. (not by number).

# syntax: .loc[row_label, column_label]


import pandas as pd

# Series
# Creating a Series
data = {'Name': ['John', 'Alice', 'Bob']}
series = pd.Series(data['Name'], index=['a', 'b', 'c'])

# Using .loc to get a value by index label
print("Series :\n", series)
print("Using loc on series: ", series.loc['b'])  # Output: Alice

# Dataframe
data2 = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22]
}

df2 = pd.DataFrame(data2)
print("Dataframe: \n", df2)
print("Using loc on dataframe: ",df2.loc[1, 'Name'])  # Output: Alice

# access multiple columns
col = ['Name', 'Age']
print("Using loc on dataframe: \n", df2.loc[1, col])

# using loc with condition
print("using loc with condition: \n", df2.loc[df2['Age']>24])

