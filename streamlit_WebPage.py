''' In this notebook, I developed an interactive book recommendation system using Streamlit and Singular Value 
Decomposition (SVD). The app provides personalized book suggestions by analyzing user preferences and predicting top 
recommendations. This project aims to enhance users' reading experiences through tailored book recommendations.'''


import streamlit as st
import pickle
import pandas as pd

# Load the models and data
with open('svd.pickle', 'rb') as f:
    svd = pickle.load(f)

with open('U_sigma_Vt.pickle', 'rb') as f:
    U, sigma, Vt = pickle.load(f)

with open('recommender_books_svd.pickle', 'rb') as f:
    recommender_books_svd = pickle.load(f)

books_data = pd.read_csv('Books.csv')
popular_books = pd.read_csv('popular_books.csv')
um = pd.read_csv('um.csv', index_col=0)
um_imputed = um.fillna(0)
um_repro = pd.read_csv('um_repro.csv', index_col=0)

print(um_repro.index)

# Streamlit app
st.title("Book Recommendation System")

user_id = st.text_input("Enter your user ID:")

def get_recommendations(user_id, popular_books, um_repro, n):

    '''
    This function generates book recommendations for a given user based on their past consumption and a user-item matrix.
    
    Parameters:
    - user_id: The ID of the user for whom recommendations are to be generated.
    - popular_books: A DataFrame containing information about popular books, including user consumption data.
    - um_repro: A user-item matrix where rows represent users and columns represent books, with values indicating user preferences.
    - n: The number of recommendations to generate.
    
    Steps:
    1. Identify the books that the user has already consumed by filtering the popular_books DataFrame using the user_id.
    2. Retrieve the user's book preferences from the um_repro matrix.
    3. Sort the user's book preferences in descending order to prioritize higher preferences.
    4. Remove the books that the user has already consumed from the list of preferences.
    5. Return the top 'n' book recommendations for the user.
    '''
    consumed = popular_books.loc[popular_books['user_id'] == user_id, 'parent_asin']
    user_books = um_repro.loc[user_id, :]
    user_books = user_books.sort_values(ascending=False)
    user_books = user_books.drop(index=consumed)
    return user_books.index[:n]

if st.button("Get Recommendations"):
    
    try:
        if user_id not in um_repro.index:
            st.error("User ID not found in the database.")
        else:
            recommendations = get_recommendations(user_id, popular_books, um_repro, 3)
            st.write("Recommended books:")
            st.write(recommendations)
    except Exception as e:
        st.error("An error occurred: " + str(e))