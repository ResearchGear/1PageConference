import sys

from acm import ACM
from first_page import first_page

# CCS 2017
#cid = '3133956'

def work(cid, output_file):
    conference = ACM(cid)
    conference.download_papers()
    first_page(conference.out_dir, output_file)

if __name__ == '__main__':
    cid, output_file = sys.argv[1], sys.argv[2]
    work(cid, output_file)
