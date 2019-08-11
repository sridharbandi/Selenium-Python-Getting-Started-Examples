from driverutil.browser import Browser


def before_scenario(context, scenario):
    context.browser = Browser().getbrowser('chrome')


def after_scenario(context, scenario):
    context.browser.quit()
