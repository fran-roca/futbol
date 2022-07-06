import json
import app.src.utils.constants as c
from app import client


#creates db
def get_catalog(table, params):
    row_headers = ['id', 'descripcion']
    if c.URL_PARAM_ID in params:
        query= """Select id_{}, descripcion from {} 
                    where id_{}={}""".format(table, table, table, params[c.URL_PARAM_ID])
        return client.execute_query_one(query, row_headers)
    else:
        desc = params[c.URL_PARAM_DESCRIPCION] if c.URL_PARAM_DESCRIPCION in params else ''
        query = """Select * from {} 
                    where lower(descripcion) like lower('{}%') 
                    order by descripcion""".format(table, desc if desc else '')
        return client.execute_query_multi(query, row_headers)

def get_paises(params):
    row_headers = ['id', 'nombre', 'codigoISO2', 'codigoISO3']
    sql_headers = "Select id_pais, nombre, codigoISO2, codigoISO3 "
    if c.URL_PARAM_ID in params:
        query = """ {} from pais 
                    where id_pais={}
                    order by nombre""".format(sql_headers, params[c.URL_PARAM_ID])
        return client.execute_query_one(query, row_headers)
    else:
        query = """ {} from pais 
                        where lower(nombre) like lower('{}%') 
                        order by nombre""".format(sql_headers, params[c.URL_PARAM_NOMBRE] if c.URL_PARAM_NOMBRE in params else '')
        return client.execute_query_multi(query, row_headers)