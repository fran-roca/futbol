import mysql.connector
import json


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
        return json.dumps(json_data, ensure_ascii=False).encode('utf8')

    def execute_query_one(self, query, row_headers):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            json_data=dict(zip(row_headers,result))
            return json.dumps(json_data, ensure_ascii=False).encode('utf8')
        else:
            return {}