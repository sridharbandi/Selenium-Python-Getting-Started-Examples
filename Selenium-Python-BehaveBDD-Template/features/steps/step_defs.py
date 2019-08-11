from behave import given, when, then
from pageobjects.google_search_page import GoogleSearchPage
from pageobjects.search_results_page import SearchResultsPage


@given(u'User is on Google search page')
def step_impl_goto_google(context):
    context.browser.get("https://www.google.com/")
    context.googlesearchpage = GoogleSearchPage(context.browser)


@when(u'User searches for Selenium')
def step_impl_search_selenium(context):
    context.googlesearchpage.searchfor("Selenium")
    context.searchresultspage = SearchResultsPage(context.browser)


@then(u'User can see Selenium results')
def step_impl_verify_results(context):
    context.searchresultspage.link_selenium_present()
