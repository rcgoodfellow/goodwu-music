#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2013 - Aug 17th & 18th (2)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece(
        "Impromptu No. 1",
        "Franz Schubert",
        ["Julio Elizalde"],
        [Movement(1, "Impromptu")]
        )
cd.pieces.append(p)

p = Piece(
        "Impromptu No. 1",
        "Franz Schubert",
        ["Tien-Hsin Cindy Wu", "Julio Elizalde"],
        [
            Movement(1, "Andante molto"),
            Movement(2, "Allegretto"),
            Movement(3, "Andantino"),
            Movement(4, "Allegro vivace"),
            ]
        )
cd.pieces.append(p)

tagit(cd)
