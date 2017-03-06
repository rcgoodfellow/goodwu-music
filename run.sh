#!/bin/bash

pkill beet

beet web &
./musicsite.py

