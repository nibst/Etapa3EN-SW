
import psycopg2

class DBConnectionSingleton:
    __connection = None
    def __init__(self):
        if DBConnectionSingleton.__connection is None:
            #TODO connect parameters in a config file
            self.__conn =  psycopg2.connect(dbname='event_manager', user='postgres', password='123', host='localhost', port='5432')
            self.__cur = self.__conn.cursor()     
            DBConnectionSingleton.__connection = self
        else:
            raise Exception("DBConnectionSingleton is a singleton")#TODO, create class for exception

    @staticmethod
    def get_singleton():
        if DBConnectionSingleton.__connection is None:
            DBConnectionSingleton.__connection = DBConnectionSingleton()
        return DBConnectionSingleton.__connection
    
    def get_connection(self):
        return self.__conn
    def get_cursor(self):
        return self.__cur
    def destroyer():
        DBConnectionSingleton.get_singleton().__cur.close()
        DBConnectionSingleton.get_singleton().__conn.close()
        DBConnectionSingleton.__connection = None
