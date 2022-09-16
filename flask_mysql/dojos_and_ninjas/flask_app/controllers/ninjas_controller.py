from flask_app import app
from flask import render_template, request, redirect, session,flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

    # <---this are the ninja routes--->
@app.route('/ninja')
def new_Ninja_page():
    all_dojos=Dojo.get_all()
    return render_template('new_ninjas.html', all_dojos=all_dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect('/')

@app.route('/ninjas/info')
def render_ninja_info():
    data={
        'id':id,
        'dojo_name': request.form['dojo_name'],
        'id': request.form['id'],
        
    }
    all_ninjas = Ninja.left_join(data)
    return render_template('ninjas_info_by_id.html', all_ninjas = all_ninjas)