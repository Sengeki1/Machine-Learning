import pandas as pd

## loading data frame
df = pd.read_csv('pokemon_data.csv')
print(df.tail(3))

df_xlsx = pd.read_excel('pokemon_data.xlsx')
print(df_xlsx.head(3))

df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t') # delimiter is to specify what is in between each column
print(df_txt.head(3))

## reading data
print(df.columns) # each column

print(df['Name'][0:5]) # each pokemon name in the column Name from the first to row 5
print(df[['Name', 'Type 1']][0:5])

print(df.iloc[1]) # prints all the values in that row (iloc stands from integer location)

print(df.iloc[2,1]) # on the row 2 and column 1
#for index, row in df.iterrows(): # iterate through all the rows in the df
#    print(index, row['Name'])
