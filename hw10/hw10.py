import pandas as pd

df1 = pd.read_csv('hw10\provinces_updated.xls - Sheet1.csv')
print(df1.head())

# # print(df1.loc[:,['Name']])

# print(df1.loc[df1['Division'] == ('Thành phố Trung ương') ,['Name','Region']])

# print(df1.loc[:,['Name','Division']])

# print(df1.loc[df1['Population'] == df1.loc[:,'Population'].max() ,['Name','Population']])
# print(df1.loc[df1['Population'] == df1.loc[:,'Population'].min() ,['Name','Population']])

# a= df1.loc[:,'Area'].sum()
# total= df1.loc[df1['Region']== 'Đồng bằng sông Hồng',['Area']].sum()

# print(total)