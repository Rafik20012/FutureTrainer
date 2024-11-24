';llkjgfsaASFimport pandas as pd

# Load the files
file1 = pd.read_excel('Merged_Diet_Food_Recommendations.xlsx')
file2 = pd.read_excel('Min_macros_for_height_and_weight.xlsx')

# Rename 'Unnamed: 0' to 'UserID' in file2 for consistency
file2 = file2.rename(columns={'Unnamed: 0': 'UserID'})

# Convert 'Food Energy (Calories/day)' columns to numeric types, removing commas if any
file1['Food Energy (Calories/day)'] = pd.to_numeric(file1['Food Energy (Calories/day)'], errors='coerce')
file2['Food Energy (Calories/day)'] = pd.to_numeric(file2['Food Energy (Calories/day)'].str.replace(',', ''), errors='coerce')

# Drop duplicate rows in each file
file1 = file1.drop_duplicates()
file2 = file2.drop_duplicates()

# Merge the dataframes on common columns (adjust columns if needed)
merged_df = pd.merge(
    file1, file2,
    on=['Protein (grams/day)', 'Carbs (grams/day)', 'Fat (grams/day)', 'Sugar (grams/day)', 'Food Energy (Calories/day)'],
    how='outer',
    suffixes=('_file1', '_file2')
)

# Drop any remaining duplicates in the merged data
merged_df = merged_df.drop_duplicates()

# Save the merged and deduplicated data to a new Excel file
merged_df.to_excel('Merged_Cleaned_File.xlsx', index=False)

print("Merging and deduplication complete. Saved as 'Merged_Cleaned_File.xlsx'")
