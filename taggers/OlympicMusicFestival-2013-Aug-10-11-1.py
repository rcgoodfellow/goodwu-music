#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2013 - Aug 10th & 11th (1)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece(
        "String Trio No. 2",
        "Ludwig van Beethoven",
        ["Emily Dagget Smith", "Tien-Hsin Cindy Wu", "Matthew Zalkind"],
        [
            Movement(1, "Allegretto"),
            Movement(2, "Andante quasi allegretto"),
            Movement(3, "Menuetto: Allegro"),
            Movement(4, "Rondo: Allegro")
            ]
        )
cd.pieces.append(p)

p = Piece(
        "Piano Quartet 1943",
        "William Walton",
        ["Emily Dagget Smith", "Alan Iglitzin", "Matthew Zalkind", 
            "Julio Elizalde"],
        [
            Movement(1, "Allegramente"),
            Movement(2, "Allegro scherzando"),
            Movement(3, "Andante tranquillo"),
            Movement(4, "Allegro molto")
            ]
        )
cd.pieces.append(p)

tagit(cd)
