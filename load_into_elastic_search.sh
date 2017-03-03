#!/bin/bash

curl -XDELETE 'localhost:9200/music?pretty&pretty'
curl -XPOST 'http://localhost:9200/_bulk' --data-binary @beetdb_s.json; echo
