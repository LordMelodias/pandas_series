# What is .iloc?
# .iloc is used to access data by index number (not by name) in a DataFrame or Series.

# syntax: .iloc[row_index, column_index]

import pandas as pd

# Dataframe
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22]
}

df = pd.DataFrame(data)
print("Dataframe: \n", df)
print(df.iloc[1, 0])  # Output: Alice (row 1, column 0)


# Series
s = pd.Series(['apple', 'banana', 'cherry'])
print("Series:\n", s)

print("Using iloc[0]:", s.iloc[0])  # Output: apple
print("Using iloc[2]:", s.iloc[2])  # Output: cherry