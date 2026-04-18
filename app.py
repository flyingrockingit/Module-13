from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_age():
    try:
        birth_year = int(request.form["birth_year"])
        current_year = datetime.now().year

        if birth_year > current_year:
            return render_template(
                "index.html",
                error=f"Please enter a valid year (not past {current_year})"
            )

        age = current_year - birth_year
        return render_template("index.html", age=age)

    except ValueError:
        return render_template("index.html", error="Please enter a valid number")

if __name__=="__main__":
    app.run(debug=True)