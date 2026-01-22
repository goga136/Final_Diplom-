import os

# API URL для Kinopoisk
API_URL = "https://api.kinopoisk.dev/v1/movie"

# Попытка получить ключ из переменной окружения
API_KEY = os.getenv("KINOPOISK_API_KEY")

# Если переменная не задана, можно использовать резервный ключ (для локальных тестов)
# Замените 'ваш_резервный_ключ_сюда' на реальный ключ, если хотите тестировать без переменной окружения
if not API_KEY:
    API_KEY = "H13CWGW-0XNMN22-N38R33C-5HWGQHJ"

HEADERS = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

# URL сайта Kinopoisk для UI тестов
BASE_URL = "https://www.kinopoisk.ru"
