#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2013 - Aug 31th & Sep 1st (1)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece(
        "Pirate King",
        "The Pirate King",
        ["The Pirate King"],
        movements("Arrrg", "yaaaar")
        )
cd.pieces.append(p)

p = Piece(
        "Preludes, Book II",
        "Claude Debussy",
        ["Julio Elizalde"],
        movements(
            "Brouillards",
            "Feuilles Mortes",
            "La Puerta del Vino",
            "Les Fees Sont d exquises Danseuses",
            "Bruyeres",
            "General Lavine, Excentric",
            "La Terrasse des Audiences du Clair de Lune",
            "Ondine",
            "Hommage a S Pickwick Esq PPMPC",
            "Canope",
            "Les Tierces Alternees",
            "Feux d artifice")
        )
cd.pieces.append(p)

tagit(cd)
