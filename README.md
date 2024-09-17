# Mental-Health-Survey-Data-Analysis

## Project Overview
This project performs an analysis of a Mental Health Survey Dataset. The analysis includes:

- Handling missing data
- Summary statistics of numerical data
- Exploration of mental health scores (depression, anxiety, and isolation) by gender
- Visualization of the correlation between numerical variables using a heatmap

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Source](#data-source)
- [Results](#results)


## Dataset
The dataset contains the following relevant columns:

- gender: The gender of the survey respondents.
- depression: Self-reported depression score.
- anxiety: Self-reported anxiety score.
- isolation: Self-reported isolation score.

## Data Source
The dataset is provided as MentalHealthSurvey.csv. Kaggle : https://www.kaggle.com/datasets/abdullahashfaqvirk/student-mental-health-survey/data 

## Tools
- Python

## Features
### Data Cleaning: 
Detects and handles missing values by either filling them with zeros or dropping them.

### Exploratory Data Analysis (EDA):
- Calculates summary statistics (mean, median, etc.) for numerical columns such as depression, anxiety, and isolation.
- Identifies unique values for categorical columns like gender.
- Groups the data by gender to calculate average mental health scores.

## Visualization:
- Bar plot of average mental health scores (depression, anxiety, isolation) by gender.
- Correlation heatmap to visualize relationships between numerical features.

## Requirements
Before running the analysis, ensure that the following Python libraries are installed:
- pandas
- matplotlib
- seaborn

## Data Cleaning
- The code handles missing data by replacing them with 0 using data.fillna(0, inplace=True) or removing rows with missing values using data.dropna().

## Exploratory Data Analysis
- The describe() method is used to display summary statistics for the numerical data.
- Average mental health scores for depression, anxiety, and isolation are calculated for the entire dataset as well as by gender.

## Visualizations
- Bar Plot: Averages of depression, anxiety, and isolation scores by gender are plotted using a bar chart.
- Heatmap: A correlation heatmap visualizes relationships between numerical variables in the dataset.

## Example Code

#### Create a bar plot for mental health averages by gender
gender_group.plot(kind='bar')
plt.title('Average Mental Health Scores by Gender')
plt.ylabel('Score')
plt.show()

![Barchart](https://github.com/user-attachments/assets/68fdbcb9-56ec-414d-b000-ffc34a002b18)

#### Calculate and plot the correlation heatmap
correlation_matrix = numerical_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

![Heatmap _MH](https://github.com/user-attachments/assets/ef847d8d-97ef-414a-b440-6459839a76dc)

## Results
- Summary Statistics: Summary statistics for mental health metrics like depression, anxiety, and isolation are calculated.
- Mental Health by Gender: The bar plot shows average scores for each gender, giving insights into gender-based differences in mental health.
- Correlation Analysis: The heatmap provides insights into relationships between the numerical variables in the dataset.





