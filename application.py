
from flask import Flask, request
from app.src.data.catalog import get_catalog
import os
import warnings
import app.src.utils.constants as c


# Quitar warnings innecesarios de la salida
warnings.filterwarnings('ignore')

# -*- coding: utf-8 -*-
application = Flask(__name__)

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
def get_equipo(desc = ''):
    """
        Función para obtener los equipos.

        Returns:
           json. {
                id: id_equipo (numeric),
                descripcion: nombre del equipo (string)
                }
    """
    return get_catalog(c.TABLE_EQUIPO, desc )


@application.route('/catalog/perfil', methods=['GET'])
def get_perfil(desc = ''):
    """
        Función para obtener los perfiles.

        Returns:
           json. {
                id: id_perfil (numeric),
                descripcion: nombre del perfil (string)
                }
    """
    return get_catalog(c.TABLE_PERFIL, desc )


@application.route('/catalog/pie', methods=['GET'])
def get_pie(desc = ''):
    """
        Función para obtener los pies.

        Returns:
           json. {
                id: id_pie (numeric),
                descripcion: pie (string)
                }
    """
    return get_catalog(c.TABLE_PIE, desc )


@application.route('/catalog/posicion', methods=['GET'])
def get_posicion(desc = ''):
    """
        Función para obtener las posiciones.

        Returns:
           json. {
                id: id_posicion (numeric),
                descripcion: nombre de la posicion (string)
                }
    """
    return get_catalog(c.TABLE_POSICION, desc )


@application.route('/catalog/seguimiento', methods=['GET'])
def get_seguimiento(desc = ''):
    """
        Función para obtener los seguimientos.

        Returns:
           json. {
                id: id_seguimiento (numeric),
                descripcion: nombre del seguimiento (string)
                }
    """
    return get_catalog(c.TABLE_SEGUIMIENTO, desc )


@application.route('/catalog/somatotipo', methods=['GET'])
def get_somatotipo(desc = ''):
    """
        Función para obtener los somatotipos.

        Returns:
           json. {
                id: id_somatotipo (numeric),
                descripcion: nombre del somatotipo (string)
                }
    """
    return get_catalog(c.TABLE_SOMATOTIPO, desc )


@application.route('/catalog/visualizacion', methods=['GET'])
def get_visualizacion(desc = ''):
    """
        Función para obtener los tipo de visualizacion.

        Returns:
           json. {
                id: id_visualizacion (numeric),
                descripcion: nombre de la visualizacion (string)
                }
    """
    return get_catalog(c.TABLE_VISUALIZACION, desc )

# main
if __name__ == '__main__':
    # ejecución de la app
    application.run(host='0.0.0.0', port=5000, debug=False)
