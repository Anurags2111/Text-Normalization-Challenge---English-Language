import pandas as pd

df = pd.read_csv('../input/en_train.csv')
print("Total class: ", df['class'].unique().size)
df['class'].unique()