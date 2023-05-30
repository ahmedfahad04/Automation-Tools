import re

import pandas as pd

data = pd.read_excel('data.xlsx')

# remove all the extra spaces in the column names
data.columns = data.columns.str.strip()
print(data.columns)