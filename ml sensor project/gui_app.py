import tkinter as tk
import threading
import requests
import joblib
import numpy as np
import time

from calibration import detect_gas_type, get_status

# ThingSpeak
CHANNEL_ID = "YOUR_CHANNEL_ID"
READ_API = "YOUR_READ_API_KEY"

URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API}&results=1"

# Load models
svr = joblib.load("models/svr.pkl")
rf = joblib.load("models/rf.pkl")
bpnn = joblib.load("models/bpnn.pkl")
cart = joblib.load("models/cart.pkl")

# GUI
root = tk.Tk()
root.title("Smart Gas Detection System")
root.geometry("400x300")

title = tk.Label(root, text="Real-Time Gas Detection", font=("Arial", 14))
title.pack(pady=10)

value_label = tk.Label(root, text="Gas Value: --")
value_label.pack()

gas_label = tk.Label(root, text="Gas Type: --")
gas_label.pack()

status_label = tk.Label(root, text="Status: --")
status_label.pack()

model_label = tk.Label(root, text="Best Model: --")
model_label.pack()

def update_data():
    def loop():
        while True:
            try:
                response = requests.get(URL)
                data = response.json()

                value = int(data['feeds'][0]['field1'])

                input_data = np.array([[value]])

                preds = [
                    svr.predict(input_data)[0],
                    rf.predict(input_data)[0],
                    bpnn.predict(input_data)[0],
                    cart.predict(input_data)[0]
                ]

                best_model = ["SVR","RF","BPNN","CART"][np.argmin(preds)]

                gas = detect_gas_type(value)
                status = get_status(value)

                value_label.config(text=f"Gas Value: {value}")
                gas_label.config(text=f"Gas Type: {gas}")
                status_label.config(text=f"Status: {status}")
                model_label.config(text=f"Best Model: {best_model}")

            except:
                pass

            time.sleep(3)

    threading.Thread(target=loop, daemon=True).start()

update_data()

root.mainloop()
