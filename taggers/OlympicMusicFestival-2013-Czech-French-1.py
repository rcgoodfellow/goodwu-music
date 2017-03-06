#!/usr/bin/env python3

from classical import *

cd = CD(
        'Olympic Music Festival 2013 - Czech & French Soundscapes (1)',
        'Olympic Music Festival Artists',
        [
            Piece(
                'Sonata for 2 Violins and Piano',
                'Bohuslav Martinů',
                ['Jessica Lee', 'Tien-Hsin Cindy Wu', 'Julio Elizalde'],
                [
                    Movement(1, 'Allegro poco moderato'),
                    Movement(2, 'Andante. Allegro')
                    ]
                ),
            Piece(
                'String Quartet No. 11',
                'Antonín Dvořák',
                ['Jessica Lee', 'Tien-Hsin Cindy Wu', 'Alan Iglitzin', 'Patrick Jee'],
                [
                    Movement(1, 'Allegro'),
                    Movement(2, 'Poco adagio e molto cantabile'),
                    Movement(3, 'Allegro vivo'),
                    Movement(4, 'Finale Vivace')
                    ]
                )
            ]
        )


tagit(cd)
