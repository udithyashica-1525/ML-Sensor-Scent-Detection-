import csv
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

def log_data(value, status, fert):
    with open("logs/data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), value, fert, status])
