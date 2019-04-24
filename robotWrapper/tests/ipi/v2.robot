*** Settings ***
Documentation       Subsuite 2
Library             DateTime

*** Variables ***
${FOO}           ${3}

*** Test Cases ***

Stub Test
    [Tags]          Stub          IPI           v2
    ${time} =       Get Time
    Set Suite Metadata            Time          ${time}
    ${my_doc}=      Catenate                    \r\n Test Description:
    ${my_doc}=      Catenate      ${my_doc}     \n - Stub Test
    Set Test Documentation        ${my_doc}
