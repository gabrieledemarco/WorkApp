import streamlit as st
from DBService import DbService
from TableService import BusinessService, UserService, Jobs_Service, Works_Service
from ClassiOggetto import Business, User, Jobs, Work
import StreamlitService as Stserv


def business_form(dbs: DbService):
    st.text("Inserisci una nuova azienda")
    New_user_Registration = st.form(key="New_business_Registration", clear_on_submit=True)
    state = None
    with New_user_Registration:
        with st.container():
            azienda = st.text_input(label="Inserisci una nuova azienda", max_chars=15)
            desc = st.text_input(label="Inserisci una descrizione per questa azienda azienda", max_chars=144)

        submit_button = st.form_submit_button(label='Registra questa azienda')

        if submit_button:
            business_class = Business(name=azienda, descr=desc)
            business_srv = BusinessService(DBService=dbs, Business=business_class)
            if not business_srv.is_business_registered():
                business_srv.insert()
                st.success("Hai registrato correttamente una nuova azienda")
                state = True
            elif business_srv.is_business_registered():
                st.error(f"Hai già registrato questa azienda")
                state = False
            else:
                st.warning("Ci spiace ma qualcosa è andato storto")
                state = False

    return state


def Jobforms(Dbs: DbService, User: User):
    st.text("Inserisci un nuovo lavoro")

    # -- Get Id logged User
    usrsrv = UserService(User=User, DBService=Dbs)
    id_user = usrsrv.get_user_id()[0]

    # -- Get list of Business
    bs = BusinessService(DBService=Dbs)
    bsl = bs.get_business_list()

    # -- Form Statement
    JobForm = st.form(key="JobForm", clear_on_submit=True)

    with JobForm:
        with st.container():
            c1, c2 = st.columns([1, 1])
            with c1:
                azienda = st.selectbox(label="Seleziona l'azienda per cui lavori", options=bsl)
                start_date = st.date_input(label="Scegli la data di partenza del lavoro", help="AAAA/MM/GG")
                h_payment = st.text_input(label="Inserisci il tuo pagamento orario")
            with c2:
                job_name = st.text_input(label="Inserisci un nome per questo lavoro")
                end_date = st.date_input(label="Scegli la data di termine del lavoro", help="AAAA/MM/GG")
                descr = st.text_input(label="Definisci il lavoro", help="Campo facoltativa")

        with st.container():
            button = st.form_submit_button(label="Aggiungi")
            if button:
                # -- Get id selected business
                Bus_class = Business(name=azienda)
                bs = BusinessService(DBService=Dbs, Business=Bus_class)
                id_busi = bs.get_business_id()[0]
                try:
                    job_class = Jobs(Business=Bus_class,
                                     User=User,
                                     start_date=start_date,
                                     end_date=end_date,
                                     h_payment=h_payment,
                                     descr=descr,
                                     job_name=job_name)

                    jobs_srv = Jobs_Service(id_user=id_user, business_id=id_busi, DBService=Dbs, Jobs=job_class)
                    jobs_srv.insert()

                    st.success("Hai registrato correttamente un nuovo lavoro")
                except Exception as ex:
                    st.warning("Ops... Qualcosa è andato storto Job Form")
                    st.text(ex)
    return


def Workform(Dbs: DbService, User: User):
    st.text("")

    # -- Get Id logged User
    usrsrv = UserService(User=User, DBService=Dbs)
    id_user = usrsrv.get_user_id()[0]

    # -- Get list of Business
    bs = BusinessService(DBService=Dbs)
    bsl = bs.get_business_list()

    # -- Form Statement
    workForm = st.form(key="workForm", clear_on_submit=True)

    with workForm:
        with st.container():
            c1, c2 = st.columns([1, 1])
            with c1:
                azienda = st.selectbox(label="Seleziona l'azienda per cui lavori", options=bsl)
                date = st.date_input(label="Scegli una data", help="AAAA/MM/GG")

            with c2:
                # -- Get id selected business
                Bus_class = Business(name=azienda)
                bs = BusinessService(DBService=Dbs, Business=Bus_class)
                id_busi = bs.get_business_id()[0]

                # -- Get Job List per selected Business
                jobsrv = Jobs_Service(DBService=Dbs, id_user=id_user, business_id=id_busi)
                job_list = jobsrv.get_job_list()

                job_name = st.selectbox(label="Seleziona il lavoro che stai svolgendo", options=job_list)
                descr = st.text_input(label="Dai una descrizione a questa sessione", help="Campo facoltativa")

        # Orari di entrata e di uscita
        entry = Stserv.Insert_time_Slider(data=date, title="Inserisci un orario di entrata")
        exit = Stserv.Insert_time_Slider(data=date, title="Inserisci un orario di uscita")

        # -- Get Selected Job id
        job = Jobs(job_name=job_name, User=User)
        jobsrv = Jobs_Service(DBService=Dbs, id_user=id_user, business_id=id_busi, Jobs=job)
        job_id = jobsrv.get_jobs_id()[0]

        # -- Get id selected business
        Bus_class = Business(name=azienda)
        bs = BusinessService(DBService=Dbs, Business=Bus_class)
        id_busi = bs.get_business_id()[0]

        with st.container():
            button = st.form_submit_button(label="Aggiungi")
            if button:

                try:
                    wrk = Work(data=date, H_start=entry, H_end=exit, desc=descr)
                    wrk_serv = Works_Service(id_user=id_user,
                                             id_business=id_busi,
                                             jobs_id=job_id,
                                             DBService=Dbs,
                                             work=wrk)
                    wrk_serv.insert()
                    st.success("Hai registrato correttamente una nuova sessione di lavoro")
                    st.balloons()
                except Exception as ex:
                    st.warning("Ops... Qualcosa è andato storto Work Form")
                    st.text(ex)
    return
