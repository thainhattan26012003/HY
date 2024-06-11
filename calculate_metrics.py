import csv
import numpy as np
import pandas as pd

df = pd.read_csv('Trinh_ngu.csv')

a = df.iloc[:, 1:2].values.tolist()
print(np.mean(a))