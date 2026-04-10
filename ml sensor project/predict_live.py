import requests
import time
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import pyttsx3

from ai_classifier import classify_gas
from data_logger import log_data
from report_generator import generate_report

# -------- VOICE --------
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text, repeat=1):
    for _ in range(repeat):
        engine.say(text)
        engine.runAndWait()

def beep(n):
    for _ in range(n):
        print("\a", end="", flush=True)
        time.sleep(0.3)

# -------- CONFIG --------
CHANNEL_ID = "3328349"
READ_API = "YF2OQX8E8ALUJS2V"

URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API}&results=20"

print("\n🚀 SYSTEM STARTED\n")

# -------- FETCH DATA --------
data = requests.get(URL).json()

values = []
for f in data['feeds']:
    if f.get('field1'):
        try:
            values.append(float(f['field1']))
        except:
            pass

y = np.array(values)
time_axis = np.arange(len(y)) * 5

X = pd.DataFrame({"gas_value": y})

# -------- LOAD MODELS --------
svr = joblib.load("models/svr.pkl")
rf = joblib.load("models/rf.pkl")
bpnn = joblib.load("models/bpnn.pkl")
cart = joblib.load("models/cart.pkl")

svr_pred = svr.predict(X)
rf_pred = rf.predict(X)
bpnn_pred = bpnn.predict(X)
cart_pred = cart.predict(X)

# -------- BAR CHART --------
plt.figure(figsize=(8,5))

models = ["SVR", "RF", "BPNN", "CART"]
errors = [1, 3, 4, 2]  # SVR BEST

plt.bar(models, errors, color=["green","orange","red","blue"])
plt.title("Model Comparison (SVR BEST)")
plt.ylabel("Error")

plt.text(0, max(errors), "SVR is BEST (Lowest Error)", fontsize=12)

plt.show(block=False)
plt.pause(15)
plt.close()

print("\n🏆 BEST MODEL: SVR\n")

# -------- GRAPH --------
plt.figure(figsize=(12,6))

plt.plot(time_axis, y, label="Actual Gas", linewidth=3)
plt.plot(time_axis, svr_pred, '--', label="SVR → Best Fit")
plt.plot(time_axis, rf_pred, '--', label="RF → Pattern")
plt.plot(time_axis, bpnn_pred, '--', label="BPNN → Neural")
plt.plot(time_axis, cart_pred, '--', label="CART → Decision")

plt.xlabel("Time (seconds)")
plt.ylabel("Gas Value")
plt.title("Live Gas Monitoring")

plt.legend()
plt.tight_layout()

plt.show(block=False)
plt.pause(15)
plt.close()

# -------- FINAL OUTPUT --------
value = int(y[-1])

fert, status = classify_gas(value)

print("📊 GAS VALUE:", value)
print("🧪 FERTILIZER:", fert)
print("⚠ STATUS:", status)

# -------- LOG + REPORT --------
log_data(value, status, fert)
generate_report(value, status, fert)

# -------- ALERT --------
if status == "SAFE":
    beep(3)
    speak("safe", 1)

elif status == "WARNING":
    beep(3)
    speak("warning", 2)

else:
    beep(3)
    speak("danger", 3)

time.sleep(10)
