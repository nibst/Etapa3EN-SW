from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.Event import Event
from src.data.dao.AddressDao import AddressDao

class EventDao:
    """
    event data acess object
    """
    #TODO error handling of connection
    def __init__(self) -> None:
        db_connection_instance:DBConnectionSingleton = DBConnectionSingleton.get_instance()
        self.__conn = db_connection_instance.get_connection()
        self.__cur = db_connection_instance.get_cursor()
    
    def __append_participants_to_events(self,database_tuples):
        participants_dict = {}
        #populate participants dict, each key is an event_id, each value is a list of participants of that event
        for record in database_tuples:
            if record[0] not in participants_dict:
                participants_dict[record[0]] = []
            participants_dict[record[0]].append(record[12])
        
        event_id_lst = []
        events_lst = []
        for record in database_tuples:    
            if record[0] in event_id_lst:
                continue
            else:
                event_id_lst.append(record[0])
                events_lst.append((*record[:12],participants_dict[record[0]])) #record tuple without user_id + list of participants
        return events_lst

    def insert_event(self,event:Event):
        """
        insert event into database
        if there is participants in this event object, insert them into Participants TABLE
        """
        insert_script = "INSERT INTO Events (event_id, host_id, event_name, address_id, start_date, end_date, visibility, check_in, check_out, description, category, event_parent_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        if event.get_event_parent() is None:
            event_parent_id = None
        else:
            event_parent_id = event.get_event_parent().get_id()
        insert_value = (event.get_id(), event.get_host().get_id(), event.get_name(), event.get_address().get_id(),event.get_start_date(), event.get_end_date(), event.get_visibility(), event.get_check_in(), event.get_check_out(),event.get_description(),event.get_category(),event_parent_id)
        self.__cur.execute(insert_script, insert_value)
        self.insert_event_participants(event)
        self.__conn.commit()
        return event
    
    def insert_event_participants(self,event:Event):
        insert_script = "INSERT INTO Participants (user_id,event_id) VALUES (%s, %s)"
        for participant in event.get_list_of_participants():
            insert_value = (participant.get_id(),event.get_id())
            self.__cur.execute(insert_script, insert_value)
            self.__conn.commit()
        return event
    
    def print_all_events(self):
        """
        print all events, but dont print participants of the event
        """
        query_scrpit = "SELECT * FROM Events"
        self.__cur.execute(query_scrpit)
        
        for record in self.__cur.fetchall():
            print(record)
        self.__conn.commit()
        
    def get_all_events(self):
        """
        DB returns tuples like:
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,NULL 1234);
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,NULL,1236);
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,NULL,1235);
        (04,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,NULL,1238);

        i.e there is multiple tuples of the same event, just varying the user participant
        """
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) ORDER BY event_id"
        self.__cur.execute(query_scrpit)
        
        records = self.__cur.fetchall()

        events_lst = self.__append_participants_to_events(records)

        self.__conn.commit()
        return events_lst

    def get_event_by_id(self,event_id):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE event_id = %s"
        input = (event_id,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()

        return events_lst[0]

    def get_events_by_host(self,host_id):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE host_id = %s"
        input = (host_id,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()

        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst

    def get_events_by_participant(self,participant_id):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE user_id = %s;"
        input = (participant_id,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()

        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst
        

    def get_events_by_date(self,date):
        pass

    def get_events_by_name(self,name):
        """
        DB returns tuples like:
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1234);
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1236);
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1235);
        (04,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1238);

        i.e there is multiple tuples of the same event, just varying the user participant
        """
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE event_name LIKE %s ORDER BY event_id"
        name = '%' + name + '%'#get event names that have this name as prefix, suffix or in the middle of the event name
        input = (name,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst

    def get_events_by_category(self,category):
        """
        DB returns tuples like:
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1234);
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1236);
        (01,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1235);
        (04,1234,'event name',9069042560, '2023-06-03','2023-06-03',TRUE,'20:06:03','23:06:03',NULL,1238);

        i.e there is multiple tuples of the same event, just varying the user participant
        """
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE category LIKE %s ORDER BY event_id"
        name = '%' + category + '%'
        input = (name,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst

    def get_events_by_street(self,street):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE address_id IN (select address_id from Address where street like %s )"
        name = '%' + street + '%'
        input = (name,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst

    def get_events_by_city(self,city):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE address_id IN (select address_id from Address where city like %s )"
        name = '%' + city + '%'
        input = (name,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst

    def get_events_by_state(self,state):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE address_id IN (select address_id from Address where event_state like %s )"
        name = '%' + state + '%'
        input = (name,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst
    
    def get_events_by_zip_code(self,zip_code):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE address_id IN (select address_id from Address where zip_code = %s )"
        input = (zip_code,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()
        return events_lst

    def get_events_by_parent_id(self,parent_id):
        query_scrpit = "SELECT * FROM Events LEFT OUTER JOIN Participants using (event_id) WHERE event_parent_id = %s"
        input = (parent_id,)
        self.__cur.execute(query_scrpit,input)
        events_lst = []
        records = self.__cur.fetchall()
        events_lst = self.__append_participants_to_events(records)
        self.__conn.commit()

        return events_lst
    

