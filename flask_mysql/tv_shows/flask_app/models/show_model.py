from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session
from flask_app.models import user_model


class Show:
    def __init__(self, data):
        self.id = data['id']
        self.tittle= data['tittle']
        self.network= data['network']
        self.released_date= data['released_date']
        self.description= data['description']
        self.users_id= data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# <---insert show into Db --->
    @classmethod
    def create(cls, data):
        query = "INSERT INTO shows (tittle, network, released_date, description, users_id) VALUES( %(tittle)s, %(network)s, %(released_date)s, %(description)s, %(users_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data)

#<---get one by tittle-->
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM shows LEFT JOIN users ON users.id=users_id WHERE shows.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            return False
        show = cls(results[0])
        row = results[0]
        user={
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
        }
        user_instance= user_model.User(user)
        show.posted_by=user_instance
        return show



# <---staticmethod-->
    @staticmethod
    def validate_show(data:dict)->bool:
        is_valid= True
        if len(data['tittle'])<=3:
            flash('tittle is required')
            is_valid = False
        if len(data['network'])<=3:
            flash('network is required')
            is_valid = False
        if len(data['released_date'])<=3:
            flash('released_date is required to be 3 or more characters')
            is_valid = False
        if len(data['description'])<=3:
            flash('description cnat be blank')
            is_valid = False
        return is_valid

