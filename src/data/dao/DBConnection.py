
import psycopg2

class DBConnectionSingleton:
    __instance = None
    def __init__(self):
        if DBConnectionSingleton.__instance is None:
            #TODO connect parameters in a config file
            self.__conn =  psycopg2.connect(dbname='event_manager', user='postgres', password='123', host='localhost', port='5432')
            self.__cur = self.__conn.cursor()     
            DBConnectionSingleton.__instance = self
        else:
            return DBConnectionSingleton.__instance

    @staticmethod
    def get_instance():
        if DBConnectionSingleton.__instance is None:
            DBConnectionSingleton.__instance = DBConnectionSingleton()
        return DBConnectionSingleton.__instance

    def get_connection(self):
        return self.__conn

    def get_cursor(self):
        return self.__cur

    def destroyer():
        DBConnectionSingleton.get_instance().__cur.close()
        DBConnectionSingleton.get_instance().__conn.close()
        DBConnectionSingleton.__instance = None
