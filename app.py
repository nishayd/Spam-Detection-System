from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from helper import make_prediction

app = Flask(__name__)
app.secret_key = 'supersecretmre'


@app.route('/')
def index():
    flash('Welcome to the Flask App', 'info')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def forminput():
    result = None
    if request.method == 'POST':
        content = request.form['content']
        print(len(content))
        if len(content)<=1:
            flash('Please enter a valid input', 'danger')
            return redirect(url_for('forminput'))
        else:
            result = make_prediction([content])
            flash('Prediction made successfully', 'success')
    return render_template('form.html', result=result)

@app.route('/results', methods=['GET','POST'])
def result():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)