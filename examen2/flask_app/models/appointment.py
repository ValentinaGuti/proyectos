from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User	# the regex module

class Appointment:
    db_name = "esquema_citas"
    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['users_id']
        self.user = data.get('user', None)

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM appointments;"
        results = connectToMySQL(cls.db_name).query_db(query)
        appointments = []
        for row in results:
            appointments.append(cls(row))
        return appointments

    @classmethod
    def save(cls, data):
        query = "INSERT INTO appointments (task, date, status, users_id) VALUES (%(task)s, %(date)s, %(status)s, %(users_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_by_user_id(cls, user_id):
        query = "SELECT * FROM appointments WHERE users_id = %(user_id)s;"
        data = {'user_id': user_id}
        results = connectToMySQL(cls.db_name).query_db(query, data)
        appointments = []
        for row in results:
            appointments.append(cls(row))
        return appointments
    