import pandas as pd

df1 = pd.read_csv('hw10\provinces_updated.xls - Sheet1.csv')
print(df1.head())

# print(df1.loc[:,['Name']])

print(df1.loc[df1['Division'] == ('Thành phố Trung ương') ,['Name','Region']])

