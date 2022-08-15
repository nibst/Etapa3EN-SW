import psycopg2
from src.data.Event import Event
class EventDaoSingleton:
    """
    Singleton for event data acess object
    """
    #TODO error handling of connection
    __eventDao = None    
    def __init__(self) -> None:
        if EventDaoSingleton.__eventDao is None:
            #TODO connect parameters in a config file
            self.__conn =  psycopg2.connect(dbname='event_manager', user='postgres', password='123', host='localhost', port='5432')
            self.__cur = self.__conn.cursor()     
            EventDaoSingleton.__eventDao = self
        else:
            raise Exception("EventDaoSingleton is a singleton")#TODO, create class for exception

    @staticmethod
    def get_event_dao():
        if EventDaoSingleton.__eventDao is None:
            EventDaoSingleton.__eventDao = EventDaoSingleton()
        return EventDaoSingleton.__eventDao
    
    def get_conn(self):
        return self.__conn
    
    def insert_event(self,event:Event):
        inser_script = "INSERT INTO Events (event_id, host_id, event_name, address_id, start_date, end_date, visibility, check_in, check_out, event_parent_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        if event.get_event_parent() is None:
            event_parent_id = None
        else:
            event_parent_id = event.get_event_parent().get_id()

        insert_value = (event.get_id(), event.get_host().get_id(), event.get_name(), event.get_address().get_id(),event.get_start_date(), event.get_end_date(), event.get_visibility(), event.get_check_in(), event.get_check_out(),event_parent_id)
        self.__cur.execute(inser_script, insert_value)
        self.__conn.commit()
        return event.get_id()
        

    def print_all_events(self):
        select_scrpit = "SELECT * FROM Events"
        self.__cur.execute(select_scrpit)
        for record in self.__cur.fetchall():
            print(record)
        self.__conn.commit()

    def get_event_by_id(self,event_id):
        pass

    def get_events_by_user(self,user_id):
        pass

    def get_events_by_date(self,date):
        pass

    def get_events_by_name(self,name):
        pass

    def get_events_by_address(self,address):
        pass

    def destroyer():
        EventDaoSingleton.get_event_dao().__cur.close()
        EventDaoSingleton.get_event_dao().__conn.close()
        EventDaoSingleton.__eventDao = None

