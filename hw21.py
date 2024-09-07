
დავალების შესასრულებლად გამოიყენეთ movies.json

წაიკითხეთ მოცემული ფაილი და ამავე ფაილში ჩაწერეთ ის ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე მეტი და ჟანრი არის Crime,
ხოლო Crime სიტყვა ჟანრში შეცვალეთ New_Crime-ით. ამავე ფაილში ჩაწერეთ ისეთი ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე ნაკლები, 
ჟანრი არის Drama და ჟანრის სახელი ჩაუწერეთ Old_Drama. იმ ფილმებს, რომელიც 2000 წელს არის გამოშვებული ჟანრში ჩაუმატეთ New_Century 
და ეს ფილმებიც ამავე ფაილში ჩაწერეთ.

import json


class Movie(object):
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre


def to_dict (self):
    return {
        'title': self.title,
       'release_year': self.release_year,
        'genre': self.genre
    }


def serialize_movie (object):
    if isinstance(object, Movie):
        return {
            'title': movie.title,
           'release_year': movie.release_year,
            'genre': movie.genre
        }



movie_file = 'movies.json'
with open(movie_file, 'r') as file:
    data = json.load(file)

for movie in data['movies']:
    if movie['release_year'] > 2000:
        if movie['genre'] == 'Crime':
            movie['genre'] = 'New_Crime'
    elif movie['release_year'] < 2000:
        if movie['genre'] == 'Drama':
            movie['genre'] = 'Old_Drama'
    elif movie['release_year'] == 2000:
        movie['genre'] = 'New_Century'

with open(movie_file, 'w') as file:
    json.dump(data, file, indent=4. default=serialize_movie)

