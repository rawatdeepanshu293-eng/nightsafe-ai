from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from risk_model import calculate_risk

app = Flask(__name__)
CORS(app)

@app.route("/risk", methods=["GET"])
def get_risk():
    lat = float(request.args.get("lat"))
    lon = float(request.args.get("lon"))

    hour = datetime.now().hour
    risk = calculate_risk(lat, lon, hour)

    return jsonify({
        "latitude": lat,
        "longitude": lon,
        "risk_score": risk,
        "risk_level": "High" if risk > 65 else "Medium" if risk > 35 else "Low"
    })

if __name__ == "__main__":
    app.run(debug=True)
