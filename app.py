import streamlit as st
import pickle
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyArcE_GzpLcz9gpECiH11Pll-lUTw9k8B0")
model = genai.GenerativeModel("gemini-1.5-pro")

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

def fetch_poster(movie_name):
    file_path = f"posters/{movie_name}.png"
    if os.path.exists(file_path):
        return file_path

    prompt = f"Create a cinematic movie poster for the movie {movie_name}"
    try:
        response = model.generate_content(prompt)
        for part in response.parts:
            if hasattr(part, "inline_data"):
                with open(file_path, "wb") as f:
                    f.write(part.inline_data.data)
                return file_path
    except:
        pass
    return "https://via.placeholder.com/500x750?text=Poster"

selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []

    for i in distance[1:6]:
        title = movies.iloc[i[0]].title
        recommend_movie.append(title)
        recommend_poster.append(fetch_poster(title))

    return recommend_movie, recommend_poster

if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(movie_name[i])
            st.image(movie_poster[i])
