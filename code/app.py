import pickle
import streamlit as st
import pandas as pd
import numpy as np
import gzip, pickle, pickletools
import random 
import time

# BASIC START UP STUFF 
if "player_answer" not in st.session_state:
    st.session_state.answer = "not done"

casi_width = 170

# Import dataset and model 
df_backend = pd.read_csv('../data/app_backend.csv')
df_frontend = pd.read_csv('../data/app_frontend.csv')
filepath = '../models/casi_dt_v2.pkl'
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()

    
# DEFINING FUNCTIONS
def next_question():
    st.session_state.answer = "not done"
    # Select a random row, calculate the prediction
    random_index = random.randint(0, len(df_backend) - 1)
    random_row_b = df_backend.loc[random_index]
    random_row_f = df_frontend.loc[random_index]
    X_with_price = random_row_b.to_frame().transpose()
    X = X_with_price.drop(['log_price'], axis = 1)
    real_price = real_price = round(float(np.exp(X_with_price['log_price'].values[0])), 2)
    casi_answer =  float(round(np.exp(model.predict(X)[0]),2))
    # Update session_state
    st.session_state.casi_answer = casi_answer
    st.session_state.real_price = real_price
    st.session_state.random_row_f = random_row_f#.to_dict()
    return real_price, casi_answer, random_row_b, random_row_f


def answer_function():
    player_answer = float(st.session_state.player_answer) #if 'player_answer' in st.session_state and st.session_state.player_answer else 0.0
    casi_answer = st.session_state.casi_answer
    real_price = st.session_state.real_price
    if abs(player_answer - real_price) < abs(casi_answer - real_price):
        st.session_state.answer = "answer correct"
    else:
        st.session_state.answer = "answer incorrect"
    return player_answer, casi_answer, real_price


# INITIAL (NEXT QUESTION)
if st.session_state.answer == "not done":
    real_price, casi_answer, random_row_b, random_row_f = next_question()

    # DESIGN STUFF
    st.title("Can you beat Casi our in-house sommelier?")
    st.markdown("**Guess the price of this wine**")
    st.table(random_row_f.to_frame().transpose().drop(columns = ['Log Price', 'Price (£)', 'name', 'ABV', 'Age']))

    col1, col2, col3 = st.columns([1,1,1]) 

    with col1:
        st.markdown(f"{random_row_f[0]}")
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
        st.header('Answer here:')
        player_answer = st.text_input("£", max_chars=7, key='player_answer', on_change=answer_function)
        #final_answer = st.button('Final Answer', on_click=answer_function)

        # if st.button('Final Answer'):
        #     try:
        #         player_answer = float(st.session_state.player_answer)
        #         answer_function()
        #     except ValueError:
        #         st.error("Please enter a valid number for the price.")
        #         st.header('Play with your own wine?')
        st.markdown(f"Upload or snap a photo of your bottle and see what casi thinks.")
        # uploaded_photo = col3.file_uploader("Upload a photo.")
        # camera_photo = col3.camera_input("Take a photo!")

    # player_answer_slider = st.select_slider("How would you price this wine?", options = [f'£{10}', f'£{20}', f'£{30}'])


# REVIEW ANSWER 
if st.session_state["answer"] in ["answer correct", "answer incorrect"]:
    st.title("Can you beat Casi our in-house sommelier?")
    random_row_f = pd.Series(st.session_state['random_row_f'])
    player_answer, casi_answer, real_price = answer_function()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"# Price: £{real_price}")
        # Add more details as needed

    with col2:
        image_path = '../images/casi_sad.png' if st.session_state["answer"] == "answer correct" else '../images/casi_happy.png'
        st.image(image_path, width=casi_width)

    with col3:
        header_text = 'Nice work!' if st.session_state["answer"] == "answer correct" else 'Better luck next time!'
        st.header(header_text)
        st.markdown(f"The real price was £{real_price}.")
        st.markdown(f"Casi guessed £{casi_answer}.")
        st.markdown(f"You guessed £{player_answer}.")
        # col3.metric(label="How close were you?", value=f"£{(casi_answer- real_price)}", delta=f"£{(player_answer-real_price)}")
        st.button('Play again', on_click=next_question)

st.write(st.session_state)
