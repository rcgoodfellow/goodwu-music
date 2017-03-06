#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2013 - Aug 17th & 18th (1)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece(
        "Six Moments",
        "Franz Schubert",
        ["Julio Elizalde"],
        [
            Movement(1, "Moderato"),
            Movement(2, "Andantino"),
            Movement(3, "Allegro moderato"),
            Movement(4, "Moderato"),
            Movement(5, "Allegro vivace"),
            Movement(6, "Allegretto")
            ]
        )
cd.pieces.append(p)

p = Piece(
        "Rondo",
        "Franz Schubert",
        ["Tien-Hsin Cindy Wu", "Julio Elizalde"],
        [Movement(1, "Rondo")]
        )
cd.pieces.append(p)

tagit(cd)
