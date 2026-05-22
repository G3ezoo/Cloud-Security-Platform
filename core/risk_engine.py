def calculate_risk(findings):

    weights = {
        "Critical": 40,
        "High": 25,
        "Medium": 10,
        "Low": 5
    }

    score = 0

    for f in findings:
        score += weights.get(f["severity"], 0)

    if score > 80:
        level = "CRITICAL"
    elif score > 40:
        level = "HIGH"
    elif score > 15:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level
    }