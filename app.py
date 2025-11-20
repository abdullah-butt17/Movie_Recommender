from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"]

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),
                       reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


@app.route("/")
def home():
    movie_list = movies['title'].values
    return render_template("index.html", movie_list=movie_list)


@app.route("/recommend", methods=["POST"])
def recommend_api():
    movie_name = request.form['movie']
    result = recommend(movie_name)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
