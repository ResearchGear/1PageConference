import sys, os
import subprocess

paper_dir = "MICRO2017"
output_file = "MICRO2017-first.pdf"

def run_command(*popenargs, **kwargs):
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(retcode, cmd)
    return output.split('\n')


def first_page(paper_dir, output_file):
    if os.path.exists(output_file):
        os.remove(output_file)
    paper_list = os.listdir(paper_dir)
    for f in  paper_list:
        if not f.endswith('.pdf'):
            paper_list.remove(f)
    paper_list = ['%s/%s' % (paper_dir, x) for x in paper_list]


    for f in paper_list:
        if not os.path.exists(output_file):
            command = ['pdftk', f, 'cat', '1', 'output', 'tmp.pdf']
            run_command(command)
        else:
            command = ['pdftk', 'B=%s' % output_file, 'A=%s' % f, 'cat', 'B', 'A1', 'output', 'tmp.pdf']
            run_command(command)
        os.rename('tmp.pdf', output_file)
