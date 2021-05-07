import mysql.connector

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db_cinema")
        return connection 
    def insert_db(self,pelicula,hora,fecha,idioma):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query= "INSERT INTO tbl_cartelera(PELICULA,HORA,FECHA,IDIOMA) VALUES(%s,%s,%s,%s)"
        data=(pelicula,hora,fecha,idioma)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()