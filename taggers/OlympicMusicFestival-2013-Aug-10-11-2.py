#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2013 - Aug 10th & 11th (2)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece(
        "Capriccio for Cello and Piano",
        "Lukas Foss",
        ["Matthew Zalkind", "Julio Elizalde"],
        [Movement(1, "Capriccio for Cello and Piano")],
        )
cd.pieces.append(p)

p = Piece(
        "String Quartet No. 10",
        "Antonin Dvorak",
        ["Emily Dagget Smith", "Tien-Hsin Cindy Wu", "Alan Iglitzin",
            "Matthew Zalkind"],
        [
            Movement(1, "Allegro ma non troppo"),
            Movement(2, "Dumka: Andante con moto Vivace"),
            Movement(3, "Romanza: Andante con moto"),
            Movement(4, "Finale: Allegro assai")
            ]
        )
cd.pieces.append(p)

tagit(cd)
