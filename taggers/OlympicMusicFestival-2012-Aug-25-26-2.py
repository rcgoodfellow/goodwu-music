#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2012 - Aug 25th & 26th (2)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece(
        "Dialogues for Violin and Cello",
        "Michael Brown",
        ["Arnaud Sussmann", "Nicholas Canellakis"],
        [Movement(1, "Dialogues for Violin and Cello")]
        )
cd.pieces.append(p)

p = Piece(
        "String Sextet No. 2",
        "Johannes Brahms",
        ["Arnold Sussmann", "Jessica Lee", "Alan Iglitzin", 
            "Tien-Hsin Cindy Wu", "Nicholas Canellackis", "Patrick Jee"],
        [
            Movement(1, "Allegro non troppo"),
            Movement(2, "Scherzo - Allegro non troppo"),
            Movement(3, "Poco adagio"),
            Movement(4, "Poco allegro")
            ]
        )
cd.pieces.append(p)
tagit(cd)

