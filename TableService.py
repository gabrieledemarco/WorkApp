from DBService import DbService
from ClassiOggetto import User, Jobs, Business, Work


class UserService:
    def __init__(self, DBService: DbService, User: User = None):
        self.User = User  # -- User Object Class
        self.DbSer = DBService  # -- Db Connection Object Class
        self.Table = "users"  # -- Table Name
        self.Columns = DBService.name_columns(name_table=self.Table)  # -- Table Column Names

    def get_user_id(self):
        return self.DbSer.get_select_with_where(select_columns=self.Columns[0],
                                                name_table=self.Table,
                                                where_columns=self.Columns[1],
                                                values_column=self.User.Nickname)

    def is_user_registered(self):
        usr = self.get_user_id()
        if len(usr) == 0:
            return False
        else:
            return True

    def get_users_list(self):
        return self.DbSer.get_all_value_in_column(name_column=self.Columns[1],
                                                  name_table=self.Table)

    def get_password_list(self):
        return self.DbSer.get_all_value_in_column(name_column=self.Columns[2],
                                                  name_table=self.Table)

    def insert(self):
        if self.is_user_registered:
            try:
                self.DbSer.insert(self.Table, list_record=[(self.User.Nickname, self.User.Password)])
            except Exception as ex:
                print(f"Errore durante l'inserimento {ex}")
        else:
            return print(f"User is registered with {self.get_user_id()[0]}")


class BusinessService:
    def __init__(self, DBService: DbService, Business: Business = None):
        self.Business = Business  # -- User Object Class
        self.DbSer = DBService  # -- Db Connection Object Class
        self.Table = "business"  # -- Table Name
        self.Columns = DBService.name_columns(name_table=self.Table)  # -- Table Column Names

    def get_business_id(self):
        return self.DbSer.get_select_with_where(select_columns=self.Columns[0],
                                                name_table=self.Table,
                                                where_columns=self.Columns[1],
                                                values_column=self.Business.name)

    def is_business_registered(self):
        usr = self.get_business_id()
        print(usr)
        if len(usr) == 0:
            return False
        else:
            return True

    def get_business_list(self):
        return self.DbSer.get_all_value_in_column(name_column=self.Columns[1], name_table=self.Table)

    def insert(self):
        id_business = self.get_business_id()
        if self.is_business_registered:
            try:
                self.DbSer.insert(self.Table, list_record=[(self.Business.name, self.Business.descr)])
            except Exception as ex:
                print(f"Errore durante l'inserimento {ex}")
        else:
            return print(f"User is registered with {id_business[0]}")


class Jobs_Service:
    def __init__(self,DBService: DbService,id_user: int=None, business_id: int=None, Jobs: Jobs = None):
        self.Jobs = Jobs
        self.DbSer = DBService
        self.id_user = id_user
        self.Business_id = business_id
        self.Table = "jobs"  # -- Table Name
        self.Columns = DBService.name_columns(name_table=self.Table)  # -- Table Column Names

    def get_jobs_id(self):
        return self.DbSer.get_select_with_where(select_columns=self.Columns[0],
                                                name_table=self.Table,
                                                where_columns=self.Columns[7],
                                                values_column=self.Jobs.name)

    def get_job_list(self):
        return self.DbSer.get_select_with_where(select_columns=self.Columns[7],
                                                name_table=self.Table,
                                                where_columns=self.Columns[1],
                                                values_column=self.Business_id)

    def is_jobs_registered(self):
        job_id = self.get_jobs_id()
        if len(job_id) == 0:
            return False
        else:
            return True

    def insert(self):
        self.DbSer.insert(self.Table, list_record=[(self.Business_id,
                                                    self.Jobs.start_date,
                                                    self.Jobs.end_date,
                                                    self.Jobs.h_pay,
                                                    self.Jobs.descr,
                                                    self.id_user,
                                                    self.Jobs.name)])


class Works_Service:
    def __init__(self, id_user: int, id_business: int, jobs_id: int, DBService: DbService, work: Work = None):
        self.work = work
        self.DbSer = DBService
        self.id_user = id_user
        self.id_business = id_business
        self.jobs_id = jobs_id
        self.Table = "works"  # -- Table Name
        self.Columns = DBService.name_columns(name_table=self.Table)  # -- Table Column Names

    def insert(self):
        self.DbSer.insert(self.Table, list_record=[(self.work.descr,
                                                    self.id_user,
                                                    self.work.data,
                                                    self.work.H_start,
                                                    self.work.H_end,
                                                    self.jobs_id)])

