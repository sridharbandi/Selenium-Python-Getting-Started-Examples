import pytest
from pageobjects.GoogleSearchPage import GoogleSearchPage
from pageobjects.SearchResultsPage import SearchResultsPage
from tests.BaseTest import BaseTest


@pytest.mark.incremental
class RunTest(BaseTest):

    def __init__(self):
        self.searchresultspage = SearchResultsPage(self.driver)
        self.googlesearchpage = GoogleSearchPage(self.driver)

    def testExample(self):
        self.driver.get("https://www.google.com/")
        self.googlesearchpage.searchfor("Selenium")
        self.searchresultspage.link_selenium_present()
