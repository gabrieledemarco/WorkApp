from DBService import DbService
from SideBar_Log import Sign
import ClassiOggetto as co
import streamlit as st
from forms import business_form, Jobforms, Workform


dbs = DbService()
with st.sidebar:
    name, passw = Sign(dbs=dbs)

st.header("Controlla le tue ore di lavoro")
if name:
    with st.container():
        st.text("Registra il tuo account oppure fai il LogIn in un account esistente")

        with st.expander("Registra una nuova azienda!", expanded=False):
            state_business = business_form(dbs=dbs)

        Usr = co.User(nickname=name, password=passw)
        with st.expander("Inizia un lavoro!"):
            jf = Jobforms(Dbs=dbs, User=Usr)

        with st.expander("Registra una nuova sessione di lavoro!"):
            wf = Workform(Dbs=dbs,User=Usr)

# dbs.close_conn()
