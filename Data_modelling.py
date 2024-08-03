import pandas as pd

# Load the cleaned datasets
content_df_cleaned = pd.read_csv('Data/Content_Cleaned.csv').drop(columns=['Unnamed: 0'], errors='ignore')
reactions_df_cleaned = pd.read_csv('Data/Reactions_Cleaned.csv').drop(columns=['Unnamed: 0'], errors='ignore')
reaction_types_df_cleaned = pd.read_csv('Data/ReactionTypes_Cleaned.csv').drop(columns=['Unnamed: 0'], errors='ignore')

# Merge datasets
# First, merge Reactions with Content on 'Content ID'
merged_df = reactions_df_cleaned.merge(content_df_cleaned, on='Content ID', how='left')

# Then, merge the result with ReactionTypes on 'Reaction Type'
final_df = merged_df.merge(reaction_types_df_cleaned, on='Reaction Type', how='left')

# Calculate total scores for each category
category_scores = final_df.groupby('Category')['Score'].sum().reset_index()

# Get the top 5 performing categories
top_5_categories = category_scores.nlargest(5, 'Score')

# Save the final cleaned dataset with top 5 categories
final_df.to_csv('Data/Final_Dataset.csv', index=False)
top_5_categories.to_csv('Data/Top_5_Categories.csv', index=False)

# Print the results
print("Final merged dataset saved as 'Final_Dataset.csv'")
print("Top 5 performing categories saved as 'Top_5_Categories.csv'")
