import streamlit as st
import pandas as pd

def calculate_average_price(average_price, market_value, investment):
    return (average_price * investment + market_value * investment) / (investment + investment)

st.title("Cryptocurrency Average Price Calculator")

# Load a pre-existing dataset with market values for 3 cryptocurrencies
market_values = pd.DataFrame({
    "Cryptocurrency": ["Bitcoin", "Ethereum", "Dogecoin"],
    "Market Value (USD)": [64000, 2500, 0.05]
})

selected_crypto = st.selectbox("Select the cryptocurrency:", market_values["Cryptocurrency"])
market_value = market_values[market_values["Cryptocurrency"] == selected_crypto]["Market Value (USD)"].iloc[0]
average_price = st.number_input("Enter your average price of the cryptocurrency (in USD):", min_value=0.0)
investment = st.number_input("Enter the amount you want to invest (in USD):", min_value=0.0)

if st.button("Calculate Average Price"):
    result = calculate_average_price(average_price, market_value, investment)
    st.success(f"The average price of your {selected_crypto} investment is: ${result:.2f}")

    





# import streamlit as st
# import requests
# from bs4 import BeautifulSoup

# st.title("YouTube Comment Scraper")

# # Function to scrape comments from a YouTube video
# def scrape_comments(video_id):
#     # Construct the YouTube comments API URL
#     url = f"https://www.youtube.com/watch?v={video_id}"
#     # Send a GET request to the API URL
#     page = requests.get(url)
#     # Parse the page content with BeautifulSoup
#     soup = BeautifulSoup(page.content, "html.parser")
#     # Find all the comment elements on the page
#     comments = soup.find_all("div", class_="comment-text-content")
#     return comments

# # Function to perform sentiment analysis on the comments
# def sentiment_analysis(comments):
#     good_count = 0
#     bad_count = 0
#     # Loop through the comments and perform sentiment analysis
#     for comment in comments:
#         if "good" in comment.text or "great" in comment.text:
#             good_count += 1
#         elif "bad" in comment.text or "worst" in comment.text:
#             bad_count += 1
#     return good_count, bad_count

# # Get the YouTube video ID from the user
# video_id = st.text_input("Enter a YouTube video ID:")

# # Scrape the comments from the video
# comments = scrape_comments(video_id)

# # Perform sentiment analysis on the comments
# if comments:
#     good_count, bad_count = sentiment_analysis(comments)
#     st.write("Good reviews:", good_count)
#     st.write("Bad reviews:", bad_count)
# else:
#     st.write("No comments found.")


# # import streamlit as st
# # import openai
# # from PIL import Image

# # image = Image.open('Myproject.png')

# # st.image(image, caption='JUGAL KISHORE')

# # # api_key_form = st.form("API Key")
# # # api_key = api_key_form.text_input("API Key", value="")

# # # def generate_response(prompt, api_key):
# # #     openai.api_key = api_key
# # #     response = openai.Completion.create(engine="chatbot", prompt=prompt)
# # #     return response.choices[0].text

# # # prompt_form = st.form("Prompt")
# # # prompt = prompt_form.text_input("Prompt", value="")
# # # # send_button = st.button("Send")
# # # st.form_submit_button()


# # # if prompt_form.submit():
# # #     response = generate_response(prompt, api_key)
# # #     st.write(response)



# # st.title("GPT-3 Chatbot App")

# # def generate_response(prompt):
# #     completions = 
# #         engine="text-davinci-002",
# #         prompt=prompt,
# #         max_tokens=1024,
# #         n=1,
# #         temperature=0.5,
# #     )

# #     message = completions.choices[0].text
# #     return message

# # message = st.text_input("Enter your message:")
# # send_button = st.button("Send")

# # if send_button:
# #     response = generate_response(message)
# #     st.write("You said:", message)
# #     st.write("Chatbot says:", response)



# # # Core Pkgs
# # import streamlit as st
# # import pandas as pd
# # from PIL import Image
# # import seaborn as sns



# # st.title("Streamlit Forms & Salary Calculator")
# # menu = ["Home","About","Data Analysis"]
# # choice = st.sidebar.selectbox("Menu",menu)

# # if choice == "Home":
# #     st.subheader("Forms Tutorial")

# #     # Salary Calculator
# #     # Combine forms + columns
# #     with st.form(key='salaryform'):
# #         col1,col2,col3,col4 = st.columns([4,3,2,1])

# #         with col1:
# #             amount = st.number_input("Hourly Rate in $")

# #         with col2:
# #             hour_per_week = st.number_input("Hours Per Week",1,120)

# #         with col3:
# #             st.text("Salary")
# #             submit_salary = st.form_submit_button(label='Calculate') 
                                        
# #         with col4:
# #             st.text("test")


# #     if submit_salary:
# #         # with st.expander("Results"):
# #         daily = amount * 8
# #         # monthly = [amount * hour_per_week]
# #         weekly = amount * hour_per_week
# #         test = (amount * hour_per_week )* 4
        
# #         data = {'hourly':amount,'daily':daily,'weekly':weekly,'monthly':test}
# #         df = pd.DataFrame(data,index=[0])
# #         # df = pd.DataFrame(,index=[0])
# #         st.dataframe(df)

# # elif choice == "About":
        
#         # image = Image.open('Myproject.png')

#         # st.image(image, caption='JUGAL KISHORE')
# #         st.write("check out this [link](https://sites.google.com/view/jugalgandhesiri/home)")

# # elif choice == "Data Analysis":
# #         df = pd.read_csv("Salary_Data.csv")
# #         st.dataframe(df)
# #         st.line_chart(df)
    



# # 		# # Method 1: Context Manager Approach (with)
# # 		# with st.form(key='form1'):
# # 		# 	firstname = st.text_input("Firstname")
# # 		# 	lastname = st.text_input("lastname")
# # 		# 	dob = st.date_input("Date of Birth")

# # 		# 	# Important
# # 		# 	submit_button = st.form_submit_button(label='SignUp')

# # 		# # Results Can be either form or outside
# # 		# if submit_button:
# # 		# 	st.success("Hello {} you ve created an account".format(firstname))

# # 		# # Method 2:
# # 		# form2 = st.form(key='form2')
# # 		# username = form2.text_input("Username")
# # 		# jobtype = form2.selectbox("Job",["Dev","Data Scientist","Doctor"])
# # 		# submit_button2 = form2.form_submit_button("Login")

# # 		# if submit_button2:
# # 		# 	st.write(username.upper())










