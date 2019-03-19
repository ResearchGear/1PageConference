import sys

from acm import ACM
from ieee import IEEE
from first_page import first_page

# CCS 2017
# cid = '3133956'

# Oakland 2017
# cid = '7957740'

libraries = {'ACM': ACM, 'IEEE': IEEE}

def work(l, cid, issue_id, output_file):
    conference = libraries[l](cid, issue_id)
    conference.download_papers()
    print "Creating a single PDF file. It may take a few minutes."
    first_page(conference.out_dir, output_file)
    print "Success! Created " + str(output_file)

if __name__ == '__main__':
    library = sys.argv[1]
    if library == 'IEEE':
        cid, issue_id, output_file = sys.argv[2], sys.argv[3], sys.argv[4]
    elif library == 'ACM':
        issue_id = ''
        cid, output_file = sys.argv[2], sys.argv[3]
    work(library, cid, issue_id, output_file)

