import random

def calculate_risk(lat, lon, hour):
    """
    Simple AI-inspired risk scoring logic
    (hackathon-safe, explainable)
    """

    crime_risk = random.uniform(0.3, 0.9) if hour >= 20 or hour <= 5 else random.uniform(0.1, 0.4)
    pothole_risk = random.uniform(0.1, 0.5)
    lighting_risk = random.uniform(0.2, 0.6)

    risk_score = (crime_risk * 0.5) + (pothole_risk * 0.3) + (lighting_risk * 0.2)

    return round(min(risk_score * 100, 100), 2)
