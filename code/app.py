"""
Backend:
0 - 'Name', 
1 - 'Region', 
2 - 'Country', 
3 - 'Vintage', 
4 - 'Producer', 
5 - 'Wine Variety',
6 - 'Grape Variety', 
7 - 'Rating', 
8 - 'rating_qty', 
9 - 'ABV', 
10 - 'from_vivino', 
11 - 'Age',
12 - 'log_price'

Frontend: 
0 - 'Name', 
1 - 'Region', 
2 - 'Country', 
3 - 'Vintage', 
4 - 'Producer', 
5 - 'Wine Variety',
6 - 'Grape Variety', 
7 - 'Price (£)', 
8 - 'Average Rating', 
9 - 'ABV', 
"""

import pickle
import streamlit as st
import pandas as pd
import numpy as np
import gzip, pickle, pickletools
import random 
import time

# BASIC START UP STUFF 
if "answer" not in st.session_state:
    st.session["answer"] = "not done"

# Import dataset and model 
df_backend = pd.read_csv('../data/app_backend.csv')
df_frontend = pd.read_csv('../data/app_frontend.csv')
filepath = '../models/casi_dt_v1.pkl'
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()

# Select a random row, calculate the prediction
random_index = random.randint(0, len(df_backend) - 1)
random_row_b = df_backend.loc[random_index]
random_row_f = df_frontend.loc[random_index]
X_with_price = random_row_b.to_frame().transpose()
X = X_with_price.drop(['log_price'], axis = 1)
real_price = round(np.exp(X_with_price['log_price']), 2)
casi_answer =  model.predict(X)

# DESIGN STUFF
casi_width = 150
st.title("Can you beat Casi our in-house sommelier?")
# Left column for data before the image
col1, col2, col3 = st.columns([1,1,1])  # Adjust column width ratios as needed


# DEFINING FUNCTIONS
def answer_function(casi_answer, real_price, player_answer):
    if round(casi_answer,2) - real_price < player_answer - real_price:
        st.session_state["answer"] = "answer correct"
    else: 
        st.session_state["answer"] = "answer incorrect"

# BEFORE QUESTION IS ANSWERED

with col1:
    st.markdown(f"Name: {random_row_f[0]}")
    st.markdown(f"Country: {random_row_f[2]}")
    st.markdown(f"Region: {random_row_f[1]}")
    st.markdown(f"Vintage: {random_row_f[3]}")
    st.markdown(f"Variety: {random_row_f[5]}")
    st.markdown(f"Grape: {random_row_f[5]}")
    st.markdown(f"ABV: {random_row_f[9]}")
    st.markdown(f"Producer: {random_row_f[4]}")
    

with col2:
    st.image('../images/casi_medium.png', width=casi_width)

with col3:
    st.header('Play with your own wine?')
    st.markdown(f"Upload or snap a photo of your bottle and see what casi thinks.")
    #uploaded_photo = col3.file_uploarder("Upload a photo.")
    #camera_photo = col3.camera_input("Take a photo!")


player_answer = st.text_input("How would you price this wine?", max_chars = 20)

st.button('Final Answer', on_click=answer_function(X, real_price, player_answer))

# player_answer_slider = st.select_slider("How would you price this wine?", options = [f'£{10}', f'£{20}', f'£{30}'])

# WHEN QUESTION ANSWERED CORRECTLY
if st.sesstion_state == "answer correct":
    with col1:
        st.markdown(f"# Price: £{real_price}")
        st.markdown(f"Name: {random_row_f[0]}")
        st.markdown(f"Country: {random_row_f[2]}")
        st.markdown(f"Region: {random_row_f[1]}")
        st.markdown(f"Vintage: {random_row_f[3]}")
        st.markdown(f"Variety: {random_row_f[5]}")
        st.markdown(f"Grape: {random_row_f[5]}")
        st.markdown(f"ABV: {random_row_f[9]}")
        st.markdown(f"Producer: {random_row_f[4]}")
        st.markdown(f"Rating: {random_row_f[8]}")

    with col2:
        st.image('../images/casi_sad.png', width=casi_width)

    with col3:
        st.header('Nice work!') # API: make these messages gpt generated 
        st.markdown(f"The real price was £{real_price}.")
        st.markdown(f"Casi guessed £{casi_answer}.")
        st.markdown(f"You guessed £{player_answer}.")
        col3.metric(label="How much did you win by?", value=(real_price-player_answer), delta=(real_price - casi_answer))
        # API: info about the wine in question and a photo

# WHEN QUESTION ANSWERED INCORRECTLY
if st.sesstion_state == "answer incorrect":
    with col1:
        st.markdown(f"# Price: £{real_price}") # API: make these messages gpt generated 
        st.markdown(f"Name: {random_row_f[0]}")
        st.markdown(f"Country: {random_row_f[2]}")
        st.markdown(f"Region: {random_row_f[1]}")
        st.markdown(f"Vintage: {random_row_f[3]}")
        st.markdown(f"Variety: {random_row_f[5]}")
        st.markdown(f"Grape: {random_row_f[5]}")
        st.markdown(f"ABV: {random_row_f[9]}")
        st.markdown(f"Producer: {random_row_f[4]}")
        st.markdown(f"Rating: {random_row_f[8]}")

    with col2:
        st.image('../images/casi_happy.png', width=casi_width)

    with col3:
        st.header('Better luck next time!')
        st.markdown(f"The real price was £{real_price}.")
        st.markdown(f"Casi guessed £{casi_answer}.")
        st.markdown(f"You guessed £{player_answer}.")
        col3.metric(label="How close were you?", value=(real_price - casi_answer), delta=(real_price-player_answer))
        # API: info about the wine in question and a photo
    



# SANDBOX
# Tools to use

# uploaded_photo = col3.file_uploarder("Upload a photo.")
# camera_photo = col3.camera_input("Take a photo!")
# col3.success("Photo uploaded sucessfully!")
# col3.progress(0)
for perc_complete in range(100):
    time.sleep(0.5)
    progress_bar.progress(perc_complyee+1)

# Use this to show how close someones score was: 

