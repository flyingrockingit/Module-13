from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    count = None
    text = ""

    if request.method == "POST":
        text=request.form.get('text',"")

        vowels = "aeiouAEIOU"
        count = sum(1 for char in text if char in vowels)
    
    return render_template('index.html',count=count, text=text)

if __name__ == '__main__':
    app.run(debug=True)