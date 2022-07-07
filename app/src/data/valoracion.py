import json
from app.src.data.jugadorPerfil import *
from app import client
import app.src.utils.constants as c

cursor = client.connection.cursor()

#creates db


def insert_valoracion(data_jugador):

    query = ("INSERT INTO valoracion "
                    "(id_scout, fecha, id_visualizacion, "
                    "id_equipo, local, visitante, campeonato, id_seguimiento, "
                    "descripcion, id_jugador) "
                "VALUES(%(id_scout)s, %(fecha)s, %(id_visualizacion)s, "
                "%(id_equipo)s, %(local)s, %(visitante)s, %(campeonato)s ,%(id_seguimiento)s, "
                "%(descripcion)s, %(id_jugador)s)")
              
    cursor.execute(query, data_jugador)
    client.connection.commit()

    return {'id': cursor.lastrowid}
   