import streamlit as st
import pickle
import pandas as pd

def recommend(x):
    movies_index = movies[movies['title'] == x].index[0]

    movies_list = sorted(list(enumerate(similarity[movies_index])), reverse=True, key=lambda x: x[1])[1:6]

    l=[]
    for i in movies_list:
        l.append(movies.iloc[i[0]].title)
    return l

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# title of page
st.title('MOVIE RECOMMENDER SYSTEM')

# code for select box
option = st.selectbox('How would you like to be contacted?',movies['title'].values)

# code for button
if st.button('Recommend'):
    x = recommend(option)
    for i in x:
        st.write(i)
