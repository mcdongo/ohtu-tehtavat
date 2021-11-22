*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  aasi2  salasana22
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Register Command
    Input Credentials  aasi2  salasana22
    Input Register Command
    Input Credentials  aasi2  salasana22
    Output Should Contain  User with username aasi2 already exists

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  aa  salasana22
    Output Should Contain  Username too short


Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  aasi2  sala2
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  aasi2  salasana
    Output Should Contain  Invalid password