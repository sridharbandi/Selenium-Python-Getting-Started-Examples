from behave import given, when, then


@given(u'User is on Google search page')
def step_impl_goto_google(context):
    context.browser.get("https://www.google.com/")


@when(u'User searches for Selenium')
def step_impl_search_selenium(context):
    context.googlesearchpage.searchfor("Selenium")


@then(u'User can see Selenium results')
def step_impl_verify_results(context):
    context.searchresultspage.link_selenium_present()
