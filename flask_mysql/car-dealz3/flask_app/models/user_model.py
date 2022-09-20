from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app.models import car_model 
from flask import flash,session


import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

# <---classmethods--->
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_table;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_users = []
        for row_from_db in results:
            users_instance= cls(row_from_db)
            all_users.append(users_instance)
        return all_users 

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users_table (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users_table WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        return cls(results[0])

#<--- staticmethods --->
    @staticmethod
    def validate_registration(data):
        is_valid=True
        if len(data['first_name'])<=3:
            flash('first_name is required')
            is_valid = False

        if len(data['last_name'])<=3:
            flash('last_name is required to be 3 or more characters')
            is_valid = False

        if len(data['email'])<=3:
            flash('email is required to be 3 or more characters')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['password'])<=3:
            flash('password is required to be 3 or more characters')
            is_valid = False

        elif data['password']!= data['password_confirm']:
            flash('passwords do not match')
            is_valid=False

        return is_valid

    @staticmethod
    def validate_login(data:dict)->bool:
        is_valid = True
        if len(data['email'])<=0:
            flash('email is required to be 3 or more characters')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['password'])<=0:
            flash('password is required to be 3 or more characters')
            is_valid = False

        if is_valid:
            data={
                'email':data['email'],
                'password':data['password']
            }
            potential_user = User.get_one_by_email({'email': data['email']})
            if not bcrypt.check_password_hash(potential_user.password, data['password']):
                flash("incorrect password")
                is_valid = False
            else:
                session['uuid'] = potential_user.id
        return is_valid

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users_table LEFT JOIN cars_table ON cars_table.id=users_table_id WHERE cars_table.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        car = cls(results[0])
        cars_and_sellers=[]
        for row_from_db in results:
            car_data = {
                'id':row_from_db['cars_table.id'],
                'model': row_from_db['model'],
                'year': row_from_db['year'],
                'seller':row_from_db['seller'],
                'id': row_from_db['users_table_id']
            }
            car_instance = car_model.Car(car_data)
            cars_and_sellers.append(car_instance)
        User.my_cars = cars_and_sellers
        return car