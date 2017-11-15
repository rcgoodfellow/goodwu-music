#!/bin/bash

export FLASK_APP=musicsite.py

#pkill beet

#beet web 10.47.1.5 &
#./musicsite.py

flask run --host=10.47.1.5

