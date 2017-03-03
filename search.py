#!/usr/bin/env python3

import json
import sys
from elasticsearch import Elasticsearch

if len(sys.argv) != 2:
    print("usage: search 'query'")
    sys.exit(1)


es = Elasticsearch()
res = es.search(index="music", body={"query": {"match": {"_all": sys.argv[1]}}})
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

#res = es.search(index="music", body={"query": {"match_all": {}}})
#print(json.dumps(res, indent=2))
