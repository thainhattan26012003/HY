import csv
import numpy as np
import pandas as pd


df = pd.read_csv('Trinh_ngu.csv')

results_lst = []
for i in range(1,7):
    a = df.iloc[:,i:i+1].values
    results_lst.append(np.mean(a))
    
column_names = ["Similarity", "MAE", "RMSE", "FSD", "R_score", "NSE"]

df_named = pd.DataFrame([results_lst], columns=column_names)

print(df_named)