from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        

    # CREATE 
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)
    
    # READ
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"        # each dictionary is a row in the table
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []

        for row in results:
            dojos.append(cls(row))

        return dojos

    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
            }
            dojo.ninjas.append(Ninja(n))
        return dojo 

    





    # @classmethod
    # def get_ninjas_in_dojo( cls, id ):
    #     query = "SELECT* FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(self.id)s;"
    #     results = connectToMySQL('dojo_ninjas').query_db(query,id)
    #     print(results)
    
    
    
    
    
    
    # @classmethod
    # def get_all_dojos(cls):
    #     query = "SELECT * FROM dojos;"        
    #     results = connectToMySQL("dojos_and_ninjas").query_db(query)
    #     dojos = []

    #     for row in results:
    #         dojos.append(cls(row))

    #     return dojos

    
    
    # @classmethod
    # def show_one(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(id)s;"
    #     result = connectToMySQL("users_schema").query_db(query, data)
    #     return cls(result[0])

    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        
    #     return connectToMySQL("users_schema").query_db(query, data)

    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     connectToMySQL("users_schema").query_db(query, data)
        


    