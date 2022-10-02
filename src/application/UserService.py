from src.application.UserConverter import UserConverter
from src.data.dao.UserDao import UserDao
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.User import User
from src import login_manager
import re
from src.application.QR_Code import cria_qr

class UserService:
    
    def __init__(self) -> None:
        pass 
    
    def create_user(self,user:User):
        #regex for email
        #shorter version of the RFC 5322-compliant Regular Expression 
        regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        if  re.match(regex,user.get_email()) is None:
            raise Exception("Email not valid")
        user_dao = UserDao()
        try:
            user_dao.insert_user(user)
        except Exception as e:
            #probably user already exist
            DBConnectionSingleton.rollback()
            raise(e)
        return user
    
    def login(self,email,password):
        user_dao = UserDao()
        user = user_dao.get_user_by_email(email)
        user_converter = UserConverter()
        user = user_converter.database_tuple_to_object(user)
        #TODO maybe raise one unique exception for email and password (more security)
        #TODO transform user in User object before doing logic to it
        if user is None:
            raise Exception("Invalid Email")
        if user.get_password() != password: 
            raise Exception("Invalid Password")
        return user

    def get_user_by_id(self,user_id):
        """
        get actual User object by user id
        """
        user_dao = UserDao()
        user = user_dao.get_user_by_id(user_id)
        user_converter = UserConverter()
        user = user_converter.database_tuple_to_object(user)
        return user

    def get_user_by_email(self,email):
        """
        get actual User object by user email
        """
        user_dao = UserDao()
        user = user_dao.get_user_by_email(email)
        user_converter = UserConverter()
        user = user_converter.database_tuple_to_object(user)
        return user

    def check_in(self,event_id,user_id):
        """
        do check in of an user in an event
        """
        user_dao = UserDao()
        try:
            nr_rows_updated = user_dao.check_in(event_id,user_id)
        except Exception as e:
            DBConnectionSingleton.rollback()
            raise e
        return nr_rows_updated

    def check_out(self,event_id,user_id):
        """
        do check out of an user in an event
        """

    def has_checked_in(self,event_id,user_id):
        """
        check if user has checked in event
        """
        user_dao = UserDao()
        return user_dao.has_checked_in(event_id,user_id)

    def subscribe_to_event(self,event_id,user_id):    
        """"
        puts user in participants list of an event
        """
        user_dao = UserDao()
        try:
            nr_rows_inserted = user_dao.insert_user_as_participant_of_event(event_id,user_id)
        except Exception as error:
            DBConnectionSingleton.rollback()
            raise error
        return nr_rows_inserted



    @login_manager.user_loader
    def load_user(user_id):
        user_service = UserService()
        user = user_service.get_user_by_id(user_id)
        return user

    