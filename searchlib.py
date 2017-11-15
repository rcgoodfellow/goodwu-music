import json
import sys
from elasticsearch import Elasticsearch
from itertools import groupby
from common import Work
import pprint

def delete(id_):
    es = Elasticsearch(['elasticsearch:9200'])
    res = es.delete(index="music", doc_type="performance", id=id_)

def search(q):
    es = Elasticsearch(['elasticsearch:9200'])
    res = es.search(
            index="music", 
            body={
                "min_score": 0.1, 
                "from":0, 
                "size":47, 
                "query": {"match": {"_all": q}}
            }
    )
    hits = map(lambda x: x['_source'], res['hits']['hits'])

    #multilevel sort
    hits = sorted(hits, key=lambda x: (x['composer'], x['title'], ))

    results = []
    pp = pprint.PrettyPrinter(indent=2)

    for s in hits:
        print(s)
        w = Work()
        w.composer = s['composer']
        w.title = s['title']
        w.catalogue = s['catalogue']
        w.venue = s['venue']
        w.recording_date = s['recording_date']
        w.tags = s['tags']
        w.id = s['id']

        for x in s['musicians']:
            w.musicians.append((x[0], x[1]))

        for x in s['movements']:
            w.movements.append(x)

        for k,v in s['files'].items():
            w.files[int(k)] = v

        pp.pprint(w.__dict__)
        results.append(w)

    return results

def index(x):
    es = Elasticsearch(['elasticsearch:9200'])
    doc = json.dumps(x.__dict__)
    print("DICT")
    print(x.__dict__)
    print("INDEX")
    print(doc)
    #id_ = "%s_%s_%s_%s"%(x.composer, x.title, x.venue, x.recording_date)
    if x.id == '':
        res = es.index(index="music", doc_type="performance", body=doc)
    else:
        res = es.index(index="music", doc_type="performance", id=x.id, body=doc)

    x.id = res['_id']
