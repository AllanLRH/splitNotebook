#!/usr/bin/env python

import json
from copy import deepcopy

inputnameLst = ['triaNotebook_input.ipynb', 'triaNotebook_output.ipynb']
with open(inputnameLst[0]) as fid:
    nbi = json.load(fid)
with open(inputnameLst[1]) as fid:
    nbo = json.load(fid)

nbc = deepcopy(nbi)
for cc, co in zip(nbc['cells'], nbo['cells']):
    if 'execution_count' in co:
        cc['execution_count'] = co['execution_count']
    if 'outputs' in co:
        cc['outputs'] = co['outputs']

nbon = 'trialNotebook_combined.ipynb'
with open(nbon, 'w') as fid:
    json.dump(nbc, fid)

