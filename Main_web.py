from DBService import DbService
from SideBar_Log import Sign, Log_in_form
from JobForm import FormsApp
import ClassiOggetto as co
import streamlit as st
from forms import business_form, Jobforms, Workform
import StreamlitWidget
import streamlit.components.v1 as components
import hydralit_components as hc
import datetime
import time

# make it look nice from the start
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
# specify the primary menu definition
menu_data = [
    {'id': 'Calendar', 'icon': "🙉", 'label': "Calendar"},
    {'id': 'Dashboard', 'icon': "fas fa-tachometer-alt", 'label': "Dashboard", 'ttip': "I'm the Dashboard tooltip!"},
    {'id': 'Forms', 'icon': "fa-thin fa-pen-fancy", 'label': "Forms"}
]
# Saving Themes
over_theme = {'txc_inactive': 'white', 'menu_background': '#ABBFE2', 'txc_active': 'yellow', 'option_active': '#506D98'}
theme_bad = {'bgcolor': '#FFF0F0', 'title_color': 'red', 'content_color': 'red', 'icon_color': 'red',
             'icon': 'fa fa-times-circle'}
theme_neutral = {'bgcolor': '#f9f9f9', 'title_color': 'orange', 'content_color': 'orange', 'icon_color': 'orange',
                 'icon': 'fa fa-question-circle'}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=False,  # will show the st hamburger as well as the navbar now!
    sticky_nav=False,  # at the top or not
    sticky_mode='jumpy',  # jumpy or not-jumpy, but sticky or pinned
    option_menu=True
)

# get the id of the menu item clicked
# st.info(f"{menu_id}")

dbs = DbService()
with st.sidebar:
    with st.container():
        name, passw = Sign(dbs=dbs)


if menu_id == "Forms":
    st.header("Registra una nuova Impresa e i lavori che svolgi!")
    st.subheader("Tieni sotto controllo il tempo che utilizzi per svolgere ogni lavoro")
    if name:
        Usr = co.User(nickname=name, password=passw)
        with hc.HyLoader('', hc.Loaders.standard_loaders, index=[3, 0, 5]):
            time.sleep(3)

            FormsApp(dbs=dbs, Usr=Usr).run()

    else:
        hc.info_card(title='Effettua il Login nel tuo Accout',
                     content='Per accedere alle funzionalità della pagina devi necessariamente registrarti '
                             'ed effettuare il Login.'
                             'Ricorda di inserire nickname e password non superiori a 10 caratteri',
                     bar_value=12,
                     theme_override=theme_bad)
        hc.info_card(title='',
                     content='Quando effettui la registrazione ricorda di inserire nickname e password non superiori '
                             'a 10 caratteri',
                     bar_value=8,
                     theme_override=theme_neutral)
        Log_in_form(dbs=dbs)
# dbs.close_conn()
