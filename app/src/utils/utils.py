import mysql.connector


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