

import pandas as pd


import seaborn as sns


import matplotlib.pyplot as plt


# Load Titanic dataset


titanic = sns.load_dataset('titanic')


# Data Cleaning

titanic['age'].fillna(titanic['age'].median(), inplace=True)  # Fill missing ages with median

titanic.dropna(subset=['embarked'], inplace=True)             # Drop rows where 'embarked' is missing



# Exploratory Data Analysis (EDA)




#  Age distribution




plt.figure(figsize=(8, 4))
sns.histplot(titanic['age'], bins=30, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()



# Survival count




plt.figure(figsize=(6, 4))
sns.countplot(x='survived', data=titanic)
plt.title('Survival Count (0 = No, 1 = Yes)')
plt.show()



#  Survival rate by gender



plt.figure(figsize=(6, 4))
sns.barplot(x='sex', y='survived', data=titanic)
plt.title('Survival Rate by Gender')
plt.show()


# Survival rate by passenger class


plt.figure(figsize=(6, 4))
sns.barplot(x='pclass', y='survived', data=titanic)
plt.title('Survival Rate by Passenger Class')
plt.show()


#  Age distribution by survival status



plt.figure(figsize=(8, 4))
sns.boxplot(x='survived', y='age', data=titanic)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Age')
plt.show()
