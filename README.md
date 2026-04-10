
---

🚀 Machine Learning Driven Gas Sensor Network

For On-Site Agrochemical Hazardous Scent Detection

---

📌 Overview

This project presents a real-time IoT + Machine Learning based gas detection system designed to identify and classify agrochemical gases such as Urea, Potassium, and Mixed Fertilizers.

The system enables farmers, warehouses, and industries to instantly monitor chemical safety without relying on laboratory testing.

---

🎯 Key Features

- 🔍 Real-time gas detection using MQ sensor
- 🌐 Cloud integration using ThingSpeak
- 🤖 Machine Learning prediction (SVR, BPNN, CART, RFR)
- 📊 Live graph monitoring
- 🎛️ Animated gauge visualization
- 🚨 Smart alert system (Safe / Warning / Danger)
- 🔊 Voice + sound alerts
- 🖥️ Full-screen web dashboard (Flask-based)
- 📈 Model comparison with accuracy analysis

---

🧠 Machine Learning Models Used

Model| Description
SVR| Best performing model with high accuracy
BPNN| Learns complex patterns
CART| Rule-based decision making
RFR| Ensemble-based prediction

✅ SVR is selected as the final model due to superior performance

---

🏗️ System Architecture

MQ Gas Sensor → ESP8266 → ThingSpeak Cloud → Python ML Model → Flask Web App → User Interface

---

⚙️ Technologies Used

- Hardware: MQ Gas Sensor, ESP8266 (NodeMCU)
- Programming: Python
- Libraries:
  - scikit-learn
  - matplotlib
  - flask
  - numpy
  - pygame (for alerts)
- Cloud: ThingSpeak API
- Web: HTML + CSS + Chart.js

---

📊 Working Methodology

1. Gas sensor collects real-time data
2. ESP8266 uploads data to ThingSpeak
3. Python fetches and preprocesses data
4. ML models are trained and compared
5. SVR model predicts gas concentration
6. System classifies gas type and safety level
7. Dashboard displays live results

---

🧪 Gas Classification Logic

Gas Type| Range
Urea| 330 – 360
Potassium| 350 – 380
Mixed| 330 – 400

---

🚦 Status Levels

- 🟢 SAFE
- 🟡 WARNING
- 🔴 DANGER

---

🖥️ User Interface

- Real-time graph visualization
- Animated gauge meter
- Background alert system (color-based)
- Fertilizer details with image
- Live monitoring dashboard

---

📸 Screenshots

«(Add your screenshots here for better impact)»

---

▶️ How to Run the Project

1️⃣ Install Dependencies

pip install flask matplotlib numpy requests pygame scikit-learn

---

2️⃣ Update API Keys

In your Python files, replace:

CHANNEL_ID = "YOUR_CHANNEL_ID"
READ_API = "YOUR_API_KEY"

---

3️⃣ Run the System

python run_all.py

---

4️⃣ Output Flow

- Model comparison graph
- Live gas monitoring graph
- Automatic browser dashboard

---

📁 Project Structure

project/
│
├── run_all.py
├── predict_live.py
├── app.py
├── alarm.mp3
├── README.md

---

💡 Applications

- 🌾 Agriculture (fertilizer monitoring)
- 🏭 Chemical industries
- 📦 Warehouses
- 🧪 Storage facilities

---

🚀 Future Enhancements

- Mobile app integration
- Advanced AI models
- Multi-sensor fusion
- Cloud analytics dashboard
- Predictive maintenance alerts

---

📚 References

- Scikit-learn Documentation
- ThingSpeak API Docs
- IEEE Research Papers on Gas Detection

---

🙌 Acknowledgment

We sincerely thank our guide and institution for their support in completing this project.

---

⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Share with others
