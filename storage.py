import csv
all_movies = []

with open('articles.csv')as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]


liked_articles = []
notliked_articles = []