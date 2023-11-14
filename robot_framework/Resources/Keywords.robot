*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${USERNAME}       lasseboy  
${PASSWORD}       tanssija

*** Keywords ***
LoginToApplication
    Input Text       xpath://input[@id='username']    ${USERNAME}
    Input Text       xpath://input[@id='password']    ${PASSWORD}
    Sleep    0.5
    Click Element    xpath://button[normalize-space()='login']         # Login button
    Sleep    2
    Click Element    xpath://button[@class='ui mini button']           # Logout button
    