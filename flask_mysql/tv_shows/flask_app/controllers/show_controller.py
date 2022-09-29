import re
from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models.user_model import User
from flask_app.models.show_model import Show


@app.route('/add/show')
def add_show():
    return render_template('add_show.html')

@app.route('/processing/show', methods=['POST'])
def processing_show():
    if not Show.validate_show(request.form):
        return redirect('/add/show')
    data={
        **request.form,
        'users_id': session['uuid']
    }
    Show.create(data)
    return redirect('/user/dashboard')

@app.route('/display/tv/<int:id>')
def display_tv(id):
    data={
        
        'id':id
    }
    tv_show=Show.get_by_id(data)
    return render_template('display_show.html', tv_show=tv_show)