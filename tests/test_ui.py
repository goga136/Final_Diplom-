import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL


@pytest.mark.ui
@allure.feature("Kinopoisk UI")
class TestKinopoiskUI:

    def skip_if_blocked(self, driver):
        current_url = driver.current_url.lower()

        if "captcha" in current_url:
            pytest.skip("Капча Kinopoisk — UI тест пропущен")

        if "sso" in current_url or "passport.yandex" in current_url:
            pytest.skip("Редирект на авторизацию — UI тест пропущен")

    def test_main_page_opens(self, driver):
        driver.get(BASE_URL)
        self.skip_if_blocked(driver)

        assert "Кинопоиск" in driver.title

    def test_search_input_exists(self, driver, wait):
        driver.get(BASE_URL)
        self.skip_if_blocked(driver)

        search_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "kp_query"))
        )
        assert search_input.is_displayed()

    def test_header_exists(self, driver, wait):
        driver.get(BASE_URL)
        self.skip_if_blocked(driver)

        header = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "header"))
        )
        assert header.is_displayed()

    def test_footer_exists(self, driver, wait):
        driver.get(BASE_URL)
        self.skip_if_blocked(driver)

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        footer = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//footer"))
        )
        assert footer.is_displayed()

    def test_logo_clickable(self, driver, wait):
        driver.get(BASE_URL)
        self.skip_if_blocked(driver)

        logo = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/']"))
        )

        assert logo.is_displayed()
        logo.click()


