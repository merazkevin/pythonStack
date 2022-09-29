from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models import user_model, painting_model

@app.route('/add/painting')
def add_painting():
    return render_template('add_painting.html')

@app.route("/painting/processing/form", methods=['POST'])
def processing_form():
    if not painting_model.Painting.validate_painting(request.form):
        return redirect('/add/painting')
    data={
        **request.form,
        'users_id': session['uuid']
    }
    painting_model.Painting.create_painting(data)
    return redirect('/user/dashboard')

@app.route('/display/painting/<int:id>')
def display_tv(id):
    data={
        
        'painting_id':id
    }
    painting_with_user = painting_model.Painting.get_painting_with_user(data)
    return render_template('display_one.html', painting=painting_with_user)

@app.route('/delete/<int:id>')
def deleting(id):
    data = {
        'id':id
    }
    painting_model.Painting.delete(data)
    return redirect('/user/dashboard')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'painting_id':id
    }
    painting = painting_model.Painting.get_painting_by_id(data)
    return render_template('edit_page.html', painting=painting)

@app.route('/updating/painting', methods=['POST'])
def updating_painting():
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "price": request.form["price"],
        "users_id": session["uuid"],
        "id": request.form["id"]
    }
    painting_model.Painting.update(data)
    return redirect("/user/dashboard")