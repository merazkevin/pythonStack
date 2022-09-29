from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session
from flask_app.models import user_model


class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.title =data['title']
        self.description =data['description']
        self.price =data['price']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
        self.users_id =data['users_id']

# <--- CLASSMETHODS --->
    @classmethod
    def get_all(cls):
        query = "select * from painting;"
        return connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def create_painting(cls, data):
        query = "INSERT INTO painting ( title,description, price, users_id) VALUES(%(title)s, %(description)s, %(price)s, %(users_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data)
    
    @classmethod
    def update(cls,data):
        query="UPDATE painting SET title= %(title)s, description=%(description)s, price=%(price)s, users_id = %(users_id)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    
    @classmethod
    def delete(cls, data):
        query="delete from painting where painting.id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_painting_by_id(cls,data):
        query = "select * from painting where id = %(painting_id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_painting_with_user(cls,data):
        query = "select * from painting join users on painting.users_id = users.id where painting.id = %(painting_id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        painting_instance = cls(results[0])
        print("================")
        print(results)
        print("================")
        user_data = {
            "id" : results[0]["users.id"],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'created_at' : results[0]['created_at'],
            'updated_at' : results[0]['updated_at']
        }
        painting_instance.user_list=user_model.User(user_data)
        return painting_instance

#<---STATICMETHODS--->
    @staticmethod
    def validate_painting(data):
        is_valid=True
        if len(data['title'])<3:
                flash('title is required')
                is_valid = False
        if len(data['description'])<3:
                flash('description is required')
                is_valid = False
        if len(data['price'])<3:
                flash('price is required')
                is_valid = False
        return is_valid