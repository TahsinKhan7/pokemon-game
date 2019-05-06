import pyodbc

##Variables to create a connection##
connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'Pokemon_Game_Db'
username = 'SA'
password = 'Passw0rd2018'

###Making a connection
docker_Pokemon_Game_Db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

###Creationg a cursor that can excecute SQL functions on connected database
cursor = docker_Pokemon_Game_Db.cursor()


# class PokeConnection:
#     def __init__(self):
#         #self.connection = 'Microsoft SQL Server'
#         self.server = 'localhost,1433'
#         self.database = 'Pokemon_Game_Db'
#         self.username = 'SA'
#         self.password = 'Passw0rd2018'
#         self.docker_Pokemon_Game_Db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
#         self.cursor = self.docker_Pokemon_Game_Db.cursor()