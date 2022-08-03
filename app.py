#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rootpage():
    weight = ''
    height = ''
    bmi = 0
    if request.method == 'POST' and 'userweight' in request.form and 'userheight' in request.form:
        weight = int(request.form.get('userweight'))
        height = int(request.form.get('userheight'))/100
        bmi = weight/(height*height)
    return render_template("index.html", weight=weight, height=height, bmi=bmi)

app.run()