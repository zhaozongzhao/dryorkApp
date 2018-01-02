
#部分引用Library
*** Settings ***
Library  RequestsLibrary
Library  Collections

#编写测试用例
*** Test Cases ***
test_get_event_list
    ${payload}=    Create Dictionary    eid=1
    Create Session    event    http://127.0.0.1:8000/api
    ${r}=    Get Request    event    /get_event_list/    params=${payload}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}   message
    Should Be Equal    ${msg}    success
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(200)
    Should Be Equal    ${sta}    ${status}

