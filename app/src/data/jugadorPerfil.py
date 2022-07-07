import json
from app import client
import app.src.utils.constants as c

cursor = client.connection.cursor()



    
def get_jugador_perfiles(id_jugador):
    row_headers = ["id", "descripcion"]
    query = """SELECT 	p.id_perfil id, 
                        p.descripcion descripcion 
                FROM 
                        perfil p join
                        jugador_perfil jp on (p.id_perfil = jp.id_perfil)
                where 
                        jp.id_jugador={}""".format( id_jugador)
    cursor.execute(query)
    rows = cursor.fetchall()
    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    return json_data


def insert_jugador_perfil(id_jugador, perfiles):

    for perfil_id in perfiles:
        query =("""INSERT INTO jugador_perfil
                    (id_jugador,
                    id_perfil)
                    VALUES
                    ({}, {})""").format(id_jugador, perfil_id)
        cursor.execute(query)
    client.connection.commit()
    
def delete_jugador_perfil(perfiles):
    for perfil_id in perfiles:
        query =("""DELETE FROM jugador_perfil WHERE id_perfil={}""").format(perfil_id)
        cursor.execute(query)
    client.connection.commit()



def update_jugador_perfil(id_jugador, perfiles):
    jugador_perfil = get_jugador_perfiles(id_jugador)
    perfiles_old = [item['id'] for item in jugador_perfil]
    perfiles_delete = list(set(perfiles_old) - set(perfiles))
    perfiles_add = list(set(perfiles) - set(perfiles_old))
    delete_jugador_perfil(perfiles_delete)
    insert_jugador_perfil(id_jugador, perfiles_add)