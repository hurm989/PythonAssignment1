import pandas as pd

# df=pd.read_csv('./file.csv')

# Write a Pandas program to get the first 3 rows of a given DataFrame.
# print(df.head(3))

# Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
# print(df.loc[:,["name","score"]])

# Write a Pandas program to select the specified columns and rows from a given data frame using loc and iloc.
# print(df.loc[[0,1],"name"])
# print(df.iloc[[0,1],[0]])

# Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
# print(df.loc[df["attempts"]>2])

# Write a Pandas program to count the number of rows and columns of a DataFrame.
# num_rows, num_columns = df.shape
# print(num_rows,num_columns)

#  Write a Pandas program to select the rows where the score is missing
# print(df[df['score'].isna()])


# Write a Pandas program to select the rows the score is between 15 and 20
# print(df.loc[ (df['score']>15) & (df['score']<20)] )

# Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
# print(df.loc[(df['attempts']<2) & (df['score']>15)])

# Write a Pandas program to change the score in row 'd' to 11.5.
# df.at[3, 'score'] = 11.5
# print(df)

# Write a Pandas program to calculate the sum of the examination attempts by the students.
# print(df["score"].sum())

# Write a Pandas program to calculate the mean of all students' scores
# print(df['score'].mean())

# Write a Pandas program to append a new row to data frame with given values for each column. Now delete the new row


# Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
# df.sort_values(by=['name','score'],ascending=[False,True],inplace=True)
# print(df)

# Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
# df['qualify'] = df['qualify'].replace({'yes': True, 'no': False})
# print(df)

# Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.
# df.loc[df['name'] == 'James', 'name'] = 'Suresh'
# print(df)

# Write a Pandas program to delete the 'attempts' column from the DataFrame.
# df.drop(columns=['attempts'])
# print(df)

# Write a Pandas program to insert a new column in existing DataFrame.
# my_col = ['A1', 'A2', 'A3', 'A4', 'A5','A1', 'A2', 'A3', 'A4', 'A5']
# df['col'] = my_col
# print(df)

# Write a Pandas program to iterate over rows in a DataFrame.
# for index, row in df.iterrows():
#     print(index,row)

# Display all columns
# print(df.columns.tolist())

# Rename Column
# df.rename(columns={'name': 'Name'},inplace=True)
# print(df)

# Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.
# df['score'] = df['score'].fillna(0)
# print(df)

# Drop multiple columns
# df.drop(columns=["name","score"],inplace=True)
# print(df)

# Drop rows and then reset the index
# df = df[df['attempts'] == 1]
# df = df.reset_index(drop=True)
# print(df)

# =======================================================================================
# df=pd.read_csv('./data.csv')
# Write a Pandas program to remove the duplicates from 'WHO region' column of World alcohol consumption dataset.

# Write a Pandas program to find out the alcohol consumption details in the year '1987' or '1989' from the world alcohol consumption dataset.
# df = df[(df['Year'] == 1987) | (df['Year'] == 1989)]
# print(df)

# Write a Pandas program to find out the alcohol consumption details by the 'Americas' in the year '1985' from the world alcohol consumption dataset.
# df = df[(df['Year'] == 1985)]
# print(df)

# Write a Pandas program to find out the alcohol consumption details in the year '1986' where WHO region is 'Western Pacific' and country is 'VietNam' from the world alcohol consumption dataset.
# df = df[(df['Year'] == 1986) & (df['WHO region'] == "Western Pacific") & (df['Country'] == "Viet Nam")]
# print(df)

# Write a Pandas program to find out the alcohol consumption details in the year '1986' or '1989' where WHO region is 'Americas' from the world alcohol consumption dataset.
# df = df[((df['Year'] == 1986) | (df['Year'] == 1989)) & (df['WHO region'] == "Americas")]
# print(df)

# Write a Pandas program to find out the alcohol consumption details in the year '1986' or '1989' where WHO region is 'Americas' or 'Europe' from the world alcohol consumption dataset.
# df = df[((df['Year'] == 1986) | (df['Year'] == 1989)) & ((df['WHO region'] == "Americas") | (df['WHO region'] == "Europe"))]
# print(df)

# Write a Pandas program to filter those records where WHO region contains "Ea" substring from world alcohol consumption dataset.
# df = df[df['WHO region'].str.contains("Ea", case=False)]
# print(df)

# Write a Pandas program to filter those records where WHO region matches with multiple values (Africa, Eastern Mediterranean, Europe) from world alcohol consumption dataset.
# regions = ['Africa', 'Eastern Mediterranean', 'Europe']
# df = df[df['WHO region'].isin(regions)]
# print(df)

# Write a Pandas program to filter those records which not appears in a given list from world alcohol consumption dataset.
# regions = ['Africa', 'Eastern Mediterranean', 'Europe']
# df = df[~df['WHO region'].isin(regions)]
# print(df)

# ===================================================================================

# df=pd.read_csv('./school_data.csv')
# findout how many schools we have in the file
# df=df['school_code'].nunique()
# print(df)

# find out the number of class we have in each school
# df=df.groupby('school_code')['class'].nunique().reset_index()
# print(df)

# find out the avg, min and max age of students of each school.
# stats = df.groupby('school_code')['age'].agg(['mean', 'min', 'max']).reset_index()
# print(stats)


# ===================================================================================

df=pd.read_csv('./sales-data.csv')

# How much sale produced by each salesman
# df=df.groupby('SalesRep')['Revenue'].sum().reset_index()
# print(df)

# which salesman produced the best sale
# sales = df.groupby('SalesRep')['Revenue'].sum().reset_index()
# saleman =sales[sales['Revenue'] == sales['Revenue'].max()]
# print(saleman)

# Display sale of each month 
# df['Date'] = pd.to_datetime(df['Date'])
# print(df)
# sales_by_month = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Revenue'].sum().reset_index()
# print(sales_by_month)

# find out the best month of sale

# in which region we got the best sale
# sales = df.groupby('Region')['Revenue'].sum().reset_index()
# best_region = sales[sales['Revenue'] == sales['Revenue'].max()]
# print(best_region)

# what product sold the most
# product = df.groupby('Product')['Units'].sum().reset_index()
# most_sold = product[product['Units'] == product['Units'].max()]
# print(most_sold)