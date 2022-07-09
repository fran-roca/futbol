import json
from app.src.data.jugadorPerfil import *
from app import client
import app.src.utils.constants as c

cursor = client.connection.cursor()


def get_valoracion(params):
    row_headers = ["id_valoracion", "id_scout", "descripcion_scout", "fecha", "id_visualizacion", 
    "descripcion_visualizacion", "id_equipo", "descripcion_equipo", "id_local", 
    "descripcion_local", "id_visitante", "descripcion_visitante", "campeonato", 
    "id_seguimiento", "descripcion_seguimiento", "descripcion", "id_jugador"]
    query = """ SELECT val.id_valoracion,
                    sco.id_scout,
                    sco.descripcion descripcion_scout,
                    fecha,
                    visu.id_visualizacion,
                    visu.descripcion descripcion_visualizacion,
                    equ.id_equipo id_equipo,
                    equ.descripcion descripcion_equipo,
                    loc.id_equipo id_local,
                    loc.descripcion descripcion_local,
                    visi.id_equipo id_visitante,
                    visi.descripcion descripcion_visitante,
                    campeonato,
                    seg.id_seguimiento,
                    seg.descripcion descripcion_seguimiento,
                    val.descripcion,
                    val.id_jugador 
                FROM valoracion val
                    join scout sco on (sco.id_scout = val.id_scout)
                    join visualizacion visu on (visu.id_visualizacion = val.id_visualizacion)
                    join equipo equ on (equ.id_equipo = val.id_equipo)
                    join equipo loc on (loc.id_equipo = val.local)
                    join equipo visi on (visi.id_equipo = val.visitante)
                    join seguimiento seg on (seg.id_seguimiento = val.id_seguimiento) """

    if c.URL_PARAM_ID_VALORACION in params:
        query += "where val.id_valoracion in ({})".format( params[c.URL_PARAM_ID_VALORACION])
    elif c.URL_PARAM_ID_JUGADOR in params:
        query += "where val.id_jugador={}".format( params[c.URL_PARAM_ID_JUGADOR])

    return client.execute_query_multi(query, row_headers)


def insert_valoracion(data_jugador):

    query = ("INSERT INTO valoracion "
                    "(id_scout, fecha, id_visualizacion, "
                    "id_equipo, local, visitante, campeonato, id_seguimiento, "
                    "descripcion, id_jugador) "
                "VALUES(%(id_scout)s, %(fecha)s, %(id_visualizacion)s, "
                "%(id_equipo)s, %(id_local)s, %(id_visitante)s, %(campeonato)s ,%(id_seguimiento)s, "
                "%(descripcion)s, %(id_jugador)s)")
              
    cursor.execute(query, data_jugador)
    client.connection.commit()

    return {'id': cursor.lastrowid}
   