import json
from app import client

cursor = client.connection.cursor()

#creates db
def get_catalog(table, desc):
    row_headers = ['id', 'descripcion']
    query = """Select * from {} 
                where lower(descripcion) like lower('{}%') 
                order by descripcion""".format(table, desc if desc else '')
    return execute_query(query, row_headers)

def get_paises(pais):
    row_headers = ['id', 'nombre', 'codigoISO2', 'codigoISO3']
    query = """Select id_pais, nombre, codigoISO2, codigoISO3 
                    from pais 
                    where lower(nombre) like lower('{}%') 
                    order by nombre""".format(pais if pais else '')
    return execute_query(query, row_headers)

def execute_query(query, row_headers):
    cursor.execute(query)
    rows = cursor.fetchall()

    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data, ensure_ascii=False).encode('utf8')