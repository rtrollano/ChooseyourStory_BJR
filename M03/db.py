import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="pruebas",
        password="proyecto_bjr",
        database="proyecto_bjr"
    )