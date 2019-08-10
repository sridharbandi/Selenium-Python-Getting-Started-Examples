from driverutil.Browser import Browser
from pageobjects.GoogleSearchPage import GoogleSearchPage
from pageobjects.SearchResultsPage import SearchResultsPage


def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser = Browser().getbrowser('chrome')
        context.googlesearchpage = GoogleSearchPage(context.browser)
        context.searchresultspage = SearchResultsPage(context.browser)


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
