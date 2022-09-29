from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models import user_model


@app.route('/')
def register_login():
    return render_template('register_login.html')\

#<--- Insert user in db ---->
@app.route('/register/user', methods=['POST'])
def register_user():
    if not user_model.User.validate_registration(request.form):
        return redirect('/')
        # hashing password
    hash_password = bcrypt.generate_password_hash(request.form['password'])
    print(hash_password)
    data={
        **request.form,
        'password':hash_password,
    }
    id = user_model.User.create(data)
    session['uuid'] = id
    return redirect('/')

# <---dashboard -->
@app.route('/user/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('user_dashboard.html')

# <---login check--->
@app.route('/user/process/login', methods=['POST'])
def user_process_login():
    data={'email':request.form['email']}
    user_in_db=user_model.User.get_one_by_email(data)
    if not user_in_db:
        flash('user not valid')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('password invalid')
        return redirect('/')
    else:
        session['uuid']= user_in_db.id
    return redirect('/user/dashboard')

@app.route('/user/<int:id>')
def get_one_dojo(id): 
    user = {
            'id':id
    }
    users_and_shows = user_model.User.left_join_get_one_by_id(user)
    return render_template('ninjas_info_by_id.html',users_and_shows=users_and_shows)

# <---log OUt--->
@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

