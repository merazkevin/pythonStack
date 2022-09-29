from flask_app import app
from flask import render_template, request, redirect, session,flash


@app.route('/')
def idex():
    return render_template('index.html')    

@app.route('/process/form', methods=["POST"])
def process_form():
    print(request.form)
    session['dog_name'] = request.form['dog_name']
    session['dog_breed']= request.form['dog_breed']
    return redirect('/show/info')

@app.route('/show/info')
def show_info():
    name = session['dog_name']
    breed= session['dog_breed']
    return render_template('display.html', name=name, breed=breed )