
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
import joblib
import gzip, pickle, pickletools
import random 

# Import a random row from the test_dataset 
df_backend = pd.read_csv('../data/app_backend.csv')
df_frontend = pd.read_csv('../data/app_frontend.csv')

filepath = '../models/casi_dt_v1.pkl'

with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()

st.title("Can you beat Casi our in-house sommelier?")

# Select a random row, calculate the prediction
random_index = random.randint(0, len(df_backend) - 1)
random_row_b = df_backend.loc[random_index]
random_row_f = df_frontend.loc[random_index]
X_with_price = random_row_b.to_frame().transpose()
X = X_with_price.drop(['log_price'], axis = 1)
real_price = round(np.exp(X_with_price['log_price']), 2)
casi_answer =  model.predict(X)

# Left column for data before the image
col1, col2, col3 = st.columns([1,1,1])  # Adjust column width ratios as needed

def answer_function(casi_answer, real_price, player_answer):
    if round(casi_answer,2) - real_price < player_answer - real_price:
        return 1
    else: 
        return 0
    
    # correct_answer = 0 

with col1:
    st.write(f"Name: {random_row_f[0]}")
    st.write(f"Country: {random_row_f[2]}")
    st.write(f"Region: {random_row_f[1]}")
    st.write(f"ABV: {random_row_f[9]}")
    st.write(f"Producer: {random_row_f[4]}")
    st.write(f"Rating: {random_row_f[8]}")

with col2:
    st.image('../images/casi_medium.png', width=150)

with col3:
    st.header('Casi is thinking...')
    if answer_function == 1: 
        f"THINK AGAIN! Casi guessed {casi_answer}, but the real price was {real_price}."
    else: 
        f"Nice work! Casi guessed {casi_answer}, but the real price was {real_price}."

player_answer = st.text_input("How would you price this wine?", max_chars = 20)


# player_answer_slider = st.select_slider("How would you price this wine?", options = [f'£{10}', f'£{20}', f'£{30}'])

st.button('Final Answer', on_click=answer_function(X, real_price, player_answer))
