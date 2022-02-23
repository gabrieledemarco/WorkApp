from datetime import date, datetime


class User:
    role = "Worker"

    def __init__(self,
                 nickname: str,
                 password: str):
        self.Nickname = nickname
        self.Password = password

    def __str__(self):
        return f" Nickname: {self.Nickname}, Password {self.Password}"


class Business:
    def __init__(self,
                 name: str,
                 descr: str = ""):
        self.name = name
        self.descr = descr


class Jobs:
    def __init__(self,
                 User: User,
                 job_name: str,
                 Business: Business = None,
                 start_date: date = None,
                 end_date: date = None,
                 h_payment: float = None,
                 descr: str = ""):
        self.User = User
        self.Business = Business
        self.name = job_name
        self.start_date = start_date
        self.end_date = end_date
        self.Business = Business
        self.h_pay = h_payment
        self.descr = descr


class Work:
    def __init__(self,
                 data: date,
                 H_start: datetime,
                 H_end: datetime,
                 desc: str = ""):
        self.data = data
        self.H_start = H_start
        self.H_end = H_end
        self.descr = desc
