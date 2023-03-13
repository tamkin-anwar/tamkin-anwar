# import connectToMySQL from flask_app.config.mysqlconnection
from flask_app.config.mysqlconnection import connectToMySQL
#class for ninja creating connection to database
class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#classmethod to query insert data into database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name,age,dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojo_ninjas').query_db(query,data)