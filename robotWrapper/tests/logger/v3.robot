*** Settings ***
Documentation       Subsuite 3
Library             DateTime

*** Variables ***
${FOO}           ${5}

*** Test Cases ***

Stub Test
    [Tags]          Stub          Logger        v3
    ${time} =       Get Time
    Set Suite Metadata            Time          ${time}
    ${my_doc}=      Catenate                    \r\n Test Description:
    ${my_doc}=      Catenate      ${my_doc}     \n - Stub Test
    Set Test Documentation        ${my_doc}
