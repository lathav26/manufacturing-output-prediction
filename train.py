import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle

# Load dataset
df = pd.read_csv("data/manufacturing_dataset_1000_samples.csv")

# Select ONLY required columns
columns = [
    "Injection_Temperature",
    "Injection_Pressure",
    "Cycle_Time",
    "Cooling_Time",
    "Material_Viscosity",
    "Ambient_Temperature",
    "Machine_Age",
    "Operator_Experience",
    "Maintenance_Hours"
]

X = df[columns]
y = df["Parts_Per_Hour"]

# Handle missing values
X = X.fillna(X.mean())

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(scaler, open("model/scaler.pkl", "wb"))

print("Model trained successfully!")