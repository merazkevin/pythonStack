from flask_app.config.mysqlconnection import connectToMySQL
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
        self.pw = data['pw']
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
        
        

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw, pw_confirm) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(pw)s, %(pw_confirm)s);"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE email= (%(email)s);"
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

        if len(data['pw'])<=0:
            flash('pw is required to be 3 or more characters')
            is_valid = False

        if len(data['pw_confirm'])<=0:
            flash('pw is required to be 3 or more characters')
            is_valid = False

        elif data['pw']!= data['pw_confirm']:
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

        if len(data['pw'])<=0:
            flash('pw is required to be 3 or more characters')
            is_valid = False

        if is_valid:
            data={
                'email':data['email'],
                'pw':data['pw']
            }
            potential_user = User.get_one_by_email({'email': data['email']})
            if not bcrypt.check_password_hash(potential_user.pw, data['pw']):
                flash("incorrect password")
                is_valid = False
            else:
                session['uuid'] = potential_user.id



        return is_valid

