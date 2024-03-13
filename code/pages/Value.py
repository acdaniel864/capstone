import streamlit as st
import pandas as pd
import numpy as np
import gzip, pickle, pickletools
import shap
import matplotlib.pyplot as plt
import json

st.set_page_config(page_title="Valuations", page_icon="📈")


# Load the model
filepath = '../models/casi_rf_production.pkl'
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model_rf = p.load()

# Preload category names and their mappings
# This part needs to be filled based on your dataset
    
# To load the mapping in a new session
with open('../mapping/label_mapping.json', 'r') as file:
    loaded_mapping = json.load(file)
category_mappings = loaded_mapping

def user_input_features():
    # Numerical inputs
    rating = st.slider('Rating', 0.0, 5.0, 2.5) 
    rating_qty = 150.0

    # Categorical inputs
    country = st.selectbox('Country', options=list(category_mappings['Country'].keys()))
    region = st.selectbox('Region', options=list(category_mappings['Region'].keys()))
    vintage = st.selectbox('Vintage', options=list(category_mappings['Vintage'].keys()))
    producer = st.selectbox('Producer', options=list(category_mappings['Producer'].keys()))
    wine_variety = 'red'
    grape_variety = st.selectbox('Grape Variety', options=list(category_mappings['Grape_variety'].keys()))
    
    # Compute other inputs
    log_rating_qty = np.log(rating_qty)
    rating_log_rating_qty = rating * log_rating_qty

    # Prepare the input data frame (ensure the order matches your model's expected input)
    features = {
        'region': category_mappings['Region'][region],
        'country':  category_mappings['Country'][country],
        'vintage': category_mappings['Vintage'][vintage],
        'producer': category_mappings['Producer'][producer],
        'wine_variety': category_mappings['Wine_variety'][wine_variety],
        'grape_variety': category_mappings['Grape_variety'][grape_variety],
        'rating': rating,
        'rating_qty': rating_qty,
        'log_rating_qty': log_rating_qty,
        'rating * log_rating_qty': rating_log_rating_qty
    }
    return pd.DataFrame([features])

col1, col2 = st.columns(2)
with col1:
    # Display the user input features
    user_inputs = user_input_features()

    explainer = shap.TreeExplainer(model_rf)
    shap_values = explainer.shap_values(user_inputs)

    # Plot SHAP values (example, adjust as necessary)
    plt.figure()
    shap.summary_plot(shap_values, user_inputs, plot_type="bar")
    st.pyplot(plt)

with col2:
    image_path = '../images/casi_medium.png'
    st.image(image_path, width=150)

        # Prediction
    prediction = model_rf.predict(user_inputs)

    # Display predicted price 
    predicted_price = np.exp(prediction) 
    st.markdown(f"### Hrmm I'd price that")
    st.markdown(f'## $ {predicted_price[0]:.2f}')



























# import pickle
# import streamlit as st
# import pandas as pd
# import numpy as np
# import gzip, pickle
# import random 
# import time
# import visualisations as vis
# import shap

# st.sidebar.title('Navigation')
# # options = st.sidebar.radio('Pages', options = ['Game', 'Wine Valuations'])

# # Import dataset and model 
# df = pd.read_csv('../data/clean_combined_wines.csv')
# df_backend = pd.read_csv('../data/app_backend.csv')
# df_frontend = pd.read_csv('../data/app_frontend.csv')
# filepath = '../models/casi_dt_production.pkl'
# casi_width = 170

# X = df_backend.drop(columns=['Log Price'])
# y = df_backend['Log Price']

# vintage_options = [i for i in sorted(df_frontend['Vintage'].unique())]
# producer_options = [i for i in sorted(df_frontend['Producer'].unique())]
# region_options = [i for i in sorted(df_frontend['Region'].unique())]
# ratinglist = [round(i,1) for i in np.arange(1, 5.1, 0.1)]

# st.write("# Would you like casi to value your wine?")

# st.sidebar.header('Specify input parameters')

# def user_input_features():
#     CRIM = st.sidebar.slider('CRIM', X.CRIM.min(), X.CRIM.max(), X.CRIM.mean())
#     ZN = st.sidebar.slider('ZN', X.ZN.min(), X.ZN.max(), X.ZN.mean())
#     INDUS = st.sidebar.slider('INDUS', X.INDUS.min(), X.INDUS.max(), X.INDUS.mean())
#     CHAS = st.sidebar.slider('CHAS', X.CHAS.min(), X.CHAS.max(), X.CHAS.mean())
#     NOX = st.sidebar.slider('NOX', X.NOX.min(), X.NOX.max(), X.NOX.mean())
#     RM = st.sidebar.slider('RM', X.RM.min(), X.RM.max(), X.RM.mean())
#     AGE = st.sidebar.slider('AGE', X.AGE.min(), X.AGE.max(), X.AGE.mean())
#     DIS = st.sidebar.slider('DIS', X.DIS.min(), X.DIS.max(), X.DIS.mean())
#     RAD = st.sidebar.slider('RAD', X.RAD.min(), X.RAD.max(), X.RAD.mean())
#     TAX = st.sidebar.slider('TAX', X.TAX.min(), X.TAX.max(), X.TAX.mean())
#     PTRATIO = st.sidebar.slider('PTRATIO', X.PTRATIO.min(), X.PTRATIO.max(), X.PTRATIO.mean())
#     B = st.sidebar.slider('B', X.B.min(), X.B.max(), X.B.mean())
#     LSTAT = st.sidebar.slider('LSTAT', X.LSTAT.min(), X.LSTAT.max(), X.LSTAT.mean())
#     data = {'CRIM': CRIM,
#             'ZN': ZN,
#             'INDUS': INDUS,
#             'CHAS': CHAS,
#             'NOX': NOX,
#             'RM': RM,
#             'AGE': AGE,
#             'DIS': DIS,
#             'RAD': RAD,
#             'TAX': TAX,
#             'PTRATIO': PTRATIO,
#             'B': B,
#             'LSTAT': LSTAT}
#     features = pd.DataFrame(data, index=[0])
#     return features

# # VALUATION SECTION 
# if 'wine_inputted' not in st.session_state:
#     st.session_state["answer"] = "before valuation"
    
# if st.session_state["answer"] == "before valuation":
#     st.title("What are the details of the wine you'd like valued?")

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.markdown(f"#Price: $")
#         # # Add more details as needed

#     with col2:
#         image_path = '../images/casi_medium.png'
#         st.image(image_path, width=casi_width)

#     with col3:
#         header_text = 'How can I help?'
#         st.selectbox('Vintage', vintage_options, key='vintage')
#         st.selectbox('Producer', producer_options, key='producer')
#         st.selectbox('Region', region_options, key='region')
#         rating_options = st.select_slider("How would you rate the wine?", options = ratinglist)

#         st.button('Value my wine', on_click=do_valuation)



# # def game():
# #         # BASIC START UP STUFF 
# #     if "player_answer" not in st.session_state:
# #         st.session_state.answer = "not done"

# #     with gzip.open(filepath, 'rb') as f:
# #         p = pickle.Unpickler(f)
# #         model = p.load()

# #     # filepath_no_rating = '../models/casi_dt_no_rating.pkl'
# #     # with gzip.open(filepath, 'rb') as f:
# #     #     p_norating = pickle.Unpickler(f)
# #     #     model_no_rating = p_norating.load()

# #     # def switch_models():
# #     #     st.session_state


# #     # DEFINING FUNCTIONS
# #     # def make_real_price(n):
# #     #     rounded = round(n * 4) / 4
# #     #     if rounded % 1 == 0:  # Checks if the decimal part is .00
# #     #         rounded -= 0.01  # Adjusts .00 to .99
# #     #     return rounded

# #     def valuation_input():
# #         st.session_state.answer = "before valuation"

# #     def do_valuation():
# #         st.session_state.answer = "do valuation"

# #     def next_question():
# #         st.session_state.answer = "not done"
# #         # Select a random row, calculate the prediction
# #         random_index = random.randint(0, len(df_backend) - 1)
# #         random_row_b = df_backend.loc[random_index]
# #         random_row_f = df_frontend.loc[random_index]
# #         X_with_price = random_row_b.to_frame().transpose()
# #         X = X_with_price.drop(['log_price'], axis = 1)
# #         real_price = round(float(np.exp(X_with_price['log_price'].values[0])), 2)
# #         casi_answer =  float(round(np.exp(model.predict(X)[0]),2))
# #         # Update session_state
# #         st.session_state.casi_answer = casi_answer
# #         st.session_state.real_price = real_price
# #         st.session_state.random_row_f = random_row_f#.to_dict()
# #         return real_price, casi_answer, random_row_b, random_row_f


# #     def answer_function():
# #         player_answer = float(st.session_state.player_answer) #if 'player_answer' in st.session_state and st.session_state.player_answer else 0.0
# #         casi_answer = st.session_state.casi_answer
# #         real_price = st.session_state.real_price
# #         if abs(player_answer - real_price) < abs(casi_answer - real_price):
# #             st.session_state.answer = "answer correct"
# #         else:
# #             st.session_state.answer = "answer incorrect"
# #         return player_answer, casi_answer, real_price

# #     # INITIAL (NEXT QUESTION)
# #     if st.session_state.answer == "not done":
# #         real_price, casi_answer, random_row_b, random_row_f = next_question()
# #         # DESIGN STUFF
# #         st.title("Can you beat Casi our in-house sommelier?")
# #         st.table(random_row_f.to_frame().transpose().drop(columns = ['Log Price', 'Price ($)', 'name', 'ABV', 'Age']))

# #         col1, col2, col3 = st.columns([1,1,1])  

# #         with col1:
# #             st.markdown(f"Name:  \n **{random_row_f[0]}**")

# #             wine_width = 88
# #             if random_row_f[5] == 'Red':
# #                 st.image('../images/red.png', width=wine_width, )
# #             elif random_row_f[5] == 'White':
# #                 st.image('../images/white.png', width=wine_width)
# #             elif random_row_f[5] == 'Rose':
# #                 st.image('../images/rose.png', width=wine_width)
# #             elif random_row_f[5] == 'Sparkling':
# #                 st.image('../images/sparkling.png', width=wine_width)

# #         with col2:
# #             st.image('../images/casi_medium.png', width=casi_width)

# #         with col3:
# #             st.header('Answer here:')
# #             player_answer = st.text_input(label = "USD", max_chars=7, key='player_answer', on_change=answer_function)


# #     # REVIEW ANSWER 
# #     if st.session_state["answer"] in ["answer correct", "answer incorrect"]:
# #         st.title("Can you beat Casi our in-house sommelier?")
# #         random_row_f = pd.Series(st.session_state['random_row_f'])
# #         player_answer, casi_answer, real_price = answer_function()

# #         col1, col2, col3 = st.columns(3)
# #         with col1:
# #             st.markdown(f"## Price: ${real_price}")
# #             st.markdown(f"## Rating: {random_row_f[8]}/5")
# #             # Add more details as needed
# #             f"How does it compare to vintage averages in {random_row_f[2]}?"
# #             st.dataframe(vis.compare_close_vintages_in_a_country(df, random_row_f[2], random_row_f[3]), hide_index=True)

# #         with col2:
# #             image_path = '../images/casi_sad.png' if st.session_state["answer"] == "answer correct" else '../images/casi_happy.png'
# #             st.image(image_path, width=casi_width)

# #         with col3:
# #             header_text = 'Nice work you beat Casi!' if st.session_state["answer"] == "answer correct" else 'Sorry, Casi beat you!'
# #             st.header(header_text)
# #             st.markdown(f"The real price was ${real_price}.")
# #             st.markdown(f"Casi guessed ${casi_answer}.")
# #             st.markdown(f"**You guessed ${player_answer}.**")
# #             # col3.metric(label="How close were you?", value=f"${(casi_answer- real_price)}", delta=f"${(player_answer-real_price)}")
# #             st.button('Play again', on_click=next_question)


# # def valuations():
# #     # VALUATION SECTION 
# #     if 'wine_inputted' not in st.session_state:
# #         st.session_state["answer"] = "before valuation"
        
# #     if st.session_state["answer"] == "before valuation":
# #         st.title("What are the details of the wine you'd like valued?")

# #         col1, col2, col3 = st.columns(3)
# #         with col1:
# #             st.markdown(f"#Price: $")
# #             # # Add more details as needed

# #         with col2:
# #             image_path = '../images/casi_medium.png'
# #             st.image(image_path, width=casi_width)

# #             st.button('Value my wine', on_click=do_valuation)

# #     # DO VALUATION
# #     if st.session_state["answer"] == "do valuation":
# #         st.title("What are the details of the wine you'd like valued?")

# #         col1, col2, col3 = st.columns(3)
# #         with col1:

# #             st.markdown(f"You asked casi to value a wine.")
# #             # Add more details as needed
# #             #f"How does it compare to vintage averages in {holder[2]}?"
# #             #st.dataframe(vis.compare_close_vintages_in_a_country(df, holder[2], holder[3]), hide_index=True)

# #         with col2:
# #             image_path = '../images/casi_happy.png'
# #             st.image(image_path, width=casi_width)

# #         with col3:
# #             header_text = 'This should cost ¢8749.99'
# #             # display details of the wine 
# #             st.button('Play against Casi', on_click=next_question)

# #             st.markdown(f"Or get casi to price another wine for you:")
# #             st.button('Value another bottle', on_click=valuation_input)



# # if options == "Valuations":
# #     valuations()

# # if options == "Game":
# #     game()







# st.write(st.session_state)

# # """
# #         st.markdown(f"{random_row_f[0]}")
# #         st.markdown(f"Country: {random_row_f[2]}")
# #         st.markdown(f"Region: {random_row_f[1]}")
# #         st.markdown(f"Vintage: {random_row_f[3]}")
# #         st.markdown(f"Variety: {random_row_f[5]}")
# #         st.markdown(f"Grape: {random_row_f[5]}")
# #         st.markdown(f"ABV: {random_row_f[9]}")
# #         st.markdown(f"Producer: {random_row_f[4]}")
# # """