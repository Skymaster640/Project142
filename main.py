from re import M
from flask import Flask,jsonify,request
from storage import all_articles, liked_articles, notliked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-article")
def get_article():

    article_data = {
        "title": all_articles[0][12],
        "url": all_articles[0][11],
        "text": all_articles[0][13]
    }

    return jsonify({
        "data":article_data,
        "status":"Success"
    })


@app.route("/liked-article",methods = ["POST"])
def liked_article():
    articles = all_articles[0]
    liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status":"Success"
    }),201

@app.route("/unliked-article",methods = ["POST"])
def unliked_article():
    articles = all_articles[0]
    notliked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status":"Success"
    }),201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "title": article[0],
            "url": article[1],
            "text": article[2]
        }
        article_data.append(_d)
    return jsonify({
        "data":article_data,
        "status":"Success"
    }),200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[12])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "url": recommended[1],
            "text": recommended[2]
        }
        article_data.append(_d)
    return jsonify({
        "data":article_data,
        "status":"Success"
    }),200
    
if __name__ == "__main__":
    app.run()