from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        date1 = request.form['date1']
        date2 = request.form['date2']

        try:
            d1 = datetime.strptime(date1, '%Y-%m-%d')
            d2 = datetime.strptime(date2, '%Y-%m-%d')

            difference = abs((d2 - d1).days)
            result = f"Difference: {difference} days"

        except Exception:
            error = "Invalid date input. Please try again."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)