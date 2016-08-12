#!/usr/bin/env python

import json
from copy import deepcopy

inputname = 'triaNotebook.ipynb'
with open(inputname) as fid:
    nbo = json.load(fid)
nbi = deepcopy(nbo)
nbo = deepcopy(nbo)

for cl in nbi['cells']:
    if 'outputs' in cl.keys():
        cl['outputs'] = []
    if 'execution_count' in cl.keys():
        cl['execution_count'] = None

for cl in nbo['cells']:
    if 'source' in cl.keys():
        cl['source'] = ''

nbis = json.dumps(nbi)
nbos = json.dumps(nbo)
a, b = inputname.split('.')
nbin = a + '_input.' + b
nbon = a + '_output.' + b

with open(nbin, 'w') as fid:
    fid.write(nbis)
with open(nbon, 'w') as fid:
    fid.write(nbos)
