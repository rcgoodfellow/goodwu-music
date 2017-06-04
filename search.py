#!/usr/bin/env python3

import json
import sys
from elasticsearch import Elasticsearch
from common import Work
import pprint

pp = pprint.PrettyPrinter(indent=2)

if len(sys.argv) != 2:
    print("usage: search 'query'")
    sys.exit(1)


es = Elasticsearch(['localhost:9200'])
res = es.search(index="music", body={"min_score": 0.1, "from":0, "size":47, "query": {"match": {"_all": sys.argv[1]}}})
hits = map(lambda x: x['_source'], res['hits']['hits'])

#multilevel sort
hits = sorted(hits, key=lambda x: (x['composer'], x['title'], ))

results = []

for s in hits:
    w = Work()
    w.composer = s['composer']
    w.title = s['title']
    w.catalogue = s['catalogue']
    w.recording_date = s['recording_date']
    w.composition_date = s['composition_date']
    w.tags = s['tags']

    for x in s['musicians']:
        w.musicians.append((x[0], x[1]))

    for x in s['movements']:
        w.movements.append(x)

    for k,v in s['files'].items():
        w.files[int(k)] = v

    """
    print(
        "[%s]: %s %s %s %s %s %s"%(
            s['composer'], 
            s['title'],
            s['musicians'],
            s['movements'],
            s['files'],
            s['recording_date'],
            s['composition_date'],
        )
    )
    """
    pp.pprint(w.__dict__)

