import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the final merged dataset
merged_df = pd.read_csv('Data/Final_Dataset.csv')

# Group by 'Category' and sum the scores for each category
category_scores = merged_df.groupby('Category')['Score'].sum().reset_index(name='Total Score')

# Sort the categories by total score in descending order and get the top 5 categories
top_5_categories = category_scores.sort_values(by='Total Score', ascending=False).head(5)

# Plot a bar chart for "Top 5 categories by aggregate popularity"
plt.figure(figsize=(10, 6))
sns.barplot(x='Total Score', y='Category', data=top_5_categories, palette='viridis')
plt.title('Top 5 Categories by Aggregate Popularity')
plt.xlabel('Total Score')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# Calculate the total popularity score of top 5 categories for the pie chart
top_5_total_score = top_5_categories['Total Score'].sum()

# Calculate the percentage share for each category
top_5_categories['Percentage Share'] = (top_5_categories['Total Score'] / top_5_total_score) * 100

# Plot a pie chart for "Popularity Percentage Share from Top 5 Categories"
plt.figure(figsize=(8, 8))
plt.pie(top_5_categories['Total Score'], labels=top_5_categories['Category'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Popularity Percentage Share from Top 5 Categories')
plt.show()
