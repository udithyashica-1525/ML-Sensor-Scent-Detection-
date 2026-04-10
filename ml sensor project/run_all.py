import subprocess
import time
import webbrowser
import threading
import os

print("\n🚀 STARTING FULL AI SYSTEM...\n")

# ---------------- STEP 1: RUN ML + GRAPHS ----------------
print("🔹 Running ML Prediction + Graphs...\n")

subprocess.run(["python", "predict_live.py"])

# ---------------- STEP 2: START WEB SERVER ----------------
print("\n🔹 Starting Web Dashboard...\n")

def start_server():
    os.system("python app.py")

threading.Thread(target=start_server).start()

# ---------------- STEP 3: WAIT FOR SERVER ----------------
time.sleep(5)

# ---------------- STEP 4: OPEN FULLSCREEN ----------------
print("🌐 Opening Dashboard...\n")

try:
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --start-fullscreen"
    webbrowser.get(chrome_path).open("http://127.0.0.1:5000")
except:
    webbrowser.open("http://127.0.0.1:5000")

print("\n✅ SYSTEM FULLY RUNNING\n")
