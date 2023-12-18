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

merged_df = pd.merge(dfs['client'], dfs['disp'], on='client_id', how='inner') # relation client & disposition 

dfs['district'] = dfs['district'].rename(columns ={'A1': 'district_id'})
merged_df = pd.merge(merged_df, dfs['district'], on='district_id', how='inner') # relation between the current df & demograph
merged_df = merged_df.sort_values(['client_id'], ascending=True)

merged_df = pd.merge(merged_df, dfs['account'], on=['district_id', 'account_id'], how='inner') # relation between account & current df
merged_df = pd.merge(merged_df, dfs['card'], on='disp_id', how='inner') # relation between card & current df

merged_df = pd.merge(merged_df, dfs['loan'], on='account_id', how='inner') # relation between df & loan
merged_df = pd.merge(merged_df, dfs['order'], on='account_id', how='inner') # relation between df & order
merged_df = pd.merge(merged_df, dfs['trans'], on='account_id', how='inner') # relation between df & trans

print("...Data merged!!")
merged_df.to_csv('merged_data.csv', index=False)