from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models.user_model import User


# <--registration/login page-->
@app.route('/')
def registration_login():
    if 'uuid' in session:
        return redirect('/user/dashboard')
    return render_template('registration_login.html')

@app.route('/create/user', methods=['POST'])
def create_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    hash_password = bcrypt.generate_password_hash(request.form['password'])
    print(hash_password)
    data={
        **request.form,
        'password': hash_password
    }
    id = User.create(data)
    session['uuid'] = id
    return redirect('/')

@app.route('/user/process/login', methods=['POST'])
def user_process_login():
    data={'email':request.form['email']}
    user_in_db = User.get_one_by_email(data)
    if not user_in_db:
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('password invalid')
        return redirect('/')
    else:
        session['uuid']= user_in_db.id
    return redirect('/user/dashboard')

@app.route('/user/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('user_dashboard.html')



@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')
