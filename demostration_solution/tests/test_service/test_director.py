import pytest

from demostration_solution.service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_mok):
        self.director_service = DirectorService(dao=director_mok)

    def test_get_one(self, data_director):
        search_director = self.director_service.get_one(1)
        director = data_director.get(1)
        assert search_director == director
        assert search_director is not None
        assert search_director.id is not None

    def test_get_all(self):
        search_directors = self.director_service.get_all()
        assert search_directors is not None

    def test_create(self, new_director):
        create_director = self.director_service.create(new_director)
        assert create_director is not None
        assert create_director == new_director

    def test_update(self, new_director):
        update_director = self.director_service.update(new_director)
        assert update_director == new_director
        assert update_director is not None

    def test_partially_update(self, data_director):
        test_dir = {"id": 1, "name": "Nikita"}
        self.director_service.partially_update(test_dir)
        assert data_director.get(1).name == 'Nikita'

    def test_delete(self):
        self.director_service.delete(1)

