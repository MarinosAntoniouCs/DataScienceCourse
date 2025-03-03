import pandas as pd

# import numpy as np
import numpy as np

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])

ser = pd.Series(data)
print(ser)

print(pd.Series(['m','a','r','i','n','o','s']))

lst = [1, 2, 3, 4, 5]
#DataFrame is a 2d array concisting of the rows columns and data
df = pd.DataFrame([lst, lst, lst, lst, lst, lst, lst, lst, lst], 
                  columns=['A', 'B', 'C', 'D', 'E'])

print(df)

# intialise data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)

#Following i will use Pandas functions to load data from various datasets