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

