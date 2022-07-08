import pytest

from demostration_solution.service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_mok):
        self.movie_service = MovieService(movie_mok)

    def test_get_one(self, data_movie):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie == data_movie.get(1)

    def test_get_all(self, data_movie):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) == len(data_movie)

    def test_create_movie(self, new_movie):
        new_movie = self.movie_service.create(new_movie)
        assert new_movie is not None

    def test_partially_update(self, data_movie, update_movie):
        self.movie_service.partially_update(update_movie)
        update_movie_one = data_movie.get(1)
        assert update_movie_one.title == update_movie.get('title')
        assert update_movie_one.trailer == update_movie.get('trailer')

    def test_update(self, new_movie):
        self.movie_service.update(new_movie)

    def test_delete(self):
        self.movie_service.delete(1)



