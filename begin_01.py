# ============================================================
# Python basics
# ============================================================

print("\n========== PYTHON FUNCTIONS ==========\n")


# Define a function with a parameter.
def hello(name):
    print("hello world " + name)


# Call the function and pass user input as the argument.
hello(input("Enter Name: "))


# Define a function without parameters.
def hello1():
    # Store user input in a variable.
    name = input("Enter Name: ")
    print("hello world " + name)


# Call the function.
hello1()


# ============================================================
# Imports
# ============================================================

print("\n========== IMPORTS ==========\n")

import pandas as pd
import polars as pl
import matplotlib as mpl
import matplotlib.pyplot as plt


# ============================================================
# Read CSV
# ============================================================

print("\n========== READ CSV / DATAFRAME ==========\n")

# Read the CSV file into a pandas DataFrame.
df = pd.read_csv("insurance.csv")

# Show the first 5 rows.
print("\n--- First 5 Rows ---")
print(df.head())

# Check the type of object.
print("\n--- DataFrame Type ---")
print(type(df))

# Show the data type of every column.
print("\n--- Data Types ---")
print(df.dtypes)

# Show DataFrame structure and column information.
print("\n--- DataFrame Info ---")
df.info()

# Get the total number of rows.
print("\n--- Total Rows ---")
print(df.shape[0])

# Get the column labels.
columns_df = df.columns

# Select column labels by position.
print("\n--- Column Labels ---")
print(columns_df[range(len(columns_df))])


# ============================================================
# loc / iloc
# ============================================================

print("\n========== LOC / ILOC ==========\n")

# loc selects using index/column labels.
print("\n--- df.loc[0] : Row by Index Label ---")
print(df.loc[0])

# iloc selects using row/column positions.
print("\n--- df.iloc[43, 0] : Row/Column by Position ---")
print(df.iloc[43, 0])


# ============================================================
# groupby
# ============================================================

print("\n========== GROUPBY ==========\n")

# Group rows by sex and region.
group_by_age = df.groupby(["sex", "region"])

print("\n--- Grouped by Sex and Region ---")
print(group_by_age)

# Select age and bmi from the grouped data.
group_by_age1 = group_by_age[["age", "bmi"]]

print("\n--- Selected Columns: age, bmi ---")
print(group_by_age1)

# Calculate the mean for each group.
group_by_age_aggregate = group_by_age1.mean()

print("\n--- Mean Age and BMI by Sex and Region ---")
print(group_by_age_aggregate)

# Same operation written in one line.
# df.groupby(["sex", "region"])[["age", "bmi"]].mean()


# ============================================================
# matplotlib
# ============================================================

print("\n========== MATPLOTLIB ==========\n")

# Calculate average insurance charges for each region.
# global_insurance_charges = df.groupby("region")["charges"].mean()

# Plot the result.
# global_insurance_charges.plot()

# Display the plot.
# plt.show()

print("Plotting code is currently commented out.")


# ============================================================
# Basic [] subsetting
# ============================================================

print("\n========== BASIC [] SUBSETTING ==========\n")

# Select the "age" column.
# Returns a pandas Series.
df_age1 = df["age"]

print("\n--- df['age'] : Select Column ---")
print(df_age1)

# Select rows 0 through 4.
df_age3 = df[0:5]

print("\n--- df[0:5] : Select Rows 0-4 ---")
print(df_age3)

# df[2]
# Attempts to select a column whose label is 2.

# df["age":5]
# Invalid syntax for DataFrame selection.


# ============================================================
# Python list vs pandas Series
# ============================================================

print("\n========== PYTHON LIST vs PANDAS SERIES ==========\n")

# This is a normal Python list.
series = ["age", "bmi"]

print("\n--- Python List ---")
print(series)
print(type(series))

# Select position 0 from the Python list.
print("\n--- series[0] ---")
print(series[0])

# Select positions 0 up to, but not including, 2.
print("\n--- series[0:2] ---")
print(series[0:2])


# Create a pandas Series with custom index labels.
pdseries1 = pd.Series(["age", "bmi"], index=["ageindex", "bmiindex"])

print("\n--- Pandas Series with Custom Index ---")
print(pdseries1)

print("\n--- Pandas Series Type ---")
print(type(pdseries1))


# ============================================================
# Python containers
# ============================================================

print("\n========== PYTHON CONTAINERS ==========\n")

# List: ordered and mutable.
age = [20, 30, 40]

# Tuple: ordered and immutable.
age_tuple = (20, 30, 40)

# Dictionary: key-value pairs.
data = {"age": [20, 30, 40], "bmi": [22.1, 25.4, 28.2]}

# Set: unique values.
age_set = {20, 30, 40}

print("\n--- List ---")
print(age)

print("\n--- Tuple ---")
print(age_tuple)

print("\n--- Dictionary ---")
print(data)

print("\n--- Set ---")
print(age_set)


# ============================================================
# List indexing
# ============================================================

print("\n========== LIST INDEXING ==========\n")

# Get the first value from a list.
print("\n--- age[0] ---")
print(age[0])

# Get values from position 0 up to, but not including, 2.
print("\n--- age[0:2] ---")
print(age[0:2])


# ============================================================
# Dictionary indexing
# ============================================================

print("\n========== DICTIONARY INDEXING ==========\n")

# Get the value stored under the "age" key.
print("\n--- data['age'] ---")
print(data["age"])

# Get position 1 from the list stored under "age".
print("\n--- data['age'][1] ---")
print(data["age"][1])


# ============================================================
# for loop
# ============================================================

print("\n========== FOR LOOP ==========\n")

# Iterate through the values of a list.
print("\n--- Iterate Through List ---")
for x in age:
    print(x)

# Iterate through dictionary keys.
print("\n--- Iterate Through Dictionary Keys ---")
for x in data:
    print(x)

# Iterate through dictionary key-value pairs.
print("\n--- Iterate Through Dictionary Items ---")
for key, value in data.items():
    print(key, value)


# ============================================================
# range
# ============================================================

print("\n========== RANGE ==========\n")

# Generates 0, 1, 2, 3, 4.
print("\n--- range(5) ---")
for x in range(5):
    print(x)

# Generates 2, 3, 4.
print("\n--- range(2, 5) ---")
for x in range(2, 5):
    print(x)

# Generates 0, 2, 4.
print("\n--- range(0, 5, 2) ---")
for x in range(0, 5, 2):
    print(x)


# ============================================================
# enumerate
# ============================================================

print("\n========== ENUMERATE ==========\n")

# Gives both the position and the value.
for position, value in enumerate(age):
    print("Position:", position, "| Value:", value)


# ============================================================
# Iterable examples
# ============================================================

print("\n========== ITERABLES ==========\n")

# A string is iterable character by character.
print("\n--- Iterate Through String ---")
for x in "RAVI":
    print(x)

# An integer is not iterable.
# for x in 100:
#     print(x)


# ============================================================
# Tuple created by comma
# ============================================================

print("\n========== TUPLE CREATED BY COMMA ==========\n")

# The comma creates the tuple.
a = 19, 20

print("\n--- a ---")
print(a)

print("\n--- Iterate Through Tuple ---")
for x in a:
    print(x)


# ============================================================
# DataFrame creation
# ============================================================

print("\n========== DATAFRAME CREATION ==========\n")


# ------------------------------------------------------------
# List of lists
# ------------------------------------------------------------

print("\n--- LIST OF LISTS ---\n")

# List of lists can be converted into a DataFrame.
list_data = [[20, 22.1], [30, 25.4], [40, 28.2]]

print("Original list_data:")
print(list_data)

print("\nDataFrame without column names:")
df_from_lists = pd.DataFrame(list_data)
print(df_from_lists)

# Without columns=, pandas automatically uses numerical
# column labels: 0, 1, ...

print("\nDataFrame with column names:")
df_from_lists = pd.DataFrame(list_data, columns=["age", "bmi"])
print(df_from_lists)

# columns= supplies the column labels because the
# list of lists does not contain column names.


# ------------------------------------------------------------
# Dictionary of lists
# ------------------------------------------------------------

print("\n--- DICTIONARY OF LISTS ---\n")

# Dictionary keys become the DataFrame column labels.
dict_data = {"age": [20, 30, 40], "bmi": [22.1, 25.4, 28.2]}

print("Original dictionary:")
print(dict_data)

print("\nDataFrame from dictionary:")
df_from_dict = pd.DataFrame(dict_data)
print(df_from_dict)

# The dictionary keys already provide the column names.


# ------------------------------------------------------------
# Dictionary + columns=
# ------------------------------------------------------------

print("\n--- DICTIONARY + columns= ---\n")

# columns= selects/reorders the dictionary columns.
df_from_dict_selected = pd.DataFrame(dict_data, columns=["bmi"])

print(df_from_dict_selected)


# ------------------------------------------------------------
# Dictionary + index=
# ------------------------------------------------------------

print("\n--- DICTIONARY + index= ---\n")

# index= assigns row labels.
df_from_dict_indexed = pd.DataFrame(dict_data, index=["row1", "row2", "row3"])

print(df_from_dict_indexed)


# ------------------------------------------------------------
# Dictionary + columns= + index=
# ------------------------------------------------------------

print("\n--- DICTIONARY + columns= + index= ---\n")

# columns= selects columns.
# index= assigns row labels.
df_from_dict_both = pd.DataFrame(
    dict_data, columns=["bmi", "age"], index=["row1", "row2", "row3"]
)

print(df_from_dict_both)


# ============================================================
# DataFrame column -> Series
# ============================================================

# print("\n========== DATAFRAME COLUMN -> SERIES ==========\n")

# Selecting one DataFrame column returns a pandas Series.
age_series = df["age"]

print("\n--- df['age'] ---")
print(age_series)

# Check that it is a Series.
print("\n--- Type of df['age'] ---")
print(type(age_series))


check_bool_vectors = age_series[age_series > age_series.mean()]
print(check_bool_vectors)

manual_bool_value = [True, False]
print(age_series[manual_bool_value])

for manual in manual_bool_value:
    print(age_series[manual])
