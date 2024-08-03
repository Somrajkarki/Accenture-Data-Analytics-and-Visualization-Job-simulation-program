import pandas as pd

# Load the datasets
content_df = pd.read_csv('Data/Content.csv')
reactions_df = pd.read_csv('Data/Reactions.csv')
reaction_types_df = pd.read_csv('Data/ReactionTypes.csv')

# Clean Content dataset
content_df_cleaned = content_df.dropna()  # Remove rows with missing values
content_df_cleaned = content_df_cleaned.rename(columns={'Type': 'Content Type'})  # Rename "Type" to "Content Type"
content_df_cleaned = content_df_cleaned.drop(columns=['User ID', 'URL'])  # Remove irrelevant columns
content_df_cleaned = content_df_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Remove blanks
content_df_cleaned.columns = content_df_cleaned.columns.str.strip()  # Remove blanks from column names

# Clean Reactions dataset
reactions_df_cleaned = reactions_df.dropna()  # Remove rows with missing values
reactions_df_cleaned = reactions_df_cleaned.rename(columns={'Type': 'Reaction Type'})  # Rename "Type" to "Reaction Type"
reactions_df_cleaned = reactions_df_cleaned.drop(columns=['User ID'])  # Remove irrelevant columns
reactions_df_cleaned = reactions_df_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Remove blanks
reactions_df_cleaned.columns = reactions_df_cleaned.columns.str.strip()  # Remove blanks from column names

# Clean ReactionTypes dataset
reaction_types_df_cleaned = reaction_types_df.dropna()  # Remove rows with missing values
reaction_types_df_cleaned = reaction_types_df_cleaned.rename(columns={'Type': 'Reaction Type'})  # Rename "Type" to "Reaction Type"
reaction_types_df_cleaned = reaction_types_df_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Remove blanks
reaction_types_df_cleaned.columns = reaction_types_df_cleaned.columns.str.strip()  # Remove blanks from column names

# Save the cleaned datasets to CSV files
content_df_cleaned.to_csv('Data/Content_Cleaned.csv', index=False, quotechar='', quoting=3)
reactions_df_cleaned.to_csv('Data/Reactions_Cleaned.csv', index=False, quotechar='', quoting=3)
reaction_types_df_cleaned.to_csv('Data/ReactionTypes_Cleaned.csv', index=False, quotechar='', quoting=3)

print('Content_Cleaned.csv, Reactions_Cleaned.csv, ReactionTypes_Cleaned.csv')
