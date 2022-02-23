
import streamlit as st
from datetime import datetime

data = datetime.today().date()
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        slider_hours_range = st.slider("Ore",min_value = 0,
                                       max_value = 24,
                                       value=7,
                                       step=1)
    with c2:
        slider_minute_range= st.slider("Minuti",min_value =0,
                                       max_value=60,
                                       value=0,
                                       step=1)


dt = datetime(year=data.year,
month = data.month,
day = data.day,
hour = slider_hours_range, minute = slider_minute_range)

print(dt)