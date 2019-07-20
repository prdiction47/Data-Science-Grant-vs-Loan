# Resources
# Libraries - https://medium.com/activewizards-machine-learning-company/top-20-python-libraries-for-data-science-in-2018-2ae7d1db8049
# The Data - https://collegescorecard.ed.gov/data/
# Learning Repos - https://archive.ics.uci.edu/ml/datasets.php

import pandas as pd
import matplotlib.pyplot as plt

student_data_url = 'https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv'
student_data = pd.read_csv(student_data_url)

#!curl 'https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv' #csv (comma separated value)

student_data.head()
student_data.isnull().sum()

x = student_data.PCTPELL.dropna()
y = student_data.PCTFLOAN.dropna()
plt.scatter(x,y)
plt.title ('Students with Pell vs Students with Fed Loan')
plt.xlabel('% Student with Pell')
plt.ylabel('% Student with F Loan')
plt.show()

plt.hist(x)
plt.show()

import seaborn as sns
sns.distplot(x)
sns.distplot(y)
