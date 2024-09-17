import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
file_path = '/Users/daxjulian/Desktop/MentalHealthSurvey.csv'  # Make sure this is the correct path to your file
data = pd.read_csv(file_path)



# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Optionally, fill or drop missing values
data.fillna(0, inplace=True)  # Replace missing values with 0 or use data.dropna() to remove rows with missing values

# Check for missing values
print(data.isnull().sum())

# Optionally, fill or drop missing values
data.fillna(0, inplace=True)  # Replace missing values with 0 or use data.dropna() to remove rows with missing values

# Summary of numerical data
print(data.describe())

# Check unique values in categorical columns
print(data['gender'].unique())

# Calculate average depression, anxiety, and isolation
avg_depression = data['depression'].mean()
avg_anxiety = data['anxiety'].mean()
avg_isolation = data['isolation'].mean()

print(f"Average Depression: {avg_depression}")
print(f"Average Anxiety: {avg_anxiety}")
print(f"Average Isolation: {avg_isolation}")

# Group by gender and calculate average mental health scores
gender_group = data.groupby('gender')[['depression', 'anxiety', 'isolation']].mean()

print(gender_group)



# Create a bar plot for mental health averages by gender
gender_group.plot(kind='bar')
plt.title('Average Mental Health Scores by Gender')
plt.ylabel('Score')
plt.show()


# Select only numerical columns
#numerical_data = data.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix on numerical data
#correlation_matrix = numerical_data.corr()

# Plot the heatmap
#plt.figure(figsize=(10, 8))
#sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
#plt.title('Correlation Heatmap')
#plt.show()

# Check for missing values and numerical columns
print(data.isnull().sum())
print(data.dtypes)

# Select only numerical columns
numerical_data = data.select_dtypes(include=['float64', 'int64'])
print(numerical_data.shape)  # Check if we have numerical data

# Drop missing values or handle them as needed
numerical_data = numerical_data.dropna()

# Calculate the correlation matrix
correlation_matrix = numerical_data.corr()

# Print the correlation matrix to ensure it's valid
print(correlation_matrix)

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()  # Ensure this is included

