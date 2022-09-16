from flask_app import app
from flask import render_template, request, redirect, session,flash
from flask_app.models.dojo_model import Dojo


# <----this are all the dojo routes--->
@app.route('/')
def render_create_dojos_MainPage():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template('create_dojos_all_dojos.html', all_dojos=all_dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    data = {
        
        'dojo_name': request.form['dojo_name']
    }
    Dojo.create(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def get_one_dojo(id): 
    dojo = {
            'id':id
    }
    dojo_and_ninjas = Dojo.get_one_by_id(dojo)
    return render_template('ninjas_info_by_id.html',dojo_and_ninjas=dojo_and_ninjas)


