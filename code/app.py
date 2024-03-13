import pickle
import streamlit as st
import pandas as pd
import numpy as np
import gzip, pickle, pickletools
import random 
import time
import visualisations as vis
import shap
import matplotlib.pyplot as plt

# BASIC START UP STUFF 
if "player_answer" not in st.session_state:
    st.session_state.answer = "not done"

if "player_answer" not in st.session_state:
    st.session_state.shap = "not done"

casi_width = 170

# Import dataset and model 
df = pd.read_csv('../data/clean_combined_wines.csv')
df_backend = pd.read_csv('../data/app_backend.csv')
df_frontend = pd.read_csv('../data/app_frontend.csv')
filepath = '../models/casi_dt_production.pkl'
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()

# filepath_no_rating = '../models/casi_dt_no_rating.pkl'
# with gzip.open(filepath, 'rb') as f:
#     p_norating = pickle.Unpickler(f)
#     model_no_rating = p_norating.load()

# def switch_models():
#     st.session_state


# DEFINING FUNCTIONS

def next_question():
    st.session_state.answer = "not done"
    # Select a random row, calculate the prediction
    random_index = random.randint(0, len(df_backend) - 1)
    random_row_b = df_backend.loc[random_index]
    random_row_f = df_frontend.loc[random_index]
    X_with_price = random_row_b.to_frame().transpose()
    X = X_with_price.drop(['log_price'], axis = 1)
    real_price = round(float(np.exp(X_with_price['log_price'].values[0])), 2)
    casi_answer =  float(round(np.exp(model.predict(X)[0]),2))
    # Update session_state
    st.session_state.casi_answer = casi_answer
    st.session_state.real_price = real_price
    st.session_state.random_row_f = random_row_f#.to_dict()
    st.session_state.random_row_b = random_row_b#.to_dict()
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
    st.table(random_row_f.to_frame().transpose().drop(columns = ['Log Price', 'Price ($)', 'name', 'ABV', 'Age']))

    col1, col2, col3 = st.columns([1,1,1])  

    with col1:
        st.markdown(f"Name:  \n **{random_row_f[0]}**")

        wine_width = 88
        if random_row_f[5] == 'Red':
            st.image('../images/red.png', width=wine_width, )
        elif random_row_f[5] == 'White':
            st.image('../images/white.png', width=wine_width)
        elif random_row_f[5] == 'Rose':
            st.image('../images/rose.png', width=wine_width)
        elif random_row_f[5] == 'Sparkling':
            st.image('../images/sparkling.png', width=wine_width)


    with col2:
        st.image('../images/casi_medium.png', width=casi_width)

    with col3:
        st.header('Answer here:')
        player_answer = st.text_input(label = "USD", max_chars=7, key='player_answer', on_change=answer_function)
        
        # no_rating = st.button('Go easy on me', on_click=switch_models)

        # st.markdown(f"Upload or snap a photo of your bottle and see what casi thinks.")
        # uploaded_photo = col3.file_uploader("Upload a photo.")
        # camera_photo = col3.camera_input("Take a photo!")

    # player_answer_slider = st.select_slider("How would you price this wine?", options = [f'${10}', f'${20}', f'${30}'])


# REVIEW ANSWER 
if st.session_state["answer"] in ["answer correct", "answer incorrect"]:
    st.title("Can you beat Casi our in-house sommelier?")
    random_row_f = pd.Series(st.session_state['random_row_f'])
    random_row_b = pd.Series(st.session_state['random_row_b'])
    player_answer, casi_answer, real_price = answer_function()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"## Price: ${real_price}")
        st.markdown(f"## Rating: {random_row_f[8]}/5")
        # Add more details as needed
        f"How does it compare to vintage averages in {random_row_f[2]}?"
        st.dataframe(vis.compare_close_vintages_in_a_country(df, random_row_f[2], random_row_f[3]), hide_index=True)

    with col2:
        image_path = '../images/casi_sad.png' if st.session_state["answer"] == "answer correct" else '../images/casi_happy.png'
        st.image(image_path, width=casi_width)

    with col3:
        header_text = 'Nice work you beat Casi!' if st.session_state["answer"] == "answer correct" else 'Casi wins!'
        st.header(header_text)
        st.markdown(f"The real price was ${real_price}.")
        st.markdown(f"Casi guessed ${casi_answer}.")
        st.markdown(f"**You guessed ${player_answer}.**")
        X_with_price = random_row_b.to_frame().transpose()
        X = X_with_price.drop(columns = ['log_price'])
        global_importances = pd.Series(model.feature_importances_, index=X.columns)
        
        st.bar_chart(global_importances, )
        # global_importances.sort_values(ascending=True, inplace=True)

        # global_importances.plot.barh(color='mediumpurple')
        # plt.xlabel("Importance")
        # plt.ylabel("Feature")
        # plt.title("Global Feature Importance");

        # col3.metric(label="How close were you?", value=f"${(casi_answer- real_price)}", delta=f"${(player_answer-real_price)}")
        st.button('Play again', on_click=next_question)

#st.write(st.session_state)


# """
#         st.markdown(f"{random_row_f[0]}")
#         st.markdown(f"Country: {random_row_f[2]}")
#         st.markdown(f"Region: {random_row_f[1]}")
#         st.markdown(f"Vintage: {random_row_f[3]}")
#         st.markdown(f"Variety: {random_row_f[5]}")
#         st.markdown(f"Grape: {random_row_f[5]}")
#         st.markdown(f"ABV: {random_row_f[9]}")
#         st.markdown(f"Producer: {random_row_f[4]}")
# """