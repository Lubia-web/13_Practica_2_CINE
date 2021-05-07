import mysql.connector

connection = mysql.connector.connect(host="localhost", 
                                    user="root", 
                                    passwd="", 
                                    database="db_cinema")

cursor = connection.cursor()
query = "INSERT INTO tbl_cartelera(PELICULA,HORA,FECHA,IDIOMA)VALUES(%s,%s,%s,%s)"
data=(pelicula,hora,fecha,idioma)
cursor.execute(query, data)

connection.commit()
connection.close()