from driverutil.Browser import Browser


def before_scenario(context, scenario):
    context.browser = Browser().getbrowser('chrome')


def after_scenario(context, scenario):
    context.browser.quit()
