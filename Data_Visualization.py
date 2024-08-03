import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the final merged dataset
merged_df = pd.read_csv('Data/Final_Dataset.csv')

# Set the style for seaborn
sns.set(style="whitegrid")

# 1. How many unique categories are there?
unique_categories_count = merged_df['Category'].nunique()
print(f"Number of unique categories: {unique_categories_count}")

# Plot the number of unique categories
plt.figure(figsize=(8, 6))
sns.countplot(data=merged_df, y='Category', order=merged_df['Category'].value_counts().index)
plt.title(f'Unique Categories (Total: {unique_categories_count})')
plt.xlabel('Number of Posts')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# 2. How many reactions are there to the most popular category?
most_popular_category = merged_df['Category'].value_counts().idxmax()
most_popular_category_reactions = merged_df[merged_df['Category'] == most_popular_category].shape[0]
print(f"Most popular category: {most_popular_category} with {most_popular_category_reactions} reactions")

# Plot the reactions to the most popular category
plt.figure(figsize=(8, 6))
sns.countplot(x='Category', data=merged_df[merged_df['Category'] == most_popular_category])
plt.title(f'Reactions to the Most Popular Category: {most_popular_category}')
plt.xlabel('Category')
plt.ylabel('Number of Reactions')
plt.tight_layout()
plt.show()

# 3. What was the month with the most posts?
# Assuming there's a 'Post Date' column in 'YYYY-MM-DD' format in the merged_df
merged_df['Post Date'] = pd.to_datetime(merged_df['Post Date'])
merged_df['Month'] = merged_df['Post Date'].dt.to_period('M')
month_with_most_posts = merged_df['Month'].value_counts().idxmax()
most_posts_count = merged_df['Month'].value_counts().max()
print(f"Month with the most posts: {month_with_most_posts} ({most_posts_count} posts)")

# Plot the number of posts per month
plt.figure(figsize=(12, 6))
sns.countplot(x='Month', data=merged_df, order=merged_df['Month'].value_counts().index)
plt.title('Number of Posts by Month')
plt.xlabel('Month')
plt.ylabel('Number of Posts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
