#!/usr/bin/env python3

import json
import sys
from elasticsearch import Elasticsearch

if len(sys.argv) != 2:
    print("usage: search 'query'")
    sys.exit(1)


es = Elasticsearch(['localhost:9200'])
res = es.search(index="music", body={"min_score": 0.1, "from":0, "size":47, "query": {"match": {"_all": sys.argv[1]}}})
hits = map(lambda x: x['_source'], res['hits']['hits'])

#multilevel sort
hits = sorted(hits, key=lambda x: (x['composer'], x['piece'], int(x['movement'])))

for s in hits:
    print("[%s]: %s:%d %s ~ %s"%(
        s['composer'], 
        s['piece'], 
        int(s['movement']), 
        s['title'], 
        s.get('performers', '').replace(";", ", "))
    )

