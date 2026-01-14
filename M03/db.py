import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="gameuser",
        password="gamepass",
        database="juego_decisiones"
    )
    cursor = conn.cursor(dictionary=True)  # dictionary=True para obtener resultados como diccionarios

