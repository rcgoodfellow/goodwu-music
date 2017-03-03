#!/bin/bash

curl localhost:8337/item/ | python3 -m json.tool > beetdb.json
jq -c '
.[] |
.[] |
{ index: { _index: "music", _type: "movement" } },
. ' beetdb.json > beetdb_s.json
