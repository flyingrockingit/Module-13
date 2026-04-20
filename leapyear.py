from flask import Flask, render_template, request

app = Flask(__name__)

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        year = int(request.form["year"])

        if is_leap_year(year):
            result = f"{year} is a Leap Year"
        else:
            result = f"{year} is NOT a Leap Year"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)