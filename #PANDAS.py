#PANDAS
# why pandas 
# 1.flexibility of python 
# 2.working with big data sets

'''Load data into pandas'''
import pandas as pd
df=pd.read_csv ('C:\\Users\\Rohan\\OneDrive\\Desktop\\Python\\Pokemon_data.csv.csv')
# print(df)
# to print bottom n number of rows
# print(df.tail(3))
# to print 1st n number of rows
# print(df.head(3))
# _xlsx=excel(for exel files)
#  Read Headers
# print(df.columns)

#  Read each Column
# print(df[['Name', 'Type 1', 'HP']])

#  Read Each Row
#  print(df.iloc[0:4])
#  for index, row in df.iterrows():
#     print(index, row['Name'])
# print(df.loc[df['Type 1'] == "Fire"])

# Read a specific location (R,C)
# print(df.iloc[3,2])
#df.sort_values(['Type 1', 'HP'], ascending=[1,0])
# in the above line sort_values is used for ascending and for decending (ascending =False).it will sort both the Type 1 and Hp .and 
# ascending=[1,0] is the 1st one i.e Type 1 is true(1) and Hp is fasle means in desending (0)

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# df = df.drop(columns=['Total'])

#print(df['Total'] = df.iloc[:, 4:10].sum(axis=1))

#cols = list(df.columns)
#prrint(df = df[cols[0:4] + [cols[-1]]+cols[4:12]])

#print(df.head(5))

#print(df.to_csv('modified.csv', index=False))

#print(df.to_excel('modified.xlsx', index=False))

#print(df.to_csv('modified.txt', index=False, sep='\t'))
