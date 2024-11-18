import pandas as pd
import joblib

# Load the saved model
model = joblib.load('saved_model/random_forest.joblib')

# Load the test dataset
test_data = pd.read_csv('dataset/test_data.csv')

# Assuming the last column is the target, separate features (X) and target (y)
X_test = test_data.iloc[:, :-1]  # All columns except the last
y_test = test_data.iloc[:, -1]   # Last column (target)

# Make predictions
predictions = model.predict(X_test)

# Display results
print("Predictions:", predictions)

# Optional: Evaluate the model
# If y_test is available, calculate accuracy or other metrics
accuracy = (predictions == y_test).mean()
print("Accuracy:", accuracy)
