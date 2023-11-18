
# Radiam's challenges

This project was developed to complete Radiam's challenges


## Reports

Allure reports were used for metrics, I deployed one of my test's reports on Netfly.

Link: https://comfy-mandazi-f1a0c1.netlify.app/

if you want to generate reports you can execute the following command lines:

Generate datas for allure reports in reports folder:
```bash
pytest --alluredir=reports .\src\tests\test_hipster_messeger.py
```
execute allura serve to see the report:

```bash
allure serve reports
```

it's necessary to install JAVA to run allura reports locally


# Documentation

It was created One feature for Front-end explaning how I would execute tests on PHPTRVELS website.

It was created automated tests for Back-end where I developed tests for The weather api

The API's tests were splitted in diferrent files to be organized on the folder of project.

test_code_responses.py - Test the reponses of API's. I've created a function to simulate 429 response code.
It was asked how 429 code could to be tested It could be tested by a recursion function, that function calls itself until
generate too many requests. But the way I've created my function works in a diferrent way, test_request_too_many_resquests function execute requests in more than one Thread, in other words It executes the same API in multiple processings until the response code retrives 429 number. It is commented from 38 to 50.

test_current_and_forecasts_weather.py - Test current and forecasts parameter for API

test_daily_aggretion.py - Test daily aggretion parameter for API

test_timestamp_weather.py = Test timestamp parameter for API

reports: reports genereted by Allure

## Requirements


pytest==7.4.3

pytest_bdd==7.0.0

## Running the test

if you want to run the test, you can use the pytest execution:

```bash
   pytest .\src\tests\back-end\
```

run one test by time:

```bash
 pytest .\src\tests\back-end\test_code_responses.py
```



