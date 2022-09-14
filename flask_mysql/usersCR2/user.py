from mysqlconnection import connectToMySQL
DATABASE = 'user2'
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_users = []
        for row_from_db in results:
            user_instance= cls(row_from_db)
            all_users.append(user_instance)
        return all_users
    
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])
        

    @classmethod
    def create(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE id=(%(id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name= %(first_name)s , last_name = %(last_name)s, email = %(email)s , created_at= NOW(), updated_at= NOW() WHERE id=%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)
