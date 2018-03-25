from HTMLParser import HTMLParser
import json
import requests
import sqlite3

cookies = {}
uid = '3134060'

from acm import ACM


class PageParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.doc = {'references':[], 'citedby':[]}
        self.section = None

    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            d = dict(attrs)
            if 'name' in d and d['name'].startswith('citation_'):
                name = d['name'][9:]
                content = d['content']
                self.doc[name] = content
        elif tag == 'a':
            d = dict(attrs)
            if 'name' in d:
                name = d['name']
                self.section = name if name in ['references', 'citedby'] else None
            if self.section is not None and 'href' in d and d['href'].startswith('citation.cfm?'):
                query = d['href'][13:]
                for p in query.split('&'):
                    a = p.split('=')
                    if a[0] == 'id':
                        self.doc[self.section].append(a[1])

class ConferenceParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.papers = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs_dict = dict(attrs)
            if 'href' in attrs_dict and 'doi.org' in attrs_dict['href']:
                pid = attrs_dict['href'].split('.')[-1]
                self.papers.append(pid)

def download_doc(uid):
    global cookies
    url = 'http://dl.acm.org/citation.cfm?id=' + uid + '&preflayout=flat'
    print url
    r = requests.get(url, cookies = cookies, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'})
    cookies.update(r.cookies)
    parser = PageParser()
    parser.feed(r.text)
    pdf_url = parser.doc['pdf_url']
    print "pdf_url: ", pdf_url
    pdf = requests.get(pdf_url, cookies = cookies, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'})
    with open('b.pdf', 'wb') as f:
        f.write(pdf.content)

def try_a(paper):
    global cookies
    url = 'https://dl.acm.org/ft_gateway.cfm?id=%s' % paper
    response = requests.get(url, cookies = cookies, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'})
    cookies.update(response.cookies)
    import bpdb; bpdb.set_trace()

def parse_conference(cid):
    url = 'https://dl.acm.org/citation.cfm?id=%d&preflayout=flat#prox' % cid
    response = requests.get(url, cookies = cookies, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'})
    print 'Conference URL: ', url
    parser = ConferenceParser()
    parser.feed(response.text)
    return parser.papers

    #download_doc(uid)

# CCS 2017
cid = '3133956'


def work(cid):
    conference = ACM(cid)
    conference.download_papers()

if __name__ == '__main__':
    work(cid)
