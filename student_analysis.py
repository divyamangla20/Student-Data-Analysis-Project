import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the CSV file
df = pd.read_csv("students.csv")


# Print the complete DataFrame
print(df)


print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Marks with 0
df["Marks"] = df["Marks"].fillna(0)

print("\nDataset After Cleaning:")
print(df)


# Add Grade column
df["Grade"] = "D"

df.loc[df["Marks"] >= 90, "Grade"] = "A"
df.loc[(df["Marks"] >= 80) & (df["Marks"] < 90), "Grade"] = "B"

print("\nDataset with Grades:")
print(df)


# Find the topper
topper = df[df["Marks"] == df["Marks"].max()]

print("\nTopper:")
print(topper)


df.to_csv("clean_students.csv", index=False)

print("Dataset saved successfully!")

os.makedirs("charts", exist_ok=True)

# Grade Distribution Bar Chart
plt.figure(figsize=(6, 4))

df["Grade"].value_counts().plot(kind="bar")

plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")

plt.savefig("charts/grade_distribution.png")

plt.close()