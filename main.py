import sys

from acm import ACM
from ieee import IEEE
from first_page import first_page

# CCS 2017
# cid = '3133956'

# Oakland 2017
# cid = '7957740'

libraries = {'ACM': ACM, 'IEEE': IEEE}

def work(l, cid, output_file):
    conference = libraries[l](cid)
    conference.download_papers()
    first_page(conference.out_dir, output_file)

if __name__ == '__main__':
    library, cid, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    work(library, cid, output_file)
