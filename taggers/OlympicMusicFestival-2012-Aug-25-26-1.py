#!/usr/bin/env python3

from classical import *

cd = CD()
cd.title = 'Olympic Music Festival 2012 - Aug 25th & 26th (1)'
cd.artists = 'Olympic Music Festival Artists'

p = Piece()
p.title = 'Suite Italienne'
p.composer = 'Igor Stravinsky'
p.performers = ['Arnaud Sussmann', 'Julio Elizalde']
p.movements = [
        Movement(1, 'Introduzione - Allegro moderato'),
        Movement(2, 'Serenata - Larghetto'),
        Movement(3, 'Aria - Allegro all breve - Largo'),
        Movement(4, 'Tarantella - Vivace'),
        Movement(5, 'Minuetto e Finale - Moderato - Molto Vivace')
        ]

cd.pieces.append(p)

p = Piece(
        "Piano Quintet No. 1",
        "Ernst Bloch",
        ["Arnold Sussmann", "Jessica Lee", "Alan Iglitzin", 
            "Nicholas Canellackis", "Julio Elizalde"],
        [
            Movement(1, "Agitato"),
            Movement(2, "Andante mistico"),
            Movement(3, "Allegro energico")
            ]
        )
cd.pieces.append(p)


tagit(cd)

