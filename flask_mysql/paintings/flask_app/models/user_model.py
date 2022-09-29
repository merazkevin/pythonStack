from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app.models import painting_model
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

# <--- classmethods--->

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        return cls(results[0])
        
    @classmethod
    def select_by_id(cls,data):
        query=" SELECT * FROM users WHERE id=%(user_id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])

    @classmethod
    def select_user_with_painting(cls,data):
        query="SELECT* FROM users LEFT JOIN painting ON users.id=painting.users_id WHERE users.id= %(users_id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            return False
        user_instance=cls(results[0])
        for row in results:
            painting_data = {
                "id" : row["painting.id"],
                "tittle":row['tittle'],
                "description":row['description'],
                "price":row['price'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at'],
                "users_id":row['users_id']
            }
            painting_instance=painting_model.Painting(painting_data)
            user_instance.list_of_paintings.append(painting_instance)
        return user_instance
        
    


    @staticmethod
    def validate_registration(data:dict)->bool:
        is_valid = True
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

        if len(data['password_confirm'])<=3:
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
