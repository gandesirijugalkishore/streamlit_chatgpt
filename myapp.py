import streamlit as st
import openai
from PIL import Image

image = Image.open('Myproject.png')

st.image(image, caption='JUGAL KISHORE')

# api_key_form = st.form("API Key")
# api_key = api_key_form.text_input("API Key", value="")

# def generate_response(prompt, api_key):
#     openai.api_key = api_key
#     response = openai.Completion.create(engine="chatbot", prompt=prompt)
#     return response.choices[0].text

# prompt_form = st.form("Prompt")
# prompt = prompt_form.text_input("Prompt", value="")
# # send_button = st.button("Send")
# st.form_submit_button()


# if prompt_form.submit():
#     response = generate_response(prompt, api_key)
#     st.write(response)


openai.api_key = "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"

st.title("GPT-3 Chatbot App")

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

message = st.text_input("Enter your message:")
send_button = st.button("Send")

if send_button:
    response = generate_response(message)
    st.write("You said:", message)
    st.write("Chatbot says:", response)



# # Core Pkgs
# import streamlit as st
# import pandas as pd
# from PIL import Image
# import seaborn as sns



# st.title("Streamlit Forms & Salary Calculator")
# menu = ["Home","About","Data Analysis"]
# choice = st.sidebar.selectbox("Menu",menu)

# if choice == "Home":
#     st.subheader("Forms Tutorial")

#     # Salary Calculator
#     # Combine forms + columns
#     with st.form(key='salaryform'):
#         col1,col2,col3,col4 = st.columns([4,3,2,1])

#         with col1:
#             amount = st.number_input("Hourly Rate in $")

#         with col2:
#             hour_per_week = st.number_input("Hours Per Week",1,120)

#         with col3:
#             st.text("Salary")
#             submit_salary = st.form_submit_button(label='Calculate') 
                                        
#         with col4:
#             st.text("test")


#     if submit_salary:
#         # with st.expander("Results"):
#         daily = amount * 8
#         # monthly = [amount * hour_per_week]
#         weekly = amount * hour_per_week
#         test = (amount * hour_per_week )* 4
        
#         data = {'hourly':amount,'daily':daily,'weekly':weekly,'monthly':test}
#         df = pd.DataFrame(data,index=[0])
#         # df = pd.DataFrame(,index=[0])
#         st.dataframe(df)

# elif choice == "About":
        
        # image = Image.open('Myproject.png')

        # st.image(image, caption='JUGAL KISHORE')
#         st.write("check out this [link](https://sites.google.com/view/jugalgandhesiri/home)")

# elif choice == "Data Analysis":
#         df = pd.read_csv("Salary_Data.csv")
#         st.dataframe(df)
#         st.line_chart(df)
    



# 		# # Method 1: Context Manager Approach (with)
# 		# with st.form(key='form1'):
# 		# 	firstname = st.text_input("Firstname")
# 		# 	lastname = st.text_input("lastname")
# 		# 	dob = st.date_input("Date of Birth")

# 		# 	# Important
# 		# 	submit_button = st.form_submit_button(label='SignUp')

# 		# # Results Can be either form or outside
# 		# if submit_button:
# 		# 	st.success("Hello {} you ve created an account".format(firstname))

# 		# # Method 2:
# 		# form2 = st.form(key='form2')
# 		# username = form2.text_input("Username")
# 		# jobtype = form2.selectbox("Job",["Dev","Data Scientist","Doctor"])
# 		# submit_button2 = form2.form_submit_button("Login")

# 		# if submit_button2:
# 		# 	st.write(username.upper())










