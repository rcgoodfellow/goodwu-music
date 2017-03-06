import json
import sys
from elasticsearch import Elasticsearch
from itertools import groupby


def search(q):
    es = Elasticsearch()
    res = es.search(index="music", body={"min_score": 0.1, "from":0, "size":4700, "query": {"match": {"_all": q}}})
    hits = map(lambda x: x['_source'], res['hits']['hits'])

    #multilevel sort
    hits = sorted(hits, key=lambda x: (x['composer'], x['piece'], int(x['movement'])))

    groups = []
    for _, group in groupby(hits, lambda x: (x['composer'], x['piece'])):
        groups.append(list(group))

    return groups
