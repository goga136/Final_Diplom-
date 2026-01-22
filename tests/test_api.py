import pytest
import requests
import allure

from config import API_URL, HEADERS


@allure.feature("Kinopoisk API")
@pytest.mark.api
class TestKinopoiskAPI:

    @allure.story("Получение фильма по валидному ID")
    def test_get_movie_success(self):
        response = requests.get(f"{API_URL}/301", headers=HEADERS)

        assert response.status_code == 200
        assert "name" in response.json()

    @allure.story("Запрос фильма с невалидным ID")
    def test_get_movie_invalid_id(self):
        response = requests.get(f"{API_URL}/-1", headers=HEADERS)

        assert response.status_code == 404

    @allure.story("Проверка наличия ID фильма в ответе")
    def test_movie_has_id(self):
        response = requests.get(f"{API_URL}/301", headers=HEADERS)

        body = response.json()
        assert "id" in body or "filmId" in body

    @allure.story("Проверка наличия рейтинга фильма")
    def test_movie_has_rating(self):
        response = requests.get(f"{API_URL}/301", headers=HEADERS)

        body = response.json()
        assert "rating" in body

    @allure.story("Запрос без API ключа")
    def test_api_without_key(self):
        response = requests.get(f"{API_URL}/301")

        assert response.status_code in (401, 403)

