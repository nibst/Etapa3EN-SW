from src.application.UserConverter import UserConverter
from src.data.dao.UserDao import UserDao
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.User import User
from src import login_manager
import re

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
    
    @login_manager.user_loader
    def load_user(user_id):
        user_dao = UserDao()
        user_converter = UserConverter()
        user_tuple = user_dao.get_user_by_id(user_id)
        user = user_converter.database_tuple_to_object(user_tuple)
        return user