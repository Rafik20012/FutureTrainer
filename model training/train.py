import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data from the Excel file
file_path = "model training/Merged_Cleaned_File_With_UserID.xlsx"  # Update with your file path
data = pd.read_excel(file_path)

# Split the data into features (X) and target (y)
X = data[['Age', 'Weight', 'Height', 'Calories_to_Burn']]
y = data[['Diet_Score', 'Exercise_Score']]  # Example targets, replace with your actual columns

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(y_train.shape[1], activation='linear')  # Adjust the output layer based on your targets
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32)

# Save the model
model.save("model.h5")
print("Model saved as model.h5")
