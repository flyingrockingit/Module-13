from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

geolocator = Nominatim(user_agent="locate_me_app")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/geocode", methods=["POST"])
def geocode():
    data = request.get_json()
    location = data.get("location")

    if not location:
        return jsonify({"error": "No location provided"}), 400

    try:
        result = geolocator.geocode(location)

        if result is None:
            return jsonify({"error": "Location not found"}), 404

        return jsonify({
            "lat": result.latitude,
            "lon": result.longitude,
            "display_name": result.address
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)