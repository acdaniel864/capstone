import pickle
import streamlit as st
import pandas as pd
import numpy as np
import gzip, pickle, pickletools
import random 
import matplotlib.pyplot as plt
import shap
from pathlib import Path

st.set_page_config(
    page_title="Play",
)
st.sidebar.success("Select a mode above.")


# BASIC START UP STUFF 
if "player_answer" not in st.session_state:
    st.session_state.answer = "not done"

if "player_answer" not in st.session_state:
    st.session_state.shap = "not done"

casi_width = 175

# Set the base directory to the parent of the current script's directory
base_dir = Path(__file__).resolve().parent.parent

# Define file paths using pathlib
clean_combined_wines_path = base_dir / 'app' / 'clean_combined_wines_copy.csv'
df_backend_path = base_dir / 'app' / 'app_backend.csv'
df_frontend_path = base_dir / 'app' / 'app_frontend.csv'
model_filepath = base_dir / 'models' / 'casi_rf_production.pkl'

# Load datasets
df = pd.read_csv(clean_combined_wines_path)
df_backend = pd.read_csv(df_backend_path)
df_frontend = pd.read_csv(df_frontend_path)

# Load the model
with gzip.open(model_filepath, 'rb') as f:
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

def compare_close_vintages_in_a_country(df, country, vintage, show_country = False):

    """
    Compares specified vintage with its closest vintages within a country based on median ratings
    and prices. It selects up to six closest vintages for comparison if the country has at least
    three vintages. The function rounds ratings and prices to two decimal places.

    Parameters:
    - df (DataFrame): Dataset with wine details.
    - country (str): Country for vintage comparison.
    - vintage (int or str): Target vintage year.
    - show_country (bool, optional): Adds country name to output if True. Defaults to False.

    Returns:
    - DataFrame: Closest vintages comparison or message for insufficient data.
    """

    country_df = df[df['country'] == country]
    
    # Check there are at least 3 vintages in the country
    vintage_counts = country_df.groupby('vintage').filter(lambda x: len(x) >= 3)
    
    # Calculate average rating and price by vintage.
    avg_metrics_by_vintage = vintage_counts.groupby('vintage')[['rating', 'price']].median().reset_index()
    
    avg_metrics_by_vintage['rating'] = avg_metrics_by_vintage['rating'].round(2)
    avg_metrics_by_vintage['price'] = avg_metrics_by_vintage['price'].round(2)
    
    vintage_position = avg_metrics_by_vintage[avg_metrics_by_vintage['vintage'] == vintage].index
    
    if not vintage_position.empty:
        position = vintage_position[0]
        
        # Find start and end positions for the vintage.
        start_pos = max(0, position - 3)
        end_pos = min(len(avg_metrics_by_vintage), position + 4)
        
        # Choose closest 6
        closest_vintages = avg_metrics_by_vintage.iloc[start_pos:end_pos].copy()
        if show_country == True:
          closest_vintages['Country'] = country 
        closest_vintages.rename(columns={'vintage': 'Vintage', 
                                         'rating' : 'Avg Rating', 'price' : 'Avg Price'}, inplace = True)
        closest_vintages['Vintage'] = closest_vintages['Vintage'].astype(str)
        return closest_vintages
    else:
        print("We don't have enough data for vintage comparison on this occasion.")

# INITIAL (NEXT QUESTION)
if st.session_state.answer == "not done":
    real_price, casi_answer, random_row_b, random_row_f = next_question()
    # DESIGN STUFF
    st.title("Can you beat CASI our in-house sommelier?")
    st.table(random_row_f.to_frame().transpose().drop(columns = ['Log Price', 'Price ($)', 'name', 'ABV', 'Age']))

    col1, col2, col3 = st.columns([1, 1, 1])  

    with col1:
        st.markdown(f"### Name:  \n **{random_row_f[0]}**")

        wine_width = 60
        if random_row_f[5] == 'Red':
            image_path = base_dir / 'images' / 'red.png'
            st.image(str(image_path), width=wine_width, )
        elif random_row_f[5] == 'White':
            image_path = base_dir / 'images' / 'white.png'
            st.image(str(image_path), width=wine_width)
        elif random_row_f[5] == 'Rose':
            image_path = base_dir / 'images' / 'rose.png'
            st.image(str(image_path), width=wine_width)
        elif random_row_f[5] == 'Sparkling':
            image_path = base_dir / 'images' / 'sparkling.png'
            st.image(str(image_path), width=wine_width)

    with col2:
        casi_path = base_dir / 'images' / 'casi_medium.png'
        st.image(str(casi_path), width=casi_width)

    with col3:
        st.markdown('### Answer here:')
        player_answer = st.text_input(label = "USD", max_chars=7, key='player_answer', on_change=answer_function)
        
# REVIEW ANSWER 
if st.session_state["answer"] in ["answer correct", "answer incorrect"]:
    st.title("Can you beat CASI our in-house sommelier?")
    random_row_f = pd.Series(st.session_state['random_row_f'])
    random_row_b = pd.Series(st.session_state['random_row_b'])
    player_answer, casi_answer, real_price = answer_function()

    col1, col2, col3 = st.columns([4, 4, 5])
    with col1:
        st.markdown(f"## Price: ${real_price}")
        st.markdown(f"## Rating: {random_row_f[8]}/5")
        f"How does it compare to vintage averages in {random_row_f[2]}?"
        st.dataframe(compare_close_vintages_in_a_country(df, random_row_f[2], random_row_f[3]), hide_index=True)

    with col2:
        casi_path = base_dir / 'images' / 'casi_sad.png' if st.session_state["answer"] == "answer correct" else base_dir / 'images' / 'casi_happy.png'
        st.image(str(casi_path), width=casi_width)

    with col3:
        header_text = 'Nice work you beat Casi!' if st.session_state["answer"] == "answer correct" else 'Casi wins!'
        st.header(header_text)
        st.markdown(f"The real price was ${real_price}")
        st.markdown(f"Casi guessed ${casi_answer}")
        st.markdown(f"**You guessed ${player_answer}**")
        st.markdown(f"Why did Casi choose that price:")
        X_with_price = random_row_b.to_frame().transpose()
        X = X_with_price.drop(columns = ['log_price'])
        # featureimp = model.feature_importances_
        # global_importances = pd.Series(index=X.columns, data=featureimp)
        
        # generate SHAP values
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        featurenames = [i.replace('_', ' ').title() for i in X]

        # SHAP summary plot
        shap.summary_plot(shap_values, feature_names=featurenames, max_display=7, plot_type="bar", color='mediumpurple')

        # Capture the current figure after it has been generated by SHAP
        fig = plt.gcf()  
        st.pyplot(fig)
        plt.clf()
        st.button('Play again', on_click=next_question)
        # st.bar_chart(global_importances)

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
        

