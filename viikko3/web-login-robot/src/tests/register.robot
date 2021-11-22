*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  aasi2
    Set Password  salasana2
    Set Password Confirmation  salasana2
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  salasana2
    Set Password Confirmation  salasana2
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  aasi2
    Set Password  salis2
    Set Password Confirmation  salis2
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  aasi2
    Set Password  salasana2
    Set Password Confirmation  salasana12
    Submit Credentials
    Register Should Fail With Message  Password and confirmation password are not equal


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}