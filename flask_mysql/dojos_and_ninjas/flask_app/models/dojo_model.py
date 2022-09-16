from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
DATABASE = 'dojos_ninjas'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos_table;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_dojos = []
        for row_from_db in results:
            dojos_instance= cls(row_from_db)
            all_dojos.append(dojos_instance)
        return all_dojos

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM dojos_table LEFT JOIN ninjas_table ON dojos_table.id=dojo_id WHERE dojos_table.id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        dojo = cls(results[0])
        ninjas_in_dojos=[]
        for row_from_db in results:
            ninja_data = {

                'id':row_from_db['ninjas_table.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age':row_from_db['age'],
                'created_at':row_from_db['ninjas_table.created_at'],
                'updated_at':row_from_db['ninjas_table.updated_at'],
                'dojo_id': row_from_db['dojo_id']
            }
            ninja_instance = ninja_model.Ninja(ninja_data)
            ninjas_in_dojos.append(ninja_instance)
        dojo.my_ninjas = ninjas_in_dojos
        return dojo

    @classmethod
    def create(cls, data ):
        query = "INSERT INTO dojos_table ( dojo_name ) VALUES (%(dojo_name)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM dojos_table WHERE id=(%(id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos_table SET first_name= %(first_name)s , last_name = %(last_name)s, email = %(email)s , created_at= NOW(), updated_at= NOW() WHERE id=%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)