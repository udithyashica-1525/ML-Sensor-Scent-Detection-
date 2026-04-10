def detect_gas_type(value):
    if 230 <= value <= 250:
        return "UREA"
   
    elif 250 <= value <= 400:
        return "MIXED"
    else:
        return "UNKNOWN"

def get_status(value):
    if value < 200:
        return "SAFE"
    elif value < 280:
        return "WARNING"
    else:
        return "DANGER"
