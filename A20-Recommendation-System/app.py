import streamlit as st
import pickle
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_pickle(file_name):
    file_path = BASE_DIR / file_name
    try:
        with file_path.open("rb") as file_handle:
            return pickle.load(file_handle)
    except FileNotFoundError:
        st.error(f"I could not find {file_name}. Please make sure the project files are in place and try again.")
        st.stop()

# Load saved files
movies = load_pickle("movies.pkl")
similarity = load_pickle("similarity.pkl")

# Recommendation function
def recommend(movie_name, top_n=5):

    if movie_name not in movies["title"].values:
        return []
    index = movies[movies["title"] == movie_name].index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)
    recommendations = []
    for i in distances[1:top_n+1]:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations


# Streamlit UI
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="centered")
st.title("🎬 Movie Recommendation System")
st.write("Pick a movie you already love, and I’ll suggest a few that feel like a good next watch.")

st.caption("Built with the TMDB 5000 dataset, TF-IDF features, and cosine similarity.")

selected_movie = st.selectbox("Choose a movie", movies["title"].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.subheader("Recommended Movies")
        for movie in recommendations:
            st.write(f"• {movie}")
    else:
        st.info("I could not find close matches for that title, but you can try another favorite.")