import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDbPage:
    URL = "https://www.imdb.com/search/name/"

    def __init__(self, browser):
        self.browser = browser

    def go_to(self):
        self.browser.get(self.URL)

    def enter_name(self, name):
        name_input = self.browser.find_element_by_id("name-search-input")
        name_input.clear()
        name_input.send_keys(name)

    def enter_birth_year(self, year):
        year_input = self.browser.find_element_by_id("birthYear")
        year_input.clear()
        year_input.send_keys(year)

    def select_gender(self, gender):
        gender_select = self.browser.find_element_by_id("gender")
        gender_select.click()
        gender_option = self.browser.find_element_by_xpath(f"//option[text()='{gender}']")
        gender_option.click()

    def select_known_for(self, occupation):
        known_for_select = self.browser.find_element_by_id("knownFor")
        known_for_select.click()
        occupation_option = self.browser.find_element_by_xpath(f"//option[text()='{occupation}']")
        occupation_option.click()

    def click_search_button(self):
        search_button = self.browser.find_element_by_xpath("//button[text()='Search']")
        search_button.click()


def test_imdb_search():
    browser = webdriver.Chrome()
    imdb_page = IMDbPage(browser)
    imdb_page.go_to()

    # Fill data in input boxes
    imdb_page.enter_name("Tom Hanks")
    imdb_page.enter_birth_year("1956")

    # Select options in select boxes
    imdb_page.select_gender("male")

    # Select options in dropdown menu
    imdb_page.select_known_for("actor")

    # Click on search button
    imdb_page.click_search_button()

    # Wait for search results to appear
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "lister-list")))

    # Assert that search results are displayed
    assert "Results" in browser.title

    # Quit the browser
    browser.quit()