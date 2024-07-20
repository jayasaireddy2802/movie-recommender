import streamlit as st
import pickle as pk
import pandas as pd
import requests

def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ab9b1be869531b744f64a6424d798c6d&language=en-US'.format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dis = similarity[movie_index]
    movies_list = sorted(list(enumerate(dis)),reverse=True,key=lambda x : x[1])[1:6]
    l = []
    poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        l.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movie_id))
    return  l,poster

st.title("Movie Recommendation System")
movies_list = pk.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pk.load(open('similarity_matrix.pkl','rb'))
option = st.selectbox(
    "Select the movie",
    movies['title'].values)
st.write("You selected:", option)
if st.button('recommend'):
    names,posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

