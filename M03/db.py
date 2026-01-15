import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysqlocal",
        database="proyecto_bjr2"
    )