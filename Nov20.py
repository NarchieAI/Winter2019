# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#In order to complete this task you will need to use the following csv files:
#(a) "SPTSXComposite.csv" - TotalAssets
#(b) "SPTSXCap_Employees.csv" - NumberEmployees & MarketCapitalization
#(c) "SP_Transactions.csv" - Transaction variables - Make sure you explore before blindly joining with the above datasets. 
path = 'C:\\DeepLearningExercise\\'
df_composite = pd.read_csv(path+'SPTSXComposite.csv')
df_employees = pd.read_csv(path+'SPTSXCap_Employees.csv', usecols=['Ticker', 'NumberEmployees', 'MarketCapitalization'])
df_transactions = pd.read_csv(path+'SP_Transactions.csv')
# Index(['Date', 'Ticker', 'TransactionType', 'TransactionValue'], dtype='object')
df_employees = df_employees.drop_duplicates()


# 1. Create a DataFrame containing the following variables: Ticker, Total Assets, Number of Employees, Market Capitalization, Total Number of Transactions, Average Transaction Value (you will have to merge multiple datasets). (The location of each variable is detailed above.) Make sure you check the shape of your final dataset! (Hint: Duplicates)
#	Extra credit: Create a new variable (categorical) which labels the company as "Large" if all of Total Assets and Number of Employees is above the 75th percentile of the relevant variable, "Small" if all of Total Assets and Number of Employees is below the 25th percentile of the relevant variable and "Medium" otherwise. You may want to break this into multiple steps. 
df_data = pd.merge(df_composite[['Ticker', 'TotalAssets']], df_employees, on='Ticker', how='left')
df_transaction_count = df_transactions.groupby(['Ticker'])['Date'].count()
df_transaction_avgvalue = df_transactions.groupby(['Ticker'])['TransactionValue'].mean()
df_transaction_summary = pd.merge(df_transaction_count, df_transaction_avgvalue, on='Ticker', how='outer')
df_transaction_summary = df_transaction_summary.rename(columns={'Date': 'NumTransactions', 'TransactionValue': 'AvgTransactionValue'})
df_data = pd.merge(df_data, df_transaction_summary, on='Ticker', how='left')

# 2. Check the count, range, mean, median and standard deviation of each variable. Does everything look relatively reasonable?
for col_name in df_data.columns:
    print(df_data[col_name].describe())
# NumberEmployees: some public company has 34 employees, and some has 200k
# only have transaction data for 104 of the companies
    
# 3. Identify any rows/observations containing NaN or null values. Handle them as you see fit. Hint: If a company does not appear in the transactions dataset, it is because it closed no transactions during the relevant time period. 
#  Extra credit: Write the ticker number of any observations that were removed or altered to a txt or log file.  
# NumberEmployees, NumTransactions, AvgTransactionValue have missing values
df_data['NumberEmployees'] = df_data['NumberEmployees'].fillna(df_data['NumberEmployees'].median())
df_data.loc[df_data['NumTransactions'].isna(), 'AvgTransactionValue'] = 0
df_data['NumTransactions'] = df_data['NumTransactions'].fillna(0)

# 4. Consider the histogram of Market Capitalization. What does it tell you? 
#Extra credit: Consider and apply an appropriate transformation to the Market Capitalization variable. Plot the histograms of the remaining variables and consider if a transformation should be applied to any explanatory variables before further analysis.
df_data['MarketCapitalization'].plot.hist()
# right-skewed, some mega-companies in the 140k range, while nothing in the 120k range

# 5. Explore the relationships between Market Capitalization and the other variables using scatter plots and a correlation matrix. Are the relationships strong or weak, positive or negative, linear or not? 
#  Extra credit: Add an appropriate title and y and x axis labels to your scatter plots. Use string formatting so that you don't have to manually assign 
df_data = df_data.set_index('Ticker')
for col_name in df_data.columns:
    if col_name != 'MarketCapitalization':
        df_data.plot.scatter(col_name, 'MarketCapitalization')
        str_log = col_name + '_log'
        df_data[str_log] = np.log(df_data[col_name])
        df_data.plot.scatter(str_log, 'MarketCapitalization')
print(df_data.corr()['MarketCapitalization'])
# the market cap potential (max possible) is approximately linearly increasing with the log of the variables
        
# 6. Look up another way or other ways to analyze/understand your data visually and create the relevant plot using matplotlib or seaborn. (Suggestions: Boxplot, violin plot, correlation heatmap.)
#  Extra credit: Visually assess differences between large, small and medium companies using the variable created in extra credit section of step 1. 
df_standardized = (df_data - df_data.mean()) / df_data.std()
sns.heatmap(df_standardized)

# 7. Answer the question, "how does market capitalization differ by sector?"
df_data_wsector = pd.merge(df_data, df_composite[['Ticker', 'PrimarySector']], on='Ticker', how='left')
print(df_data_wsector.head())
plt.figure()
sns.boxplot(x='PrimarySector', y='MarketCapitalization', data=df_data_wsector)
#for sector in df_data_wsector.PrimarySector.unique():
#    df_sector = df_data_wsector.loc[df_data_wsector['PrimarySector']==sector]
#    df_sector['MarketCapitalization'].plot.hist()
#    plt.title(sector)
#    plt.show()

# 8. Save the cleaned DataFrame as a csv or excel file (df.to_csv(path) or df.to_excel(path)). (Create a new directory for your outputs/reports)
df_data.to_csv(path+'SPTSX_Combined.csv')

# 7. Extra credit: Go back over your code, if you have not defined any functions, refactor your code to include at least one function.  Put your functions in a separate .py file and import it as a module. 
#	Extra, extra credit: Create a package containing your functions file so that you can use the functions for other projects.

# 9. Commit your code to git
