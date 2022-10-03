from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.User import User
class UserDao:
    """
    user data acess object
    """
    #TODO error handling of connection
    def __init__(self) -> None:
        db_connection_instance:DBConnectionSingleton = DBConnectionSingleton.get_instance()
        self.__conn = db_connection_instance.get_connection()
        self.__cur = db_connection_instance.get_cursor()

    def __append_user_to_userlist(self,database_tuples):
        users_dict = {}
        #populate participants dict, each key is an event_id, each value is a list of participants of that event
        for record in database_tuples:
            if record[0] not in users_dict:
                users_dict[record[0]] = []
            users_dict[record[0]].append(record[3])
        
        user_id_lst = []
        users_lst = []
        for record in database_tuples:    
            if record[0] in user_id_lst:
                continue
            else:
                user_id_lst.append(record[0])
                users_lst.append((*record[:3],users_dict[record[0]])) #record tuple without user_id + list of participants
        return users_lst
    
    def insert_user(self,user:User):
        inser_script = "INSERT INTO Users (user_id,user_name,email,passw) VALUES (%s, %s, %s,%s)"

        insert_value = (user.get_id(), user.get_username(),user.get_email(),user.get_password())
        self.__cur.execute(inser_script, insert_value)
        self.__conn.commit()

        return user
    def get_user_by_email(self,email):

        query_script = "SELECT * FROM Users WHERE email = %s"
        self.__cur.execute(query_script, (email,))
        user = self.__cur.fetchone()
        self.__conn.commit()
        return user
    def get_user_by_id(self,id):

        query_script = "SELECT * FROM Users WHERE user_id = %s"
        self.__cur.execute(query_script, (id,))
        user = self.__cur.fetchone()
        self.__conn.commit()
        return user

    def print_all_users(self):
        query_script = "SELECT * FROM Users;"
        self.__cur.execute(query_script)
        for record in self.__cur.fetchall():
            print(record)
        self.__conn.commit()

    def get_all_users(self):
        query_script = "SELECT * FROM Users;"
        self.__cur.execute(query_script)
        
        records = self.__cur.fetchall()

        users_lst = self.__append_user_to_userlist(records)

        self.__conn.commit()
        return users_lst

    def delete_by_email(self,email):
        delete_script = "DELETE FROM Users WHERE email = %s"
        self.__cur.execute(delete_script, (email,))
        self.__conn.commit()
        return self.__cur.rowcount
    
    def check_in(self,event_id,user_id):
        update_script = "UPDATE Participants SET has_checked_in = true WHERE event_id = %s and user_id = %s"
        self.__cur.execute(update_script, (event_id,user_id))
        self.__conn.commit()
        if self.__cur.rowcount == 0:
            raise Exception("Event invalid or User has not subscribed to event previously")
        return self.__cur.rowcount

    def check_out(self,event_id,user_id):
        update_script = "UPDATE Participants SET has_checked_out = true WHERE event_id = %s and user_id = %s"
        self.__cur.execute(update_script, (event_id,user_id))
        self.__conn.commit()
        if self.__cur.rowcount == 0:
            raise Exception("Event invalid or User has not subscribed to event previously")
        return self.__cur.rowcount


    def has_checked_in(self,event_id,user_id):
        query_script = "SELECT has_checked_in FROM Participants WHERE event_id = %s and user_id = %s"
 
        self.__cur.execute(query_script, (event_id,user_id))
        tuple = self.__cur.fetchone()

        if tuple is not None and tuple[0] == True:
            has_checked_in = True
        else:
            has_checked_in = False
        self.__conn.commit()
        return has_checked_in

    def has_checked_out(self,event_id,user_id):
        query_script = "SELECT has_checked_out FROM Participants WHERE event_id = %s and user_id = %s"
 
        self.__cur.execute(query_script, (event_id,user_id))
        tuple = self.__cur.fetchone()

        if tuple is not None and tuple[0] == True:
            has_checked_out = True
        else:
            has_checked_out = False
        self.__conn.commit()
        return has_checked_out

        
    def insert_user_as_participant_of_event(self,event_id,user_id):
        insert_script = "INSERT INTO Participants (event_id,user_id) VALUES (%s, %s)"
        
        insert_value = (event_id,user_id)
        self.__cur.execute(insert_script, insert_value)
        self.__conn.commit()

        return self.__cur.rowcount