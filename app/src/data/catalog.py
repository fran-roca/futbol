import json
from app import client

cursor = client.connection.cursor()

#creates db
def get_catalog(table, desc):
    row_headers = ['id', 'descripcion']
    query = "Select * from {} where descripcion like '{}%'".format(table, desc)
    cursor.execute(query)
    rows = cursor.fetchall()

    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data, ensure_ascii=False).encode('utf8')
