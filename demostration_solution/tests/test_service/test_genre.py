import pytest

from demostration_solution.service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_mok):
        self.genre_service = GenreService(genre_mok)

    def test_get_one(self, data_genre):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre == data_genre.get(1)

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None

    def test_create(self, new_genre):
        new_genre = self.genre_service.create(new_genre)
        assert new_genre is not None

    def test_partially_update(self, data_genre):
        self.genre_service.partially_update({"id": 1, "name": 'Test'})
        update_genre = data_genre.get(1)
        assert update_genre.name == 'Test'

    def test_update(self, new_genre):
        self.genre_service.update(new_genre)

    def test_delete(self):
        self.genre_service.delete(1)
