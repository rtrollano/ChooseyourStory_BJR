import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="gameuser",
        password="gamepass",
        database="juego_decisiones"
    )
