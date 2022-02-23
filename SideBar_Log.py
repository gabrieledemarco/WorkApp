import streamlit as st
from TableService import UserService
from DBService import DbService
from Authent import main_authentication
from ClassiOggetto import User


def Sign(dbs: DbService):
    auth = st.container()

    with auth:
        Sign_request = auth.expander(label="Iscriviti", expanded=False)
        with Sign_request:
            Sign_up(dbs=dbs)
        Log_request = auth.expander(label="Connetti al tuo account", expanded=False)
        with Log_request:
            name, passw = Log_in_form(dbs)

    return name, passw


def Sign_up(dbs: DbService):
    New_user_Registration = st.form(key="New_user_Registration", clear_on_submit=True)

    with New_user_Registration:
        with st.container():
            c11, c12 = st.columns(2)
            with c11:
                nick = st.text_input(label="Nickname", max_chars=10)
            with c12:
                password = st.text_input(label="Password", max_chars=10, type="password")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            usr = User(nickname=nick, password=password)
            usr_srv = UserService(User=usr, DBService=dbs)
            if not usr_srv.is_user_registered():
                usr_srv.insert()
                st.success(f"Ciao {nick}, hai effettuato la registrazione con successo")
            elif usr_srv.is_user_registered():
                st.error(f"Ci spiace ma {nick} è già presente, scegli un altro nickname")
            else:
                st.warning("Ci spiace ma qualcosa è andato storto")
    return


def Log_in_form(dbs: DbService):
    try:
        return main_authentication(DbService=dbs)
    except Exception as ex:
        print(ex)
