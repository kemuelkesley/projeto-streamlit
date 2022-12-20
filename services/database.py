# Teste
# import pyodbc

# server = 'pc-gamer' 
# database = 'BancoEstudos' 
# username = 'sa' 
# password = 'bandal' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
# cursor = cnxn.cursor()

# Produção
import mysql.connector

cnxn = mysql.connector.connect(
    host="containers-us-west-155.railway.app",
    database="railway",
    port=7259,
    user="root",
    password="PDj5vmYB6AvKEKOGPbUQ"
)

# Dando um select para verificar se retorna algo
cursor = cnxn.cursor()    

cursor.execute("SELECT * FROM CLIENTES")

row = cursor.fetchall()
print(row)

