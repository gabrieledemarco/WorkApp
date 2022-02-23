import streamlit as st
from datetime import datetime, date
import random


def Insert_time_Slider(data: date = datetime.today().date(), title=""):
    # data = datetime.today().date()
    key_r = random.randrange(100, 10, -2)
    with st.container():
        st.text(title)
        c1, c2 = st.columns(2)
        with c1:
            slider_hours_range = st.slider(key=f"{key_r}", label="Ore",
                                           min_value=0,
                                           max_value=24,
                                           value=7,
                                           step=1)
        with c2:
            slider_minute_range = st.slider(key=f"{key_r}s", label="Minuti",
                                            min_value=0,
                                            max_value=60,
                                            value=0,
                                            step=1)

    return datetime(year=data.year,
                    month=data.month,
                    day=data.day,
                    hour=slider_hours_range, minute=slider_minute_range)
