import streamlit as st
from datetime import datetime,date,time
import calendar
import pytz

std_name = ('Eren', 'Historia', 'Mikasa')
now = datetime.now()

st.title("Attendance Register",)
name = st.selectbox('Student',std_name)

# Date input
date_val = st.date_input("Date",date.today())

# Duration Input
duration_val = st.slider("Duration (Min)",value=45)

# Time Input
time_val = st.time_input('Class time', time(int(now.hour),int(now.minute)-(int(now.minute)%10)),step=1800)
am_pm = st.radio('[Placeholder]AM-PM',options=('AM', 'PM'),label_visibility="hidden")


# Attendance Input
present_val = st.radio(f"Was {name} Present or Absent",('Present', 'Absent'))

# If Student is absent then duraiton is 0
if(present_val == "Absent"):
    duration_val = 0

# Submit Button
submitted = st.button("Submit")

if submitted:
    st.markdown(f":blue[Student]:&emsp;&emsp;{name}")
    st.markdown(f":blue[Date]:&emsp;&emsp;&emsp;&ensp;{date_val.strftime('%m/%d/%Y')}&nbsp;({calendar.day_name[date_val.weekday()]})")
    st.markdown(f":blue[Time]:&emsp;&emsp;&emsp;&ensp;{time_val}")
    st.markdown(f":blue[Duration]:&emsp;&emsp;{duration_val} Min")
    st.markdown(f":blue[Attandance]:&emsp;{present_val}")


st.title("Check Records")




# &nbsp;  1 space.
# &ensp;  2 spaces.
# &emsp;  4 spaces.