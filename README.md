# First Page Conference

1. Automatically download all papers of a particular conference.
2. Create a pdf file containing the first pages of these papers.

# Prerequisites

* pdftk (sudo snap install pdftk if using Ubuntu 18.04)
* some python packages: requests, HTMLParser

# How to Run

`python main.py [IEEE|ACM] [conference ID] [filter ID*] [output file]`

*filter ID is optional and only needed for IEEE.

# Find Conference ID

For ACM library, you can first find your conference from
[ACM Conference List](https://dl.acm.org/events.cfm), and then go to the
conference page (e.g. [ISCA](https://dl.acm.org/event.cfm?id=RE239)) and check
the "Publication Archive" tab (e.g. [ISCA 2017](https://dl.acm.org/citation.cfm?id=3079856)). The conference ID is in the URL (e.g., https://dl.acm.org/citation.cfm?id=3079856)
In the end, you can run our script such as

`python main.py ACM 3079856 summary_ACM.pdf`

For IEEE library, you can find your conference from [IEEE Conference List](http://ieeexplore.ieee.org/browse/conferences/title/). After finding your conference, (e.g., Oakland 2018, at [https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=8418581](https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=8418581), please scroll down and go to the second page. On this page, check
`punumber` and `filter` fields in the URL,
[https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=8418581&filter=issueId EQ "8418583" &pageNumber=2](https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=8418581&filter=issueId EQ "8418583" &pageNumber=2)). Specifically, for the filter field, please check the number between double quotes  [filter=issueId EQ "8418583"].
In the end, you can run our script such as

`python main.py IEEE 8418581 8418583 summary_IEEE.pdf`

# Limitation

Currently we only support ACM and IEEE libraries.
