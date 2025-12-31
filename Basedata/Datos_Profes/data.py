import mysql.connector

def conectar_db():
    conectar=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )

    con=conectar.cursor()

    sql="SELECT * FROM usuario where rol='Profesor'"
    con.execute(sql)
    resultado=con.fetchall()

    for i in resultado:
        print(i)    





    conectar.close()    
    return resultado



