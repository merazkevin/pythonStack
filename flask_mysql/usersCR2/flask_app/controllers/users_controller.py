from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.user_model import User

@app.route("/")
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", all_users=all_users)

@app.route('/user/new/form')
def newUser():
    return render_template("newUser.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.create(data)
    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
    'id':id
    }
    User.delete(data)
    return redirect('/')



# this route takes us to edit one user---->
@app.route('/edit/<int:id>')
def update(id):
    data={
        'id':id
        
    }
    one_user= User.get_one_by_id(data)
    return render_template('editUser.html', one_user=one_user)

@app.route('/edit/<int:id>/update', methods=['POST'])
def processing_update(id):
    data={
        "id":id,
        "first_name":request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email": request.form["email"],
    }
    User.update(data)
    return redirect('/')

@app.route('/show/user/<int:id>')
def user_show_page(id):
    data={
        'id':id
        
    }
    one_user= User.get_one_by_id(data)
    return render_template('showUser.html', one_user=one_user)

# @app.route('/show/user/<int:id>/users')
# def user_show
