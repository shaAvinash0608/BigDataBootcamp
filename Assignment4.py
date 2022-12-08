''' Ans Q1 - import pandas as pd
           df = pd.read_csv('data.csv')
           print(df.to_string()'''

''' Ans Q2 - To check the data type of all columns in Pandas DataFrame you can use this command  df.dtypes .
             To check the data type of a particular column in Pandas DataFrame you can use this command  df['DataFrame Column'].dtypes .  '''

''' Ans Q3 - you select rows from a Pandas DataFrame based on a condition using these method 
             Boolean Indexing method.
             Positional indexing method.
             Using isin() method.
             Using Numpy. where() method.
             Comparison with other methods.       '''

''' Ans Q4 - We can rename the columns in a Pandas Dataframe is by using the rename() function.         '''

''' Ans Q5 - The drop() method removes the specified row or column.
             By specifying the column axis (axis='columns'), the drop() method removes the specified column.
             By specifying the row axis (axis='index'), the drop() method removes the specified row.
             syntex - dataframe.drop(labels, axis, index, columns, level, inplace., errors).   '''


''' Ans Q6 - df.(column_name).unique()    '''

''' Ans Q7 - df['column name'].isna().sum().  '''

''' Ans Q8 - The fillna() function iterates through your dataset and fills all empty rows with a specified value. '''

''' Ans Q9 - We can concatenate two Pandas DataFrames using concat and append method.  '''

''' Ans Q10 - We can merge two Pandas DataFrames on certain columns using the merge function by simply specifying the certain columns for merge. 
              Syntax: DataFrame.merge(right, how=’inner’, on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, copy=True, indicator=False, validate=None) '''


''' Ans Q11 - df.groupby(df["column_name"]).column_name.agg(["min","max","sum","count","mean"]) '''

''' Ans Q12 - The pivot() function is used to reshaped a given DataFrame organized by given index / column values. This function does not support data aggregation, multiple values will result in a MultiIndex in the columns.
              syntex - DataFrame.pivot(self, index=None, columns=None, values=None)   '''


''' Ans Q13 - The best way to convert one or more columns of a DataFrame to numeric values is to use pandas.to_numeric() . This function will try to change non-numeric objects (such as strings) into integers or floating-point numbers as appropriate. '''

''' Ans Q14 - Use sort_values to sort the df by a specific column's values stntex :- df.sort_values('column_name'). '''

''' Ans Q15 - The copy() method returns a copy of the DataFrame.

By default, the copy is a "deep copy" meaning that any changes made in the original DataFrame will NOT be reflected in the copy.
