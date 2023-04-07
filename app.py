import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title='Movie Recommender', page_icon='random')

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a234ff57c821c6f69e8d3e657e2a1760&language=en-US')
    data = response.json()
    # st.text(response)
    # st.text(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a234ff57c821c6f69e8d3e657e2a1760&language=en-US')
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:5]
    # above line returns top 5 similar movies
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))

    return [recommended_movies,recommended_movies_poster]



st.title('Movie Recommender system')

selected_movie_name= st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    [names,posters] = recommend(selected_movie_name)
    # for i in recommendations:
    #     st.write(i)

    col1,col2,col3,col4,col5 = st.columns(5)
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