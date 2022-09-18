from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models import user_model



# <---1 Route--->
@app.route('/')
def register_login_page():
    if 'uuid'in session:
        return redirect('/user/dashboard')
    return render_template('register_login_page.html')

# <---2 Route--->
@app.route('/register/user', methods=['POST'])
def register_user():
    if not user_model.User.validate_registration(request.form):
        return redirect('/')
        # hashing password
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    print(hash_pw)
    data={
        **request.form,
        'pw':hash_pw,
        'pw_confirm':hash_pw
    }
    id = user_model.User.create(data)
    session['uuid'] = id
    return redirect('/')

# <---3 Route--->
@app.route('/user/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('user_dashboard.html')

#<---4 Route--->
@app.route('/user/process/login', methods=['POST'])
def user_process_login():
    data={'email':request.form['email']}
    user_in_db=user_model.User.get_one_by_email(data)
    if not user_in_db:
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.pw, request.form['pw']):
        flash('password invalid')
        return redirect('/')
    else:
        session['uuid']= user_in_db.id
    return redirect('/user/dashboard')
#<---5 Route--->
@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')