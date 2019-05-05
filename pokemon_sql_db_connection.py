import pyodbc

class PokeConnection:
    def __init__(self):
        #self.connection = 'Microsoft SQL Server'
        self.server = 'localhost,1433'
        self.database = 'Pokemon_Game_Db'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_db_instance = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursors = self.docker_db_instance.cursor()