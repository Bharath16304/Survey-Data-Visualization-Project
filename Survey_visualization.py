import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('survey_data.csv')  # columns: question_1, question_2, rating_1, rating_2, etc.

# Bar Chart Example
df['question_1'].value_counts().plot(kind='bar', title='Survey Question 1 Responses')
plt.show()

# Pie Chart Example
df['question_2'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Survey Question 2 Distribution')
plt.show()

# Heatmap for Ratings
sns.heatmap(df[['rating_1', 'rating_2']].corr(), annot=True)
plt.title('Ratings Correlation Heatmap')
plt.show()
