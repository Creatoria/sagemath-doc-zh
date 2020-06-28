import fitz
import os
import sys


def toc2chapter(toc):
    di = []
    st = -1
    for t in toc:
        if t[0] == 1:
            di.append([t[1]])
            st += 1
        else:
            di[st].append(t[1])
    return di


filename = sys.argv[1]
filename = os.path.basename(filename)
filenoext = '.'.join(filename.split('.')[:-1])
basedir = os.path.dirname(filename)
workdir = basedir + filenoext
if not os.path.exists(workdir):
    os.mkdir(workdir)
    os.mkdir(workdir + '/Markdown')
p = fitz.open(filename)
toc = p.getToC()

d = toc2chapter(toc)
ii = 0
for ch in d:
    ii += 1
    jj = 0
    tmpdir = workdir + '/Markdown/CH' + str(ii).zfill(2) + '/'
    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir)
    for page in ch:
        name = str(ii).zfill(2) + '.' + str(jj) + '_' + \
            page.strip().replace('/', ' ').replace('?', ' ').replace(' ', '_') + '.md'
        open(tmpdir + name, 'w').close()
        jj += 1
