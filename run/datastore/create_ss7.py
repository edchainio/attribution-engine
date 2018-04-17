#!/usr/bin/env python3


import json

from pprint import pprint


ss6_attrs = json.load(open('searchspace6.json'))['attributions']
ss7_attrs = {'attributions':[]}

for _ in ss6_attrs:
    _['deep_link'] = 'https://www.youtube.com/watch?v=ZK3O402wf1c'
    ss7_attrs['attributions'].append(_)

ss7 = json.dumps(ss7_attrs)

with open('searchspace7.json', 'w') as f:
    f.write(ss7)

pprint(ss7_attrs['attributions'])
