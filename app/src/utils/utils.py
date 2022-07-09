import mysql.connector
import datetime
import json

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)

class DocumentDB:
    """
        Clase para gestionar la base de datos MySQL
    """

    def __init__(self, host, database, username, password):
        """
            Constructor de la conexión a MySQL

            Args:
               host (str):  Host de la base de datos.
               username (str): usuario.
               password (str): contraseña.
        """
        self.connection = mysql.connector.connect(
            host = host,
            database = database,
            user = username,
            password = password
            )

    def execute_query_multi(self, query, row_headers):
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        json_data=[]
        for result in rows:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data,cls=DateEncoder, ensure_ascii=False).encode('utf8')

    def execute_query_one(self, query, row_headers):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            json_data=dict(zip(row_headers,result))
            return json.dumps(json_data,cls=DateEncoder, ensure_ascii=False).encode('utf8')
        else:
            return {}