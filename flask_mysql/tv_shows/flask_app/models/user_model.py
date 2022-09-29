from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import show_model
from flask_app import DATABASE, bcrypt
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
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_users = []
        for row_from_db in results:
            users_instance= cls(row_from_db)
            all_users.append(users_instance)
        return all_users 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        return cls(results[0])

# <---get all left join--->
    @classmethod
    def get_by_id(cls, data):
        query= "SELECT * FROM users LEFT JOIN shows ON users_id =%(id)s;"
        results = connectToMySQL(DATABASE).query_db( query, data)
        if not results:
            return False
        user = cls(results[0])
        users_and_shows=[]
        for row_from_db in results:
            tv_data = {
                **user,
                'id':row_from_db['users.id'],
                'tittle': row_from_db['tittle'],
                'network': row_from_db['network'],
                'released_date':row_from_db['released_date'],
                'created_at':row_from_db['show.created_at'],
                'updated_at':row_from_db['show.updated_at'],
                'id':row_from_db['users_id']
            }
            show_on_tv = show_model.Show(tv_data)
            users_and_shows.append(show_on_tv)
        user.my_shows = users_and_shows
        return user


    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data)

    @staticmethod
    def validate_registration(data:dict)->bool:
        is_valid = True
        if len(data['first_name'])<=0:
            flash('first_name is required')
            is_valid = False

        if len(data['last_name'])<=0:
            flash('last_name is required to be 3 or more characters')
            is_valid = False

        if len(data['email'])<=0:
            flash('email is required to be 3 or more characters')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['password'])<=0:
            flash('password is required to be 3 or more characters')
            is_valid = False

        if len(data['password_confirm'])<=0:
            flash('password is required to be 3 or more characters')
            is_valid = False

        elif data['password']!= data['password_confirm']:
            flash('passwords do not match')
            is_valid=False

        return is_valid

    @staticmethod
    def validate_login(data:dict)->bool:
        is_valid = True
        if len(data['email'])<=3:
            flash('email is required to be 3 or more characters')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(data['password'])<=3:
            flash('pw is required to be 3 or more characters')
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
