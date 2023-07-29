import pandas as pd

# Load data 
df = pd.read_csv('Employees.csv')

# 1- Remove duplicates
df = df.drop_duplicates()


# 2- Remove decimal places in the Age column
df["Age"] = df["Age"].astype(float).astype(int)

# 3- Convert USD salary to EGP
df["Salary(EGP)"] = (df["Salary(USD)"] * 30).astype(int)
# Drop the "Salary(USD)"
df.drop("Salary(USD)", axis=1, inplace=True)

# 4- Print stats
average_age = df["Age"].mean()
median_salary = df["Salary(EGP)"].median()
male_to_female_ratio = (df["Gender"].value_counts()["M"] / df["Gender"].value_counts()["F"]).round(2)

print("Average Age:", average_age)
print("Median Salary:", median_salary)
print("Male to Female Ratio:", male_to_female_ratio)

# 5-  Write the data to a new CSV file
df.to_csv("NewEmployeesFile.csv", index=False)