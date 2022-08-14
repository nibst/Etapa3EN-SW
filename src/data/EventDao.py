import psycopg2
from src.data.Event import Event
class EventDaoSingleton:
    """
    Singleton for event daos
    """
    #TODO error handling of connection
    __eventDao = None    
    __conn =  psycopg2.connect(dbname='event_manager', user='postgres', password='123', host='localhost', port='5432')
    __cur = __conn.cursor()     
    def __init__(self) -> None:
        if EventDaoSingleton.__eventDao is None:
            EventDaoSingleton.__eventDao = self
        else:
            raise Exception("EventDaoSingleton is a singleton")#TODO, create class for exception

    @staticmethod
    def get_event_dao():
        if EventDaoSingleton.__eventDao is None:
            EventDaoSingleton.__eventDao = EventDaoSingleton()
        return EventDaoSingleton.__eventDao
    
    def get_conn():
        return EventDaoSingleton.__conn
    
    def insert_event(event:Event):
        inser_script = "INSERT INTO Events (event_id, host_id, event_name, address_id, start_date, end_date, visibility, check_in, check_out, event_parent_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        insert_value = (event.get_id(), event.get_host().get_id(), event.get_name(), event.get_address().get_id(), event.get_start_date(), event.get_end_date(), event.get_visibility(), event.get_check_in(), event.get_check_out(), event.get_event_parent().get_id())
        EventDaoSingleton.__cur.execute(inser_script, insert_value)
        EventDaoSingleton.__conn.commit()
        return event.get_id()
        
    def get_event(event_id):
        pass

    def get_events_by_user(user_id):
        pass

    def get_events_by_date(date):
        pass

    def get_events_by_name(name):
        pass

    def get_events_by_address(address):
        pass

    def destroyer():
        EventDaoSingleton.get_event_dao().__cur.close()
        EventDaoSingleton.get_event_dao().__conn.close()
        EventDaoSingleton.__eventDao = None

