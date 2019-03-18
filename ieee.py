import sys
import os
import requests
from HTMLParser import HTMLParser

#url_conference = 'http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=%s&pageNumber=%d'
url_conference  = 'https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=%s&filter=issueId EQ "%s"&pageNumber=%d'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'}
url_paper = 'http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=%s'

class ConferenceParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.papers = []
        self.start = False

    def handle_data(self, data):
        # Only papers have abstracts, so we only keep the pdf if we see "Abstract"
        if data == 'Abstract':
            self.start = True

    def handle_starttag(self, tag, attrs):
        if self.start and tag == 'a':
            attrs_dict = dict(attrs)
            if 'href' in attrs_dict and attrs_dict['href'] is not None and 'arnumber' in attrs_dict['href']:
                self.start = False
                href = attrs_dict['href']
                # href = 'stamp/stamp.jsp?tp=&arnumber=7958569'
                after_arnumber = href[href.find('arnumber'):]
                start = after_arnumber.find('=') + 1
                end = after_arnumber.find('&')
                if end == -1:
                    pid = after_arnumber[start:]
                else:
                    pid = after_arnumber[start:end]
                self.papers.append(pid)

class RenderParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.pdf = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'iframe':
            attrs_dict = dict(attrs)
            if 'src' in attrs_dict:
                self.pdf = attrs_dict['src']


class IEEE(object):
    def __init__(self, cid, issue_id, out_dir=None):
        self.cid = cid
        self.issue_id = issue_id
        if out_dir is None:
            self.out_dir = cid
        else:
            self.out_dir = out_dir
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        self.papers = []
        self.cookies = {}

    def parse_papers(self, cid, issue_id):
        page = 1
        papers = []
        while True:
            url = url_conference % (cid, issue_id, page)
            response = requests.get(url, cookies=self.cookies, headers=headers)
            self.cookies.update(response.cookies)
            parser = ConferenceParser()
            parser.feed(response.text)
            if len(parser.papers) > 0:
                papers += parser.papers
                page += 1
            else:
                break
        return papers

    def download_paper(self, pid):
        url = url_paper % pid
        response = requests.get(url, cookies=self.cookies, headers=headers)
        self.cookies.update(response.cookies)
        script = response.content
        parser = RenderParser()
        parser.feed(response.text)
        pdfurl = parser.pdf
        self.download_pdf(pdfurl, pid)

    def download_pdf(self, url, pid):
        response = requests.get(url, cookies=self.cookies, headers=headers)
        self.cookies.update(response.cookies)
        filename = os.path.join(self.out_dir, '%s.pdf' % pid)
        print filename
        with open(filename, 'wb') as f:
            f.write(response.content)

    def download_papers(self):
        self.papers = self.parse_papers(self.cid, self.issue_id)
        for p in self.papers:
            self.download_paper(p)

# Test
#conference = IEEE('7957740', '7958557')
#conference.download_papers()
