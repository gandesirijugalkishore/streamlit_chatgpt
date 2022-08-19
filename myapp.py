# Core Pkgs
import streamlit as st
import pandas as pd
from PIL import Image


st.title("Streamlit Forms & Salary Calculator")
menu = ["Home","About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.subheader("Forms Tutorial")

    # Salary Calculator
    # Combine forms + columns
    with st.form(key='salaryform'):
        col1,col2,col3,col4 = st.columns([4,3,2,1])

        with col1:
            amount = st.number_input("Hourly Rate in $")

        with col2:
            hour_per_week = st.number_input("Hours Per Week",1,120)

        with col3:
            st.text("Salary")
            submit_salary = st.form_submit_button(label='Calculate') 
                                        
        with col4:
            st.text("test")


    if submit_salary:
        # with st.expander("Results"):
        daily = amount * 8
        # monthly = [amount * hour_per_week]
        weekly = amount * hour_per_week
        test = (amount * hour_per_week )* 4
        
        data = {'hourly':amount,'daily':daily,'weekly':weekly,'monthly':test}
        df = pd.DataFrame(data,index=[0])
        # df = pd.DataFrame(,index=[0])
        st.dataframe(df)

elif choice == "About":
        
        image = Image.open('Myproject.png')

        st.image(image, caption='JUGAL KISHORE')
        st.write("check out this [link](https://sites.google.com/view/jugalgandhesiri/home)")




		# # Method 1: Context Manager Approach (with)
		# with st.form(key='form1'):
		# 	firstname = st.text_input("Firstname")
		# 	lastname = st.text_input("lastname")
		# 	dob = st.date_input("Date of Birth")

		# 	# Important
		# 	submit_button = st.form_submit_button(label='SignUp')

		# # Results Can be either form or outside
		# if submit_button:
		# 	st.success("Hello {} you ve created an account".format(firstname))

		# # Method 2:
		# form2 = st.form(key='form2')
		# username = form2.text_input("Username")
		# jobtype = form2.selectbox("Job",["Dev","Data Scientist","Doctor"])
		# submit_button2 = form2.form_submit_button("Login")

		# if submit_button2:
		# 	st.write(username.upper())










