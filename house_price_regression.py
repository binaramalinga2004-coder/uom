import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# CSV file read කරනවා
data = pd.read_csv('Housing.csv')

# Data check
print("First 5 rows:")
print(data.head())

# Convert categorical features to numeric (Yes/No, furnishingstatus)
categorical_cols = ['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']
data_encoded = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Features සහ target define කරනවා
X = data_encoded.drop('price', axis=1)
y = data_encoded['price']

# Training සහ Testing data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Multiple Linear Regression model create
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Performance metrics print
print("\nModel Performance:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Plot actual vs predicted price
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Multiple Linear Regression - Actual vs Predicted Price")
plt.show()
