from app import client
import app.src.utils.constants as c

cursor = client.connection.cursor()

#creates db
def get_jugador(params):
    row_headers = ["id_jugador", "nombre", "apodo", "anio", "id_equipo", "des_equipo", 
    "numero", "id_pie", "des_pie", "id_somatotipo", "des_somatotipo", "estatura", 
    "id_pais", "nombre_pais", "id_pais_nacionalidad", "nombre_nacionalidad", 
    "id_posicion1", "des_posicion1", "id_posicion2", "des_posicion2"]
   
    query = """ SELECT  j.id_jugador,
                        j.nombre,
                        apodo,
                        anio,
                        eq.id_equipo,
                        eq.descripcion des_equipo,
                        numero,
                        pie.id_pie,
                        pie.descripcion des_pie,
                        som.id_somatotipo,
                        som.descripcion des_somatotipo,
                        estatura,
                        p.id_pais,
                        p.nombre nombre_pais,
                        nac.id_pais id_pais_nacionalidad,
                        nac.nombre nombre_nacionalidad,
                        pos.id_posicion,
                        pos.descripcion des_posicion1,
                        pos2.id_posicion,    
                        pos2.descripcion des_posicion2
                    FROM jugador j 
                        join equipo eq on (j.id_equipo = eq.id_equipo)
                        join pie pie on (j.id_pie = pie.id_pie)
                        join somatotipo som on (j.id_somatotipo = som.id_somatotipo)
                        join pais p  on (j.id_pais = p.id_pais)
                        join pais nac on (j.id_pais_nacionalidad=nac.id_pais)
                        join posicion pos  on (j.id_posicion1 = pos.id_posicion)
                        join posicion pos2 on (j.id_posicion2=pos2.id_posicion)
                    WHERE
                        j.id_jugador={}"""\
                        .format( params[c.URL_PARAM_ID])
    return client.execute_query_one(query, row_headers)
    

def get_min_jugador(params):
    row_headers = ["id_jugador", "nombre"]
    sql_headers = "id_jugador, nombre"
    if c.URL_PARAM_ID in params:
        print("select {} from jugador where id_jugador={}".format( sql_headers, params[c.URL_PARAM_ID]))
        
    else:
        query = """Select {} from jugador
                    where lower(nombre) like lower('{}%') 
                    order by nombre"""\
                        .format( sql_headers, params[c.URL_PARAM_NOMBRE] if c.URL_PARAM_NOMBRE in params else '')
        return client.execute_query_multi(query, row_headers)
    

def insert_jugador(data_jugador):
    query = ("INSERT INTO jugador "
              "(nombre, apodo, anio, id_equipo, numero, id_pie, id_somatotipo, estatura, "
              "id_pais, id_pais_nacionalidad, id_posicion1, id_posicion2) "
              "VALUES (%(nombre)s, %(apodo)s, %(anio)s, %(id_equipo)s, %(numero)s, %(id_pie)s, "
              "%(id_somatotipo)s, %(estatura)s, %(id_pais)s, %(id_pais_nacionalidad)s, "
              "%(id_posicion1)s, %(id_posicion2)s)")
    print(data_jugador)
    cursor.execute(query, data_jugador)
    client.connection.commit()
    new_jugador = get_min_jugador({'id': cursor.lastrowid})
    print(new_jugador)
    return new_jugador

