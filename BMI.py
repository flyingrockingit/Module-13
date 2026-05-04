from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None

    if request.method == "POST":
        weight = request.form.get('weight')
        height = request.form.get('height')

        if weight and height:
            try:
                weight = float(weight)
                height = float(height)

                # convert cm → meters
                height_m = height / 100

                if height_m > 0:
                    bmi = weight / (height_m ** 2)

                    if bmi < 18.5:
                        category = "Underweight"
                    elif bmi < 25:
                        category = "Normal weight"
                    elif bmi < 30:
                        category = "Overweight"
                    else:
                        category = "Obese"
            except ValueError:
                bmi = None
                category = "Invalid input"

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)