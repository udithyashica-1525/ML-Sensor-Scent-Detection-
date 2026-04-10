def classify_gas(value):
    if value < 260:
        return "UREA", "SAFE"
    else:
        return "MIXED", "DANGER"
