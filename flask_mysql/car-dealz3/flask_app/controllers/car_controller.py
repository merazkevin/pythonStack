from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models.car_model import Car


@app.route('/car/<int:id>')
def get_one_car(id): 
    car = {
            'id':id
    }
    cars_and_sellers = Car.get_one_by_id(car)
    return render_template('car_info_by_id.html',cars_and_sellers=cars_and_sellers)

@app.route('/car/sale/post')
def car_sale_post():
    return render_template('car_sale_post.html')

@app.route('/create/car/post', methods=['POST'])
def create_car_post():
    Car.create_car_for_sale(request.form)
    return redirect('/user/dashboard')