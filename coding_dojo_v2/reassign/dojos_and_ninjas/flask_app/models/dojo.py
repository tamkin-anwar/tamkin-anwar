# import connectToMySQL from flask_app.config.mysqlconnection
from flask_app.config.mysqlconnection import connectToMySQL
# import Ninja class from .ninja
from .ninja import Ninja
#class for Dojo creating connection to database
class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#classmethod to query select all from dojos and add result to list
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojo_and_ninjas').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos
#classmethod to query insert data into database
    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojo_ninjas').query_db(query,data)
        return result
#classmethod to query select all from dojos table in database and left join ninjas table on dojos.id and ninjas.dojo_id where inputed id gets appended to dojos.id
    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo