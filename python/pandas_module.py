# # pandas  ==> 
# 'series data structure '
# # in series datastructure we can give indexing position like a,b,c instead of 0,1,2,3.....
# import pandas
# # s_ds=pandas.Series(['ajay',101,'ajay@gmail.com'],index=['a','b','c'])
# # print(s_ds)
# # print(s_ds[1])
# # # print(s_ds[c]) error 

# # df=pandas.DataFrame([101,'mohan',84,65,95],columns=['std_id','std_name','maths','telugu','hindi'])
# # print(df)
# df1= pandas.DataFrame({
#     'std_id':[101,102,103,104,105],
#     'std_name':['sai','ravi','ajay','ram','sita'],
#     'maths':[45,85,67,92,87],
#     'telugu':[65,48,97,67,75],
#     'hindi':[74,87,94,92,88]
# })
# print(df1)

# df1['total']=df1['maths']+df1['telugu']+df1['hindi']
# print(df1)
# df1.to_excel("abc.xlsx")
# # # how to drop a column
# df1.drop('total',axis=1,inplace=True)
# print(df1)

# # how to drop a row
# df1.drop(0,axis=0,inplace=True)
# print(df1)


# # # how to call a particular column
# print(df1['std_name'])


# # viewing the data---functions and attributes
# # # --------------------
# # # how to call first 3 rows
# print(df1.head(3))
# print(df1.head())


# # # how to call last 3 rows
# print(df1.tail(3))


# # ho to shape of the data
# print(df1.shape)


# # how to know no of columns
# print(df1.columns)


# # info
# print(df1.info())


# # describe
# print(df1.describe())




# # loc
# # to print a particular cell
# print(df1.loc[2,'std_name'])


# # to print a particular row and all columns
# print("particular row and all columns")
# print(df1.loc[2,:])


# # to print a particular row and particular columns
# print("particular row and particular columns")
# print(df1.loc[2,['std_name','maths']])



# # multiple rows and single column
# print("multiple rows and single column")
# print(df1.loc[[0,2,4],'std_name'])



# # multiple rows and multiple columns
# print("multiple rows and multiple columns")
# print(df1.loc[[0,2,4],['std_name','maths']])


# # multiple rows and all columns
# print("multiple rows and all columns")
# print(df1.loc[[0,2,4],:])


# # update the value of a cell
# print("update the value of a cell")
# df1.loc[2,'std_name']='ajay kumar'
# print(df1)


# # change the values of entire column
# print("change the values of entire column")
# df1['std_name']=['sai krishna','ravi kumar','ajay kumar','ram kumar','sita devi']
# print(df1)


# # range of rows and columns
# print("range of rows and columns")
# print(df1.loc[0:3,'std_name':'maths'])


# # total rows and single column
# print("total rows and single column")
# print(df1.loc[:,'std_name'])


# # total rows and multiple columns
# print("total rows and multiple columns")
# print(df1.loc[:,['std_name','maths']])


# # select rows based on condition
# print("select rows based on condition")
# print(df1.loc[df1['maths']>80])


# # select rows based on multiple conditions
# print("select rows based on multiple conditions")
# print(df1.loc[(df1['maths']>80) & (df1['telugu']>80)])


# # select records starting with a particular letter
# print("select records starting with a particular letter")
# print(df1.loc[df1['std_name'].str.startswith('s')],['std_name','maths'])


# # select records ending with a particular letter
# print("select records ending with a particular letter")
# print(df1.loc[df1['std_name'].str.endswith('i')],['std_name','maths'])


# # iloc
# print('----------------------iloc-----------------------------')
# # iloc is used to access the data based on integer position
# # iloc[row_index,column_index] 
# # row_index can be a single integer, a list of integers, or a range of integers
# # column_index can also be a single integer, a list of integers, or a range of integers

# # to print a particular cell
# print(df1.iloc[2,1])


# # to print a particular row and all columns
# print("particular row and all columns")
# print(df1.iloc[2,:])


# # to print a particular row and particular columns
# print("particular row and particular columns")
# print(df1.iloc[2,[1,3]])


# # multiple rows and single column
# print("multiple rows and single column")
# print(df1.iloc[[0,2,4],1])


# # multiple rows and multiple columns
# print("multiple rows and multiple columns")
# print(df1.iloc[[0,2,4],[1,3]])


# # multiple rows and all columns
# print("multiple rows and all columns")
# print(df1.iloc[[0,2,4],:])


# # update the value of a cell
# print("update the value of a cell")
# df1.iloc[2,1]='ajay kumar'
# print(df1)


# # change the values of entire column
# print("change the values of entire column")
# df1.iloc[:,1]=['sai krishna','ravi kumar','ajay kumar','ram kumar','sita devi']
# print(df1)


# # range of rows and columns
# print("range of rows and columns")
# print(df1.iloc[0:3,1:4])


# # sort values in ascending order
# print("sort values in ascending order")
# print(df1.sort_values('maths'))#ascending order is default / ascending=True


# # sort values in descending order
# print("sort values in descending order")
# print(df1.sort_values('maths',ascending=False))


# 19-02-2025
import pandas as pd
df3 = pd.DataFrame({
    'emp_id':[101,102,103,104,105],
    'emp_name':['sai','ravi','ajay','ram','sita'],
    'salary':[45000,85000,67000,92000,87000],
})
print(df3['salary'].max())
print(df3['salary'].min())
print(df3['salary'].mean())
print(df3['salary'].sum())
print(df3['salary'].std())

read=pd.read_excel('emp_details.xlsx')

# print(read)

# print(read.isnull())
h=pd.DataFrame(read)

# h['Emp Name'].fillna('Afroz',inplace=True)
# h['Emp ID'].fillna('E017',inplace=True)
# h['Salary'].fillna('30000',inplace=True)
# h['Age'].fillna('22',inplace=True)
# h['Dept'].fillna('Sales',inplace=True)

h['Emp Name'] = h['Emp Name'].fillna('Afroz')
h['Emp ID']   = h['Emp ID'].fillna('E017')
h['Salary']   = h['Salary'].fillna(30000)   # numeric
h['Age']      = h['Age'].fillna(22)         # numeric
h['Dept']     = h['Dept'].fillna('Sales')
print(read)