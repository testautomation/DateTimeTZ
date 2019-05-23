*** Settings ***
Library    DateTimeTZ     #WITH NAME  DT



*** Test Cases ***
# Time Zone Test
#     # default
#     ${dt 1}=   Get Current Date  result_format=%Y-%m-%dT%H:%M:%S-%z
#     Log To Console    \n${dt 1}

#     # timezone local
#     ${dt 2}=   Get Current Date  time_zone=local  result_format=%Y-%m-%dT%H:%M:%S%z
#     Log To Console    ${dt 2}

#     # timezone utc
#     ${dt 2}=   Get Current Date  time_zone=utc  result_format=%Y-%m-%dT%H:%M:%S%z
#     Log To Console    ${dt 2}

Get Timestamp With Different Locales
    log to Console  \n
    ${timestamp}	Get Timestamp	locale=rus	time_format=dd LLL y H:mm:ss
    log to Console  ${timestamp}

    ${timestamp}	Get Timestamp	locale=en	time_format=dd LLL y H:mm:ss
    log to Console  ${timestamp}

    ${timestamp}	Get Timestamp	locale=de	time_format=dd LLL y H:mm:ss
    log to Console  ${timestamp}

Get Timestamp With TimeZone (short name)
    log to Console  \n
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss z
    log to Console  ${timestamp}

Get Timestamp With TimeZone (full name)
    log to Console  \n
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss zzzz
    log to Console  ${timestamp}

Get Timestamp With TimeZone (RFC 822 format)
    log to Console  \n
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss Z
    log to Console  ${timestamp}

Get Timestamp With TimeZone (GMT format)
    log to Console  \n
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss ZZZZ
    log to Console  ${timestamp}

Get Timestamp with TimeZone with small v
    log to Console  \n
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss v
    log to Console  ${timestamp}
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss vvvv
    log to Console  ${timestamp}

Get Timestamp with TimeZone with big V
    log to Console  \n
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss V
    log to Console  ${timestamp}
    ${timestamp}	Get Timestamp	locale=de	time_format=yyyy-mm-dd H:mm:ss VVVV
    log to Console  ${timestamp}