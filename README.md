# First Page Conference

Get the first page of all the papers in a conference.

# Prerequisites

* pdftk
* some python packages: requests, HTMLParser

# How to Run

`python main.py [conference ID] [output file]`

To find conference ID, you can first find your conference from
[ACM Conference List](https://dl.acm.org/events.cfm), and then go to the
conference page (e.g. [ISCA](https://dl.acm.org/event.cfm?id=RE239)) and check
the "Publication Archive" tab (e.g. [ISCA 2017](https://dl.acm.org/citation.cfm?id=3079856)). The conference ID is in the URL (e.g., https://dl.acm.org/citation.cfm?id=3079856)

# Limitation

Currently we only support ACM library.
