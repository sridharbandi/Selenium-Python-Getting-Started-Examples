## Selenium Python Behave BDD Template to getting started with

To automate [Selenium Webdriver](https://docs.seleniumhq.org/projects/webdriver/) binaries management in runtime am using [webdrivermanager](https://github.com/SergeyPirogov/webdriver_manager), an excellent library by [Serhii Pirohov](https://github.com/SergeyPirogov)

### How to use?
Create the Page Objects of your Web application under **_pageobjects_** package and call those Page Objects in your  step definitions under **_features/steps_** package and create feature files under **_features_** folder(Sample Page Objects, Step defs & feature file included in this template)

### Install
To install the required dependencies issue the below command in project root directory
```javascript
pip3 install -r requirements.txt
```

### How to run?
Issue the below commands in project root directory

```javascript
behave
```
By default it runs in Chrome browser, you can specify which browser to use as well
```javascript
behave --browser=firefox
```
> Make sure to set the PYTHONPATH in environment variables.  Or else it may throw an error - ```ModuleNotFoundError: No module named '<package>'```
> Refer [https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html](https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html)


Currently supported browsers are
* chrome
* firefox
* edge
* ie

> Feel free to modify it to your own needs :)