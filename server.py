from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/ninja')

def ninjas():
    return render_template('ninjas.html')

@app.route('/ninja/<color>')

def show_ninja(color):
    if (color == "blue" or color == "orange" or color == "red" or color == "purple"):
        return render_template(color + '.html')
    else:
        return render_template('notapril.html')

app.run(debug=True)