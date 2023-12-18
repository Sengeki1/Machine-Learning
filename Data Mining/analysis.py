import os
import pandas as pd

data_file_folder = '/home/marco/Transferências/archive/'
dfs = {}

for file in os.listdir(data_file_folder):
    if file.endswith('.csv'):
        print('Loading file {0}...'.format(file))
        full_path = os.path.join(data_file_folder, file)
        df = pd.read_csv(full_path, sep=';', low_memory=False)
        file_name = os.path.splitext(file) # tuple(name, after dot)
        dfs[file_name[0]] = df

merged_df = pd.merge(dfs['client'], dfs['disp'], on='client_id', how='inner')
merged_df = pd.merge(merged_df, dfs['account'], on='account_id', how='inner') 
merged_df = pd.merge(merged_df, dfs['order'], on='account_id', how='inner')  
merged_df = pd.merge(merged_df, dfs['trans'], on='account_id', how='inner')  
merged_df = pd.merge(merged_df, dfs['loan'], on='account_id', how='inner')  
merged_df = pd.merge(merged_df, dfs['card'], on='account_id', how='inner')  
merged_df = pd.merge(merged_df, dfs['district'], left_on='district_id_x', right_on='A1', how='inner')
print("...Data merged!!")

merged_df.to_csv('merged_data.csv', index=False)
