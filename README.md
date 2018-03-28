# First Page Conference

1. Automatically download all papers of a particular conference.
2. Create a pdf file containing the first pages these papers.

# Prerequisites

* pdftk
* some python packages: requests, HTMLParser

# How to Run

`python main.py [IEEE|ACM] [conference ID] [output file]`

# Find Conference ID

For ACM library, you can first find your conference from
[ACM Conference List](https://dl.acm.org/events.cfm), and then go to the
conference page (e.g. [ISCA](https://dl.acm.org/event.cfm?id=RE239)) and check
the "Publication Archive" tab (e.g. [ISCA 2017](https://dl.acm.org/citation.cfm?id=3079856)). The conference ID is in the URL (e.g., https://dl.acm.org/citation.cfm?id=3079856)

For IEEE library, you can find your conference from [IEEE Conference List](http://ieeexplore.ieee.org/browse/conferences/title/), and then check the
`punumber` field in the conference URL (e.g., Oakland 2017, at
[http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7957740](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7957740)).
In the end, you can run our script such as

`python main.py IEEE 7957740 summary.pdf`

# Limitation

Currently we only support ACM and IEEE libraries.
