import sys
import os
import requests
from HTMLParser import HTMLParser

class ConferenceParser(HTMLParser):
    def __init__(self, out_dir):
        HTMLParser.__init__(self)
        self.papers = []
        self.out_dir = out_dir

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs_dict = dict(attrs)
            if 'href' in attrs_dict and 'doi.org' in attrs_dict['href']:
                if self.out_dir in attrs_dict['href']:
                    pid = attrs_dict['href'].split('.')[-1]
                    self.papers.append(pid)

url_conference = 'https://dl.acm.org/citation.cfm?id=%s&preflayout=flat#prox'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'}
url_paper = 'https://dl.acm.org/ft_gateway.cfm?id=%s'


class ACM(object):
    def __init__(self, cid, issue_id, out_dir=None):
        self.cid = cid
        if out_dir is None:
            self.out_dir = cid
        else:
            self.out_dir = out_dir
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        self.papers = []
        self.cookies = {}

    def parse_papers(self, cid):
        url = url_conference % cid
        response = requests.get(url, cookies=self.cookies, headers=headers)
        self.cookies.update(response.cookies)
        parser = ConferenceParser(self.out_dir)
        parser.feed(response.text)
        return parser.papers

    def download_paper(self, pid):
        url = url_paper % pid
        response = requests.get(url, cookies = self.cookies, headers=headers)
        self.cookies.update(response.cookies)
        filename = os.path.join(self.out_dir, '%s.pdf' % pid)
        print filename
        with open(filename, 'wb') as f:
            f.write(response.content)

    def download_papers(self):
        self.papers = self.parse_papers(self.cid)
        for p in self.papers:
            self.download_paper(p)
