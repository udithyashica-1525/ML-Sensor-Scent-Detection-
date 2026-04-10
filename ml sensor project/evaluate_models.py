import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("dataset.csv")

X = data[['gas_value']]
y = data['gas_value']

# Load models
svr = joblib.load("models/svr.pkl")
rf = joblib.load("models/rf.pkl")
bpnn = joblib.load("models/bpnn.pkl")
cart = joblib.load("models/cart.pkl")

# Predictions
pred_svr = svr.predict(X)
pred_rf = rf.predict(X)
pred_bpnn = bpnn.predict(X)
pred_cart = cart.predict(X)

# Accuracy
scores = {
    "SVR": r2_score(y, pred_svr),
    "RF": r2_score(y, pred_rf),
    "BPNN": r2_score(y, pred_bpnn),
    "CART": r2_score(y, pred_cart)
}

print("Model Accuracy:\n", scores)

# Graph
plt.bar(scores.keys(), scores.values())
plt.title("Model Accuracy Comparison")
plt.ylabel("R2 Score")
plt.show()
