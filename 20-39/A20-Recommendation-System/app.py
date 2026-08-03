import streamlit as st
import pickle

# Load saved files
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

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
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")
st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get similar movie recommendations.")

selected_movie = st.selectbox("Choose a Movie",movies["title"].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Recommended Movies")
    for movie in recommendations:
        st.write(f"✅ {movie}")