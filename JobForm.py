from DBService import DbService
from ClassiOggetto import User
import streamlit as st
from forms import business_form, Jobforms, Workform


class FormsApp():
    def __init__(self, dbs: DbService, Usr=User):
        self.dbs = dbs
        self.Usr = Usr

    def run(self):
        with st.expander("Registra una nuova azienda!", expanded=False):
            business_form(dbs=self.dbs)
        with st.expander("Inizia un lavoro!", expanded=False):
            Jobforms(Dbs=self.dbs, User=self.Usr)
        with st.expander("Registra una nuova sessione di lavoro!", expanded=False):
            Workform(Dbs=self.dbs, User=self.Usr)
