import pandas as pd

# Load the merged file
merged_df = pd.read_excel('Merged_Cleaned_File.xlsx')

# Create a new 'UserID' column with a "User" prefix and incrementing numbers
merged_df['UserID_file1'] = ['User' + str(i + 1) for i in range(len(merged_df))]

# Save the modified DataFrame to a new file
merged_df.to_excel('Merged_Cleaned_File_With_UserID.xlsx', index=False)

print("UserID_file1 arranged in 'User+number' format and saved as 'Merged_Cleaned_File_With_UserID.xlsx'")
