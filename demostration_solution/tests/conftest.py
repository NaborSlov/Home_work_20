# Фикстуры для тестов

import time

import pytest
from unittest.mock import MagicMock

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.dao.model.genre import Genre
from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO


@pytest.fixture
def data_director():
    """
    Данные для теста DirectorService
    """
    return {
        1: Director(id=1, name="Valera"),
        2: Director(id=2, name="Katerina"),
        3: Director(id=3, name="Maxim"),
        4: Director(id=4, name="Egor"),
        5: Director(id=5, name="Dimas")
    }


@pytest.fixture
def new_director():
    """
    Данные для проверки создания директора
    """
    return {'id': 6, 'name': "Nikita"}


@pytest.fixture
def director_mok(data_director, new_director):
    """
    Мок класса DirectorDAO
    """
    dir_mok_dao = DirectorDAO(None)
    dir_mok_dao.get_one = MagicMock(return_value=data_director.get(1))
    dir_mok_dao.get_all = MagicMock(return_value=data_director.values())
    dir_mok_dao.create = MagicMock(return_value=new_director)
    dir_mok_dao.update = MagicMock(return_value=new_director)
    dir_mok_dao.delete = MagicMock()

    return dir_mok_dao


@pytest.fixture
def data_genre():
    """
    Данные для теста GenreService
    """
    return {1: Genre(id=1, name='genre1'),
            2: Genre(id=2, name='genre2'),
            3: Genre(id=3, name='genre3'),
            4: Genre(id=4, name='genre4'),
            5: Genre(id=5, name='genre5')}


@pytest.fixture
def new_genre():
    """
    Данные для проверки создания жанра
    """
    return {"id": 6, 'name': 'genre6'}


@pytest.fixture
def genre_mok(data_genre, new_genre):
    """
    Мок класса GenreDAO
    """
    genre_mok = GenreDAO(None)
    genre_mok.get_one = MagicMock(return_value=data_genre.get(1))
    genre_mok.get_all = MagicMock(return_value=data_genre.values())
    genre_mok.create = MagicMock(return_value=Genre(**new_genre))
    genre_mok.update = MagicMock()
    genre_mok.delete = MagicMock()

    return genre_mok


@pytest.fixture
def data_movie(data_director, data_genre):
    """
    Данные для теста MovieService
    """
    movie1 = Movie(
        id=1,
        title='movie1',
        description='description1',
        trailer='trailer1',
        year=1000,
        rating=1.1,
        genre_id=1,
        genre=data_genre.get(1),
        director_id=1,
        director=data_director.get(1))

    movie2 = Movie(
        id=2,
        title='movie2',
        description='description2',
        trailer='trailer2',
        year=2000,
        rating=2.1,
        genre_id=2,
        genre=data_genre.get(2),
        director_id=2,
        director=data_director.get(2))

    movie3 = Movie(
        id=3,
        title='movie3',
        description='description3',
        trailer='trailer3',
        year=3000,
        rating=3.1,
        genre_id=3,
        genre=data_genre.get(3),
        director_id=3,
        director=data_director.get(3))

    return {1: movie1, 2: movie2, 3: movie3}


@pytest.fixture
def new_movie(data_director, data_genre):
    """
    Данные для проверки создания фильма
    """
    return {
        'id': 4,
        'title': 'movie4',
        'description': 'description4',
        'trailer': 'trailer4',
        'year': 4000,
        'rating': 4.1,
        'genre_id': 4,
        'director_id': 4}


@pytest.fixture
def update_movie():
    """
    Данные для проверки обновления фильма
    """
    return {
        'id': 1,
        'title': 'movie_test',
        'description': 'description_test',
        'trailer': 'trailer_test',
        'year': 5000,
        'rating': 5.1,
        'genre_id': 5,
        'director_id': 5}


@pytest.fixture
def movie_mok(data_movie, new_movie):
    """
    Мок класса MovieDAO
    """
    movie_mok = MovieDAO(None)
    movie_mok.get_one = MagicMock(return_value=data_movie.get(1))
    movie_mok.get_all = MagicMock(return_value=data_movie.values())
    movie_mok.create = MagicMock(return_value=Movie(**new_movie))
    movie_mok.update = MagicMock()
    movie_mok.delete = MagicMock()

    return movie_mok


@pytest.fixture(autouse=True, scope='module')
def separator():
    yield
    print('\n--------------------')


@pytest.fixture(autouse=True, scope='session')
def time_after_tests():
    yield
    now = time.time()
    print("\n--------------------")
    print(f"finished: {time.strftime('%d %b %X', time.localtime(now))}")
    print('--------------------')
