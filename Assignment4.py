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
              By default, the copy is a "deep copy" meaning that any changes made in the original DataFrame will NOT be reflected in the copy.  '''


''' Ans Q16 - The loc function in pandas can be used to access groups of rows or columns by label.
              Add each condition you want to be included in the filtered result and concatenate them with the & operator .
              Syntex :- dataFrame.loc[(dataFrame['column_name']>=100000) & (dataFrame['column_name']< 40) & (dataFrame['column_name'].str.startswith('D')),
                    ['column_name','JOB']]  '''

''' Ans Q17 - To get column average or mean from pandas DataFrame use either mean() and describe() method. The DataFrame. mean() method is used to return the mean of the values for the requested axis.   '''

''' Ans Q18 - Standard deviation is calculated using the function . std() . However, the Pandas library creates the Dataframe object and then the function . std() is applied on that Dataframe .   '''

''' Ans Q19 - By using corr() function we can get the correlation between two columns in the dataframe.
              Syntex :- dataframe[‘first_column’].corr(dataframe[‘second_column’]). '''


''' Ans Q20 - The most basic way to select a single column from a dataframe, just put the string name of the column in brackets.     '''

''' Ans Q21 - If you'd like to select rows based on integer indexing, you can use the . iloc function. If you'd like to select rows based on label indexing, you can use the . loc function. '''

''' Ans Q22 - To sort the DataFrame based on the values in a single column, you'll use . sort_values() . By default, this will return a new DataFrame sorted in ascending order. It does not modify the original DataFrame. '''

''' Ans Q23 - you can  create a new column in a DataFrame based on the values of another column using apply() method .  '''

''' Ans Q24 - The drop_duplicates() method removes duplicate rows. Use the subset parameter if only some specified columns should be considered when looking for duplicates.  '''

''' Ans Q25 - The main distinction between loc and iloc is: loc is label-based, which means that you have to specify rows and columns based on their row and column labels. 
              iloc is integer position-based, so you have to specify rows and columns by their integer position values (0-based integer position).  '''

