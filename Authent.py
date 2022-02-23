from TableService import UserService
from DBService import DbService
import streamlit as st
import streamlit_authenticator as stauth
import traceback
import sys


def main_authentication(DbService: DbService):
    usr_serv = UserService(DBService=DbService)
    names = usr_serv.get_users_list()
    passw = usr_serv.get_password_list()
    name = ""
    try:
        authenticator = aunthenticator(names, passw)
        name, authentication_status = authenticator.login('Login', 'main')
        authentication_msg(authentication_status=authentication_status)
    except:
        print("")
    finally:
        return name, passw


def aunthenticator(names: list, password: list):
    hashed_passwords = stauth.hasher(password).generate()
    authenticator = stauth.authenticate(names, names, hashed_passwords,
                                        'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
    return authenticator


def authentication_msg(authentication_status):
    if authentication_status is False:
        st.error("Username or Password are incorrect")
    elif authentication_status is True:
       st.success(f"User Authorized, welcome dear user ")
    elif authentication_status is None:
       st.warning("Please access to your account with a Username and Password")
    return
