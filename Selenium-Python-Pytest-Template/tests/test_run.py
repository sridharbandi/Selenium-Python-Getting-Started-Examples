import pytest

from pageobjects.google_search_page import GoogleSearchPage
from pageobjects.search_results_page import SearchResultsPage
from tests.base_test import BaseTest


@pytest.mark.incremental
class test_run(BaseTest):

    def test_example(self):
        self.searchresultspage = SearchResultsPage(self.driver)
        self.googlesearchpage = GoogleSearchPage(self.driver)
        self.driver.get("https://www.google.com/")
        self.googlesearchpage.searchfor("Selenium")
        self.searchresultspage.link_selenium_present()

