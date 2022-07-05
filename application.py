
from flask import Flask, request
from flask_cors import CORS
from app.src.data.catalog import get_catalog, get_paises
import os
import warnings
import app.src.utils.constants as c


# Quitar warnings innecesarios de la salida
warnings.filterwarnings('ignore')

# -*- coding: utf-8 -*-
application = Flask(__name__)
CORS(application)

# usando el decorador @app.route para gestionar los enrutadores (Método GET)
@application.route('/', methods=['GET'])
def root():
    """
        Función para gestionar la salida de la ruta raíz.

        Returns:
           dict.  Mensaje de salida
    """
    return "{'Proyecto':'Futbol'}"


@application.route('/catalog/equipo', methods=['GET'])
def get_equipo():
    """
        Función para obtener los equipos.

        Returns:
           json. {
                id: id_equipo (numeric),
                descripcion: nombre del equipo (string)
                }
    """
    args = request.args
    desc = args.get(c.URL_PARAM_DESCRIPCION)
    return get_catalog(c.TABLE_EQUIPO, desc )


@application.route('/catalog/perfil', methods=['GET'])
def get_perfil():
    """
        Función para obtener los perfiles.

        Returns:
           json. {
                id: id_perfil (numeric),
                descripcion: nombre del perfil (string)
                }
    """
    args = request.args
    desc = args.get(c.URL_PARAM_DESCRIPCION)
    return get_catalog(c.TABLE_PERFIL, desc )


@application.route('/catalog/pie', methods=['GET'])
def get_pie():
    """
        Función para obtener los pies.

        Returns:
           json. {
                id: id_pie (numeric),
                descripcion: pie (string)
                }
    """
    args = request.args
    desc = args.get(c.URL_PARAM_DESCRIPCION)
    return get_catalog(c.TABLE_PIE, desc )


@application.route('/catalog/posicion', methods=['GET'])
def get_posicion():
    """
        Función para obtener las posiciones.

        Returns:
           json. {
                id: id_posicion (numeric),
                descripcion: nombre de la posicion (string)
                }
    """
    args = request.args
    desc = args.get(c.URL_PARAM_DESCRIPCION)
    return get_catalog(c.TABLE_POSICION, desc )


@application.route('/catalog/seguimiento', methods=['GET'])
def get_seguimiento():
    """
        Función para obtener los seguimientos.

        Returns:
           json. {
                id: id_seguimiento (numeric),
                descripcion: nombre del seguimiento (string)
                }
    """
    args = request.args
    desc = args.get(c.URL_PARAM_DESCRIPCION)
    return get_catalog(c.TABLE_SEGUIMIENTO, desc )


@application.route('/catalog/somatotipo', methods=['GET'])
def get_somatotipo():
    """
        Función para obtener los somatotipos.

        Returns:
           json. {
                id: id_somatotipo (numeric),
                descripcion: nombre del somatotipo (string)
                }
    """
    args = request.args
    desc = args.get(c.URL_PARAM_DESCRIPCION)
    return get_catalog(c.TABLE_SOMATOTIPO, desc )


@application.route('/catalog/visualizacion', methods=['GET'])
def get_visualizacion():
    """
        Función para obtener los tipo de visualizacion.

        Returns:
           json. {
                id: id_visualizacion (numeric),
                descripcion: nombre de la visualizacion (string)
                }
    """
    args = request.args
    desc = args.get(c.URL_PARAM_DESCRIPCION)
    return get_catalog(c.TABLE_VISUALIZACION, desc )

@application.route('/catalog/pais', methods=['GET'])
def get_pais():
    """
        Función para obtener los paises.

        Returns:
           json. {
                id: id_pais (numeric),
                nombre: nombre del pais (string)
                codigoISO2: codigoISO2 (string)
                codigoISO3: codigoISO3 (string)
                }
    """
    args = request.args
    pais = args.get(c.URL_PARAM_NOMBRE)
    return get_paises(pais )

# main
if __name__ == '__main__':
    # ejecución de la app
    application.run(host='0.0.0.0', port=os.environ[c.APP_PORT], debug=False)
