from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'dojos_ninjas'

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas_table;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_ninjas = []
        for row_from_db in results:
            ninja_instance= cls(row_from_db)
            all_ninjas.append(ninja_instance)
        return all_ninjas

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM ninjas_table WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results[0])
        return cls(results[0])

    @classmethod
    def create(cls, data ):
        query = "INSERT INTO ninjas_table ( first_name, last_name, age, dojo_id ) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s) ;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM ninjas_table WHERE id=(%(id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas_table SET first_name= %(first_name)s , last_name = %(last_name)s, age = %(age)s , created_at= NOW(), updated_at= NOW() WHERE id=%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def left_join(cls, data):
        query ="SELECT * FROM dojos_table LEFT JOIN ninjas_table ON ninjas_table.id ORDER BY dojo_name;"
        print(data)
        return connectToMySQL(DATABASE).query_db(query, data)