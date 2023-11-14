*** Settings ***
Documentation    This is a basic sample test for login into an example ReactJS app site. Default browser is chrome mode is headless. 
...    Default is that selenium drivers are under certain directory e.g. c:/bin/ which is added to the path. Now chromedriver is also here in root.
...    Run test with command: [robot.exe -d Logs TestCases] or [robot -d Logs -t "LoginTest" TestCases]

Library  SeleniumLibrary
Resource    ../Resources/Keywords.robot

Suite Setup      Log To Console    Opening Suite - Inserting possible test data
Test Setup       Open Browser      ${URL}    ${BROWSER_HEADLESS}
Test Teardown    Close Browser
Suite Teardown   Log To Console    Closing Suite - Cleanup

*** Variables ***
${BROWSER}             chrome
${BROWSER_HEADLESS}    headlesschrome
${url}                 https://dance-calendar.herokuapp.com


*** Test Cases ***
LoginTest
    [Documentation]    Test case is E2E scenario for login & logout into a web application
    [Tags]                     smoke            
    Set Selenium Speed         .1s
    Set Selenium Timeout       5s
    Maximize Browser Window
    LoginToApplication
