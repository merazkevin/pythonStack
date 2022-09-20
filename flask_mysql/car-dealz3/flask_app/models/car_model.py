from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Car:
    def __init__(self,data):
        self.id = data['id']
        self.price= data['price']
        self.model= data['model']
        self.make= data['make']
        self.year= data['year']
        self.description= data['description']
        self.users_table= data['users_table']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars_table;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_cars = []
        for row_from_db in results:
            cars_instance= cls(row_from_db)
            all_cars.append(cars_instance)
        return all_cars 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cars_table WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return cls(results[0])
        return False

    @classmethod
    def create_car_for_sale(cls, data):
        query = "INSERT INTO cars_table WHERE (price, model, make, year, description) Values (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s);"
        return connectToMySQL(DATABASE).query_db( query, data)
