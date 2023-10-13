import streamlit as st
from datetime import datetime,date,time
import calendar
import pandas as pd
import time

file_record = "AttendanceRecord.xlsx"

def updateExcel(name_val,date_val,duration_val,time_val,am_pm_val,present_val,comments):
    # time_val = time_val.strftime("%H:%M")
    timestr = time_val + f" {am_pm_val}"
    date_str = date_val.strftime('%d/%m/%Y')
    print("========================")
    print(timestr)

    new_data = {
        'Year': [int(date_str[-4:])],
        'Date': [int(date_str[:2])],
        'Month':[calendar.month_name[date_val.month]],
        'Day': [calendar.day_name[date_val.weekday()]],
        'Duration (Min)': [int(duration_val)],
        'Time': [timestr],
        'Attendance': [present_val],
        'Comments':[comments],
    }
    df = pd.DataFrame(data = new_data)
    # st.write(new_data)
    with pd.ExcelWriter(file_record,mode='a',engine='openpyxl',if_sheet_exists='overlay') as writer:
        try:
            df.to_excel(writer, sheet_name = name_val, startrow=writer.sheets[name_val].max_row,index = False,header=False)
        except KeyError as k:
            print("New sheet creater for new student")
            df.to_excel(writer, sheet_name = name_val,index=False)



with open('names.txt') as f:
    global std_name_l
    std_name_l = f.readlines()
    for i,n in enumerate(std_name_l):
        std_name_l[i] = n[:-1]
    std_name_l.sort()
    std_name_l = tuple(std_name_l)
    f.close()

now = datetime.now()

tab1, tab2, tab3 = st.tabs(["Student Attendance Recording", "Attendance Record Display", "New Student Entry"])
with tab1:
    st.title("Attendance Register")
    name_val = st.selectbox('Student',std_name_l)

    # Date input
    date_val = st.date_input("Date",date.today())
    # Duration Input
    duration_val = st.slider("Duration (Min)",value=45,step=5)

    # Time Input
    # time_val = st.time_input('Class time', time(int(now.hour),int(now.minute)-(int(now.minute)%10)),step=1800)
    time_options = []
    for i in range(1,13):
        for j in range(0,55,15):
            temp = ""
            if i / 10 == 0:
                temp += f"0{i}"
            else:
                temp += str(i)
            temp += ":"
            if j / 10 == 0:
                temp += f"0{j}"
            else:
                temp += str(j)
            
            time_options.append(temp)
    # print("----------------------------")
    # print(time_options)

    time_val = st.selectbox('Class Start Time',tuple(time_options))
    am_pm_val = st.radio('[Placeholder]AM-PM',options=('AM', 'PM'),label_visibility="hidden")


    # Attendance Input
    present_val = st.radio(f"Was {name_val} Present or Absent",('Present', 'Absent'))

    # Additional Comments
    comments = st.text_input('Comments')

    # If Student is absent then duraiton is 0
    if(present_val == "Absent"):
        duration_val = 0

    # Submit Button
    submitted = st.button("Submit",on_click=updateExcel,args=(name_val,date_val,duration_val,time_val,am_pm_val,present_val,comments))

    if submitted:
        st.markdown(f":blue[Student]:&emsp;&emsp;{name_val}")
        st.markdown(f":blue[Date]:&emsp;&emsp;&emsp;&ensp;{date_val.strftime('%m/%d/%Y')}&nbsp;({calendar.day_name[date_val.weekday()]})")
        st.markdown(f":blue[Time]:&emsp;&emsp;&emsp;&ensp;{time_val}&nbsp;{am_pm_val}")
        st.markdown(f":blue[Duration]:&emsp;&emsp;{duration_val} Min")
        st.markdown(f":blue[Attandance]:&emsp;{present_val}")


with tab2:
    st.title("Check Records")
    rec_check_name = st.selectbox('Student',std_name_l,key="Sb_record_check_name")
    check_rec_button = st.button("Show Records")

    if check_rec_button:
        try:
            df_disp = pd.read_excel(file_record,sheet_name=rec_check_name)
            st.dataframe(df_disp, use_container_width=True)
        except ValueError as e:
            st.write(f"No Records Found for {rec_check_name}")

with tab3:
    st.title("New Student Entry")
    new_std = st.text_input('Enter New Student Name')
    new_std_button = st.button("Add")

    if new_std_button:
        with open("names.txt",'a') as f:
            # std_name_l_l = f.readlines()
            # std_name_l_l = [x[:-1] for x in std_name_l]
            if new_std not in std_name_l:
                f.write(new_std+"\n")
            f.close()
        st.write("Successfully created new student entry!")
        st.write("Please wait...")
        time.sleep(2)
        st.experimental_rerun()

    
# &nbsp;  1 space.
# &ensp;  2 spaces.
# &emsp;  4 spaces.
