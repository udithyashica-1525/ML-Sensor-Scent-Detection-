import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Create models folder
os.makedirs("models", exist_ok=True)

# Load dataset
data = pd.read_csv("dataset.csv")

X = data[['gas_value']]
y = data['gas_value']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Models
svr = SVR(kernel='rbf', C=100, gamma=0.1)
rf = RandomForestRegressor()
bpnn = MLPRegressor(max_iter=500)
cart = DecisionTreeRegressor()

models = {
    "SVR": svr,
    "RF": rf,
    "BPNN": bpnn,
    "CART": cart
}

scores = {}

# Train models
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = r2_score(y_test, preds)
    scores[name] = score
    joblib.dump(model, f"models/{name.lower()}.pkl")

# Print accuracy
print("\nModel Accuracy:")
for k, v in scores.items():
    print(f"{k}: {round(v*100,2)}%")

# Graph
plt.figure()
plt.bar(scores.keys(), scores.values())
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()
