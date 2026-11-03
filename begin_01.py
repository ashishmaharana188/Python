# def hello(name):
#    print("hello world " + name)


# hello(input("Enter Name: "))


# def hello1():
#    name = input("Enter Name: ")
#    print("hello world " + name)


# hello1()


import pandas as pd
import polars as pl


df = pd.read_csv("insurance.csv")
print("Select Dataframe all data:\n\n", df.head())  # select first 5 rows
print(type(df))  # check type
print("Data Types:\n\n", df.dtypes)  # column column name and type
print("Rows DataTypes columns and Index:\n")
df.info()
print("Total Rows::\n\n", df.shape[0])

columns_df = df.columns
print(columns_df[range(len(columns_df))])

print(columns_df.loc[0])
