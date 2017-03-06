#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2013 - Aug 31th & Sep 1st (2)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece(
        "Pirate King",
        "The Pirate King",
        ["The Pirate King"],
        movements("Commentary on Beethoven String Quartet No. 12")
        )
cd.pieces.append(p)

p = Piece(
        "String Quartet No. 12",
        "Ludwig van Beethoven",
        ["Jessica Lee", "Tien-Hsin Cindy Wu", "Alan Iglitzin", "Patric Jee"],
        movements(
            "Maestoso - Allegro",
            "Adagio, ma non troppo e molto cantabile",
            "Scherzo Vivace",
            "Finale Allegro - Allegro comoco"
            )
        )
cd.pieces.append(p)

tagit(cd)
